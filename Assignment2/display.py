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
def display():
    fname = input(
        '\033[0;32mEnter filename (default: code.vypr):\033[0m') or ' '

    if fname == ' ':
        file = open("Testcases/code.vypr", 'r', encoding='utf8')
    else:
        file = open(f'Testcases/{fname}', 'r', encoding='utf8')

    print("\n\033[92m"+file.read()+"\033[0m\n")
    file.close()


if __name__ == '__main__':
    display()
