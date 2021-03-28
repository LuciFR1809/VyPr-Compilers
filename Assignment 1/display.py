def display():
	fname = input('Enter filename (default: code.vypr):') or ' '

	if fname == ' ':
		file = open("code.vypr", 'r', encoding='utf8')
	else:
		file = open(f'{fname}', 'r', encoding='utf8')

	print(file.read())
	file.close()


if __name__ == '__main__':
	display()
