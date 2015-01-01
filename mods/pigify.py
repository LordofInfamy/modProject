import sys

if len(sys.argv) < 2:
    sys.exit("""You must give a translate request in format:\n"""
	     "!pigify lol")

arg = sys.argv
word = arg[1]
word = word.lower()
first = word[0]
pyg = 'ay'
new_word = word + first + pyg

if original.isalpha():
    new_word = new_word [1:len(new_word)]
    print(new_word.encode("UTF-8"))
else:
	print("Alphanumeric characters only!")
