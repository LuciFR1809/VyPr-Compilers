#BLACK = \033[0;30m
#RED = \033[0;31m
#GREEN = \033[0;32m
#BROWN = \033[0;33m
#BLUE = \033[0;34m
#PURPLE = \033[0;35m
#CYAN = \033[0;36m
#YELLOW = \033[1;33m
#BOLD = \033[1m
#FAINT = \033[2m
#ITALIC = \033[3m
#UNDERLINE = \033[4m
#BLINK = \033[5m
#NEGATIVE = \033[7m
#CROSSED = \033[9m
#END = \033[0m
import os
import time

from create import create
from display import display
from lexer import lexer
from other import other
cls = lambda: os.system('cls')
cls()
print('''
			  Welcome to\033[1;33m

		██╗░░░██╗██╗░░░██╗██████╗░██████╗░
		██║░░░██║╚██╗░██╔╝██╔══██╗██╔══██╗
		╚██╗░██╔╝░╚████╔╝░██████╔╝██████╔╝
		░╚████╔╝░░░╚██╔╝░░██╔═══╝░██╔══██╗
		░░╚██╔╝░░░░░██║░░░██║░░░░░██║░░██║
		░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝
\033[0m 
	  \033[1mA Lexical Analyser Program for Toy Lang VYPR\033[0m''')
time.sleep(1)
print('''
			   \033[1mGROUP 21\033[0m \033[0;36m
		+----------------+---------------+
		|      NAME      |    ID NO.     |
		+----------------+---------------+
		| Ashna Swaika   | 2018A7PS0027H |
		| Abhishek Bapna | 2018A7PS0184H |
		| Kumar Pranjal  | 2018A7PS0163H |
		| Ashish Verma   | 2018A7PS0009H |
		+----------------+---------------+
\033[1;0m''')
time.sleep(1)

option = input('''\033[0;32m
COMMANDS:
Create File            -->     CREATE
Display Code           -->     SHOW
Show Lexical Analysis  -->     LEX
Other Details          -->     OTHER\033[0m \033[0;31m
Quit                   -->     QUIT
\033[0m
ACTION:''')
print()
while option.upper() != 'QUIT':

	if option.upper() == 'CREATE':
		create()


	elif option.upper() == 'SHOW':
		display()

	elif option.upper() == 'LEX':
		fname = input('Enter filename (default: code.vypr):') or ' '
		if fname == ' ':
			fname = "code.vypr"
		else:
			fname = f'{fname}'
		try:
			lexer(fname)
		except FileNotFoundError:
			print('\033[0;31m File not found... \033[0m')
			continue

	elif option.upper() == 'OTHER':
		other()

	else:
		print('\033[0;31m \nCommand not found. Use following available commands \033[0m')

	option = input('''\033[0;32m
COMMANDS:
Create File            -->     CREATE
Display Code           -->     SHOW
Show Lexical Analysis  -->     LEX
Other Details          -->     OTHER\033[0m \033[0;31m
Quit                   -->     QUIT
\033[0m
ACTION:''')
print('\033[3mNow leaving \033[1mVYPR \033[0m\n')
