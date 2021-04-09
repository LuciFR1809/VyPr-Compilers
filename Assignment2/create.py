#black=\033[30m
#red=\033[31m
#green=\033[32m
#orange=\033[33m
#blue=\033[34m
#purple=\033[35m
#cyan=\033[36m
#lightgrey=\033[37m
#darkgrey=\033[90m
#lightred=\033[91m
#lightgreen=\033[92m
#yellow=\033[93m
#lightblue=\033[94m
#pink=\033[95m
#lightcyan=\033[96m
#BOLD = \033[1m
#FAINT = \033[2m
#ITALIC = \033[3m
#UNDERLINE = \033[4m
#BLINK = \033[5m
#NEGATIVE = \033[7m
#CROSSED = \033[9m
#END = \033[0m
from time import sleep
import sys
import os

from remove import remove
def del_lines(i, fname):
    for j in range(i):
        sys.stdout.write('\x1b[1A')
        remove(fname)

def delete_1_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def create():
	fname = input('\033[32mEnter filename (default: code.vypr):\033[0m') or ' '

	if fname == ' ':
		file = open('code.vypr', 'w', encoding='utf8')
		file.write("import modulename\nint main()\n{\n	return 0;\n}")
	else:
		file = open(f'{fname}.vypr', "w", encoding='utf8')
		print('''\033[32mWhat Do You Want To Write To Your File? 
        [Write "$EOF" (without quotes) to end]
        [Write "$RET" (without quotes) to delete upper line]
        [Write "$REM" (without quotes) to clear file]\033[0m''')
		print('***START***')
		print('> ', end='')
		text = input()
		x=0
		while text != '$EOF' and text!='\n$EOF':
			if(text=='$RET' or text=='\n$RET'):
				file.close()
				delete_1_line()
				del_lines(1,f'{fname}.vypr')
				file=open(f'{fname}.vypr',"a+")
				print('> ', end='')
				text =input()
				x=x-1
			elif (text=='$REM' or text =='\n$REM'):
				delete_1_line()
				for j in range(x):
					delete_1_line()
				file.close()
				with open(f'{fname}.vypr','w') as f:
					f.write('')
				file=open(f'{fname}.vypr',"a+")
				print('> ', end='')
				text = input("\b ")
			else:
				file.write(text+'\n')
				print('> ', end='')
				text = input()
				x=x+1
	file.close()

	print("\033[93mFile Created Successfully...\033[0m")

if __name__ == '__main__':
	create()
