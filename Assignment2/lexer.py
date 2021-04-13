# Compiler Construction CSF363 Assignment
# Phase 1 - Lexical Analysis
# Made by --
# Kumar Pranjal - 2018A7PS0163H
# Ashna Swaika - 2018A7PS0027H
# Abhishek Bapna - 2018A7PS0184H
# Ashish Verma - 2018A7PS0009H

# black=\033[30m
# red=\033[31m
# green=\033[32m
# orange=\033[33m
# blue=\033[34m
# purple=\033[35m
# cyan=\033[36m
# lightgrey=\033[37m
# darkgrey=\033[90m
# lightred=\033[91m
# lightgreen=\033[92m
# yellow=\033[93m
# lightblue=\033[94m
# pink=\033[95m
# lightcyan=\033[96m
# BOLD = \033[1m
# FAINT = \033[2m
# ITALIC = \033[3m
# UNDERLINE = \033[4m
# BLINK = \033[5m
# NEGATIVE = \033[7m
# CROSSED = \033[9m
# END = \033[0m

# Code starts here
import sys


# Storing tokens in lists
keywords = ['int', 'float', 'do', 'void', 'boolean', 'string', 'for', 'if', 'else',
            'while', 'break', 'continue', 'switch', 'default', 'return', 'case', 'import', 'true', 'false']

operators = ['+=', '-=', '*=', '/=', '%=', '==', '<=', '>=', '!=', '<<',
                         '>>', '&&', '||', '+', '-', '*', '%', '/', '=', '!', '<', '>']

delimiters = [';', ',', '(', ')', '{', '}', '\n', '\r', '\t', '\\']

string_term = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

legal_term = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
              'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

numeric_term = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sign_term = ['+', '-']


def DFA(check_str, prev_op, prev_lex):
    '''
    Internal function used by lexeme() function to find a token
    '''
    matches = []
    pairs = []

    # check for end of string
    if check_str[0] == "$" and len(check_str) == 1:
        return None, None, None

    # check for blank space
    if check_str[0] == " ":
        return check_str[1:], None, None

    # check for keyword
    key_match = [check_str.startswith(x) for x in keywords]
    if any(key_match):
        key = keywords[key_match.index(True)]
        matches.append(len(key))
        pairs.append(['keyword', key])

    # check for operators
    key_match = [check_str.startswith(x) for x in operators]
    if any(key_match):
        key = operators[key_match.index(True)]
        matches.append(len(key))
        if key in sign_term and (prev_op == 'operator' or prev_op == 'keyword' or prev_lex == '{' or prev_lex == '('):
            pairs.append(['sign'+key, key])
        else:
            pairs.append(['operator', key])

    # check for delimiters
    key_match = [check_str.startswith(x) for x in delimiters]
    if any(key_match):
        key = delimiters[key_match.index(True)]
        matches.append(len(key))
        pairs.append(['delimiter', key])

    # check for identifier
    if check_str[0] in string_term:
        for index, letter in enumerate(check_str):
            if letter not in legal_term:
                matches.append(index)
                pairs.append(['identifier', check_str[:index]])
                break

    # check for string literal
    if check_str[0] == '"':
        for index, letter in enumerate(check_str[1:]):
            if letter == '"' and check_str[index] != '\\':
                matches.append(index+2)
                pairs.append(['string literal', check_str[:index+2]])
                break

    # check for numerical literal
    if check_str[0] in numeric_term or check_str[0] in sign_term:
        isFloat = False
        for index, letter in enumerate(check_str[1:]):
            if letter not in numeric_term:
                if letter == '.' and not isFloat:
                    isFloat = True
                else:
                    if prev_op == 'sign+' or prev_op == 'sign-':
                        matches.append(index+2)
                        orig_str = check_str[:index+1]
                        if isFloat:
                            pairs.append(
                                ['floating_literal', prev_op[-1] + orig_str])
                            break
                        else:
                            pairs.append(
                                ['integer_literal', prev_op[-1] + orig_str])
                            break
                    else:
                        matches.append(index+1)
                        if isFloat:
                            pairs.append(
                                ['floating_literal', check_str[:index+1]])
                            break
                        else:
                            pairs.append(
                                ['integer_literal', check_str[:index+1]])
                            break

    # check for comment
    if check_str[0] == '#':
        matches.append(len(check_str))
        pairs.append([None, None])

    # now find the token for longest matching lexeme
    # final is final index in matches which should be used for token lexeme pairs
    if(len(matches)) == 0:
        if len(check_str) > 1:
            return check_str[1:], 'invalid', check_str[0]
        else:
            return None, 'invalid', check_str[0]

    final = matches.index(max(matches))

    # SPECIAL CASE - sign operators
    if (prev_op != 'operator' or prev_op != 'keyword' or prev_lex != '{' or prev_lex != '(') and check_str[0] in sign_term:
        final = 0

    end_pos = int(matches[final])
    if end_pos < len(check_str):
        if (prev_op == 'sign+' or prev_op == 'sign-') and (pairs[final][0] == 'floating_literal' or pairs[final][0] == 'integer_literal'):
            end_pos -= 1
        return check_str[end_pos:], pairs[final][0], pairs[final][1]
    elif end_pos == len(check_str):
        return None, pairs[final][0], pairs[final][1]
    else:
        print("\033[31msome error in parsing\033[0m")


def lexeme(string):
    '''
    Accepts a string and returns a generator object containing tokens
    which can be accessed using a for loop or by using next() function
    '''
    lines = string.splitlines()
    for line_number, line in enumerate(lines):
        line = line.strip() + '$'
        prev_op = None
        prev_lex = None
        if len(line) > 0:
            while(line != None):
                line, key, lexeme = DFA(line, prev_op, prev_lex)
                if key is not None and key != 'invalid':
                    prev_op = key
                    prev_lex = lexeme
                if key is not None and key != 'invalid' and key != 'sign+' and key != 'sign-':
                    yield {'line': line_number+1, 'token': key, 'lexeme': lexeme}
                elif key == 'invalid':
                    yield {'line': line_number+1, 'token': 'invalid', 'lexeme': lexeme}


# Driver Code
def lexer(fname=None):
    if fname is None:
        filename = f'Testcases/{sys.argv[1]}'
    else:
        filename = fname
    outfile = open(
        f'{filename.split(".")[0]}_output.txt', 'w', encoding='utf8')
    parsefile = open(
        f'{filename.split(".")[0]}_input_parse.txt', 'w', encoding='utf8')
    with open(filename, 'r', encoding='utf8') as f:
        filestr = f.read()
        for lex in lexeme(filestr):
            if lex['token'] == 'invalid':
                print(
                    f"!!! Error in line {lex['line']} while parsing {lex['lexeme']}")
                print(
                    f"!!! Error in line {lex['line']} while parsing {lex['lexeme']}", file=outfile)
                print(
                    f"{lex['line']} <!> Error <!> {lex['lexeme']}", file=parsefile)

            else:
                print(
                    f"Line: {lex['line']}, Token: {lex['token']}, Lexeme: {lex['lexeme']}")
                print(
                    f"Line: {lex['line']}, Token: {lex['token']}, Lexeme: {lex['lexeme']}", file=outfile)
                print(
                    f"{lex['line']} <!> {lex['token']} <!> {lex['lexeme']}", file=parsefile)


if __name__ == '__main__':
    lexer()
