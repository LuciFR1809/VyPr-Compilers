# BLACK = \033[0;30m
# RED = \033[0;31m
# GREEN = \033[0;32m
# BROWN = \033[0;33m
# BLUE = \033[0;34m
# PURPLE = \033[0;35m
# CYAN = \033[0;36m
# YELLOW = \033[1;33m
# BOLD = \033[1m
# FAINT = \033[2m
# ITALIC = \033[3m
# UNDERLINE = \033[4m
# BLINK = \033[5m
# NEGATIVE = \033[7m
# CROSSED = \033[9m
# END = \033[0m
def other():
    print('''
	A Parser Program for toy lang vYpr
			   \033[1mGROUP 21\033[0m\033[0;36m
		+----------------+---------------+
		|      NAME      |    ID NO.     |
		+----------------+---------------+
		| Ashna Swaika   | 2018A7PS0027H |
		| Abhishek Bapna | 2018A7PS0184H |
		| Kumar Pranjal  | 2018A7PS0163H |
		| Ashish Verma   | 2018A7PS0009H |
		+----------------+---------------+
\033[1;0m
	Toy Language creation in python for Compilers Construction (CS F363)
 
	\033[0;34m 		Part 1: \033[0m
 	Functionalities enabled\033[0;32m
	[\u2713] Created DFA
	[\u2713] Created lexeme() function which can be called repeatedly
	[\u2713] Removes Whitespace
	[\u2713] Removes Comments
	[\u2713] CLI created for easy operation\033[0;0m
 
   	\033[0;34m		Part 2: \033[0m
	Functionalities enabled\033[0;32m
	[\u2713] Created CFG of language
	[\u2713] Created LALR(1) parse table for vYpr
	[\u2713] Expand language constructs
	[\u2713] Syntax analysis
	[\u2713] Error handling while parsing\033[0;0m
 
   	Fuctionalities on check list:\033[0;31m
	[ ] Compile and execute vYpr programs
\033[0;0m''')


if __name__ == '__main__':
    other()
