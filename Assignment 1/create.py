def create():
	fname = input('Enter filename (default: code.vypr):') or ' '
	if fname == ' ':
		file = open('code.vypr', 'w', encoding='utf8')
		file.write("import modulename\nint main()\n{\nreturn 0;\n}")
	else:
		file = open(f'{fname}.vypr', "w", encoding='utf8')
		print(
			'What Do You Want To Write To Your File? [Write "EOF" (without quotes) to end]:')
		print('> ', end='')
		text = input()
		while text != 'EOF':
			file.write(text+'\n')
			print('> ', end='')
			text = input()
	file.close()
	print("File Created...")


if __name__ == '__main__':
	create()
