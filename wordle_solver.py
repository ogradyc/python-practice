
# I want to practice regular expressions by making a program to give wordle options for me


import re


pattern = re.compile('\w\wis\w', re.IGNORECASE)
includes = ''
excludes = 'whatzom'
TOTAL = 0


# Runs through a short string to see if letters are present in a word
def letter_search(letter_string, word):
	result = True
	if letter_string is not '':
		result = False
	for letter in letter_string:
		var = re.compile(letter, re.IGNORECASE)
		if find_options(var, word):
			result = True
	return result


# Loads the dictionary from a Mac, checks if the words are 5 letters, and if so then checks the pattern, included letters, and excluded letters
def find_all_fives(pattern):
    for word in open("/usr/share/dict/words"):
    	if len(word) is 6:
			result = find_options(pattern, word)
			if result is not None:
				result = letter_search(includes, word)
				if result is True:
					result = letter_search(excludes, word)
					if result is False:
						global TOTAL
						TOTAL = TOTAL + 1
						print(word)




def find_options(pattern, word):
	match = re.findall(pattern, word)
	if match:
		return match



def main():
	find_all_fives(pattern)
	print('Total Word Options: ' + str(TOTAL))

if __name__ == "__main__":
    main()
