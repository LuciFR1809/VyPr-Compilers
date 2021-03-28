import os
import time

from create import create
from display import display
from lexer import lexer
from other import other

print('''
			  Welcome to

		██╗░░░██╗██╗░░░██╗██████╗░██████╗░
		██║░░░██║╚██╗░██╔╝██╔══██╗██╔══██╗
		╚██╗░██╔╝░╚████╔╝░██████╔╝██████╔╝
		░╚████╔╝░░░╚██╔╝░░██╔═══╝░██╔══██╗
		░░╚██╔╝░░░░░██║░░░██║░░░░░██║░░██║
		░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝

	  A Lexical Analyser Program for Toy Lang VYPR
	''')
time.sleep(1)
print('''
		+----------------+---------------+
		|      NAME      |    ID NO.     |
		+----------------+---------------+
		| Ashna Swaika   | 2018A7PS0027H |
		| Abhishek Bapna | 2018A7PS0184H |
		| Kumar Pranjal  | 2018A7PS0163H |
		| Ashish Verma   | 2018A7PS0009H |
		+----------------+---------------+
		Group 21
''')
time.sleep(1)

option = input('''
COMMANDS:
Create File            -->     CREATE
Display Code           -->     SHOW
Show Lexical Analysis  -->     LEX
Other Details          -->     OTHER
Quit                   -->     QUIT

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
			print('File not found...')
			continue

	elif option.upper() == 'OTHER':
		other()

	else:
		print('Command not found. Use following available commands')

	option = input('''
COMMANDS:
Create File            -->     CREATE
Display Code           -->     SHOW
Show Lexical Analysis  -->     LEX
Other Details          -->     OTHER
Quit                   -->     QUIT

ACTION:''')
print()
print('Now leaving VYPR')
