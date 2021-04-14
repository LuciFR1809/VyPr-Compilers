import sys
import json
import platform
import subprocess
from lexer import lexer

# list of safe symbols for error recovery
safe_symbols = [';', '}']

# update safe stack to newest safe state
def update_safe(stack):
    return stack.copy()

# bring original stack to safe state
def stack_safe_state(safe_stack):
    return safe_stack.copy()

# bring token in required format as in parse table
def parse_format(lines):
    tokens = []

    for line in lines:
        lin_num, token, lexeme = line.split('<!>')
        token = token.strip()
        lexeme = lexeme.strip('\n')
        lexeme = lexeme.strip()
        if token == 'integer_literal':
            token = 'INT_LIT'
        if token == 'floating_literal':
            token = 'FLT_LIT'
        if token == 'identifier':
            token = 'ID'
        if token == 'string literal':
            token = 'STR_LIT'
        if token == 'operator':
            token = lexeme
        if token == 'delimiter':
            token = lexeme
        if token == 'keyword':
            token = lexeme
        if token == 'stop':
            token = lexeme
        if token == 'Error':
            pass
        tokens.append([lin_num, token, lexeme])

    return tokens

# look up parse table or goto table
def parse_lookup(parse_table, token, number):
    return parse_table[number].get(token, 'Error')

# look up reduce table
def reduce_lookup(reduce_table, number):
    rule = reduce_table[number]
    lines = rule.split('->')
    return lines[0].strip(), lines[1].strip()

# parsing process
def parse(fname=None):

    #get input file
    if fname is None:
        filename = f'Testcases/{sys.argv[1]}'
    else:
        filename = fname

    # get parse table , goto table and reduce table
    with open("Tables/Action Table.json", 'r', encoding='utf8') as f1:
        parse_table = json.load(f1)
    with open("Tables/Goto Table.json", 'r', encoding='utf8') as f2:
        goto_table = json.load(f2)
    with open("Tables/Rules.json", 'r', encoding='utf8') as f3:
        reduce_table = json.load(f3)

    # input file lexical analysis , open input and output parser files
    parse_outf = open( f'{filename.split(".")[0]}_output_parse.txt', "w", encoding='utf8')
    lexer(filename)
    inputfname = f'{filename.split(".")[0]}_input_parse.txt'

    # code to just bring input into required format - lines will contain final (line, token, lexeme) tuple
    with open(inputfname, 'r', encoding='utf8') as f:  
        lines = f.readlines()

        if lines != []:
            last = lines[-1].split('<!>')
            last = [x.strip() for x in last]
            if last != []:
                lines.append(f'{last[0]} <!> stop <!> $')
            else:
                lines.append('0 <!> stop <!> $')

        lines = parse_format(lines)
    
        # stack - has stack contents
        # safe_stack - maintains the last safe state and all symbols inside it
        # tokens - have all tokens - terminals in order of insertion into stack
        # count - keeps a check on which token we currently are looking at
        # steps - is the number of times we go trhough the loop

        stack = ['0']
        safe_stack = ['0']
        tokens = []
        count = 0
        steps = 0

        # get parse_table, reduce_table and goto_table
        while True and count < len(lines):
            lin_num, token, lexeme = lines[count]
            update_safe_stack = False
            print(f'{steps} : {stack}', file=parse_outf)
            steps += 1

            if token in safe_symbols:
                update_safe_stack = True

            # handle lexical error
            if token == 'Error':
                stack = stack_safe_state(safe_stack)
                count += 1
                if token == '$':
                    print(f'\033[93mPARSING FAIL ::: FOUND EOF\033[0m')
                    break

                print(
                    f'\033[35mLexical Error Line number {lin_num} :::: Unidentified character {lexeme} found\033[0m')
                continue

            # look up parse table for next character
            number = stack[-1]
            next_op = parse_lookup(parse_table, token, number)

            # shift action
            if next_op[0] == 's':
                stack.append(token)
                tokens.append(token)
                stack.append(next_op[1:])
                if update_safe_stack:
                        safe_stack = update_safe(stack)
                count += 1
                continue

            # reduce action
            elif next_op[0] == 'r':
                non_terminal, condense = reduce_lookup(reduce_table, next_op[1:])
                condense = condense.split()
                condense.reverse()

                # to pop out elements from the stack
                flag = True
                condense = [i.strip() for i in condense if i]

                if condense[0] != 'ϵ':
                    for i in condense:
                        if flag:
                            stack.pop()
                        if stack[-1] == i:
                            stack.pop()
                            flag = True
                        else:
                            flag = False

                # now look up goto table and find the next rule
                num = stack[-1]
                new_num = parse_lookup( goto_table, non_terminal, num)

                if new_num == 'Error':
                    stack = stack_safe_state(safe_stack)
                    count += 1
                    if token == '$':
                        print(f'\033[93mPARSING FAIL ::: FOUND EOF\033[0m')
                        break
                    expected = []
                    for keys in goto_table[num].keys():
                        expected.append(keys)
                    print(
                        f'\033[0;31mSyntax Error:: Line number {lin_num}, Found {lexeme} Expected one among {expected}, Please check again\033[0m')
                
                else:
                    stack.append(non_terminal)
                    stack.append(new_num)

            elif next_op == 'acc':
                stack.clear()
                stack.append('0')
                stack.append(next_op)
                print(f'{steps} : {stack}', file=parse_outf)
                parse_outf.close()
                print("\033[32mPARSING SUCCESS - accept state reached\033[0m")
                print(f"{filename.split('.')[0]}_output_parse.txt".replace('/', '\\' ))
                if platform.system() == "Windows":
                    subprocess.run(["notepad", f"{filename.split('.')[0]}_output_parse.txt".replace('/', '\\' )])
                elif platform.system() == "Linux":
                    subprocess.run(["gedit",f"{filename.split('.')[0]}_output_parse.txt"])     
                break

            else:
                expected = []
                for keys in parse_table[number].keys():
                    if keys == '$':
                        continue
                    expected.append(keys)
                print(
                    f'\033[0;31mSyntax Error Line number {lin_num} ::::  Found {lexeme} Expected one among {expected} \033[0m')
                stack = stack_safe_state(safe_stack)
                count += 1
                if token  == '$':
                    print(f'\033[93mPARSING FAIL ::: FOUND EOF\033[0m')
                    break
                



if __name__ == '__main__':
    parse()


