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
from progress.bar import Bar
def create():
	fname = input('\033[32mEnter filename (default: code.vypr):\033[0m') or ' '
	if fname == ' ':
		file = open('code.vypr', 'w', encoding='utf8')
		file.write("import modulename\nint main()\n{\n	return 0;\n}")
	else:
		file = open(f'{fname}.vypr', "w", encoding='utf8')
		print(
			'\033[32mWhat Do You Want To Write To Your File? [Write "EOF" (without quotes) to end]:\033[0m')
		print('> ', end='')
		text = input()
		while text != 'EOF':
			file.write(text+'\n')
			print('> ', end='')
			text = input("\033[7m"+"\033[0m")
	file.close()
	with Bar('Processing', max=20) as bar:
		for i in range(20):
			sleep(.05)
			bar.next()
	print("\033[93mFile Created Successfully...\033[0m")


if __name__ == '__main__':
	create()
