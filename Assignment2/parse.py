# ID == identifier
# STR_LIT == string literal
# INT_LIT == integer literal
# FLT_LIT == floating literal

import sys
import json


class Tree(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.depth = 0

    def addnode(self, child):
        self.children.append(child)
        if self.depth <= child.depth:
            self.depth = child.depth+1


def parse_lookup(parse_table, token, number):
    return parse_table[number].get(token, 'Error')


def reduce_lookup(reduce_table, number):
    rule = reduce_table[number]
    lines = rule.split('->')
    return lines[0].strip(), lines[1].strip()


def parse(fname=None):
    if fname is None:
        filename = sys.argv[1]
    else:
        filename = fname

    with open("Action Table.json", 'r', encoding='utf8') as f1:
        parse_table = json.load(f1)

    with open("Goto Table.json", 'r', encoding='utf8') as f2:
        goto_table = json.load(f2)

    with open("Rules.json", 'r', encoding='utf8') as f3:
        reduce_table = json.load(f3)
    
    parse_outf = open(f'{filename.split("_")[0]}_output_parse.txt', "w", encoding='utf8')

    with open(filename, 'r', encoding='utf8') as f:
        lines = f.readlines()
        last = lines[-1].split('<!>')
        last = [x.strip() for x in last]
        if last != []:
            lines.append(f'{last[0]} <!> stop <!> $')
        else:
            lines.append('0 <!> stop <!> $')
        stack = ['0']
        tree_stack = []
        Err_stack = []
        count = 0
        steps = 0
        # get parse_table, reduce_table and goto_table
        while True:
            lin_num, token, lexeme = lines[count].split('<!>')
            token = token.strip()
            lexeme = lexeme.strip('\n')
            lexeme = lexeme.strip()
            print(f'{steps} : {stack}', file=parse_outf)
            steps+=1
            # bring token in required format as in parse table

            if token == 'integer_literal':
                token = 'INT_LIT'
            if token == 'floating_literal':
                token = 'FLT_LIT'
            if token == 'identifier':
                token = 'ID'
            if token == 'string_literal':
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
                print(
                    f'\033[0;31mLexical Error:: Line number {lin_num}, UnIdentified character {lexeme} found\033[0m')
                Err_stack.append(
                    f'Lexical Error:: Line number {lin_num}, UnIdentified character {lexeme} found')
                continue

            # look up parse table for next character
            next_op = parse_lookup(parse_table, token, stack[-1])

            # shift action
            if next_op[0] == 's':
                stack.append(token)
                tree_stack.append(Tree(token))
                stack.append(next_op[1:])
                count += 1
                continue

            # reduce action
            elif next_op[0] == 'r':
                non_terminal, condense = reduce_lookup(
                    reduce_table, next_op[1:])
                parent = Tree(non_terminal)
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
                            parent.addnode(tree_stack.pop())
                            stack.pop()
                            flag = True
                        else:
                            flag = False

                # now look up goto table and find the next rule
                new_num = parse_lookup(
                    goto_table, non_terminal, stack[-1])

                if new_num == 'Error':
                    print(
                        f'\033[0;31mSyntax Error:: Line number {lin_num}, Wrong Syntactic Input {lexeme}, Please check again\033[0m')
                    Err_stack.append(
                        f'Syntax Error:: Line number {lin_num}, Wrong Syntactic Input {lexeme}, Please check again')
                else:
                    stack.append(non_terminal)
                    tree_stack.append(parent)
                    stack.append(new_num)

            elif next_op == 'acc':
                stack.append(next_op)
                print(f'{steps} : {stack}', file=parse_outf)
                parse_outf.close()
                print("SUCCESS")
                break

            else:
                print(
                    f'\033[0;31mSyntax Error:: Line number {lin_num}, Wrong Syntactic Input {lexeme}, Please check again\033[0m')
                Err_stack.append(
                    f'Syntax Error:: Line number {lin_num}, Wrong Syntactic Input {lexeme}, Please check again')
                prev_lin_num = lin_num
                while prev_lin_num == lin_num:
                    count += 1
                    lin_num, token, lexeme = lines[count].split('<!>')
            
            


if __name__ == '__main__':
    parse()
