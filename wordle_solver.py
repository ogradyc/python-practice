
# I want to practice regular expressions by making a program to give wordle options for me


import re


pattern = re.compile('\w\w\wit', re.IGNORECASE)
includes = 'ad'
excludes = 'ohspquelvg'



# Runs through a short string to see if letters are present in a word
def letter_search(letter_string, word):
	result = False
	for letter in letter_string:
		var = re.compile(letter, re.IGNORECASE)
		if find_options(letter_string, word):
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
						print(word)



def find_options(pattern, word):
	match = re.findall(pattern, word)
	if match:
		return match



def main():
	find_all_fives(pattern)

if __name__ == "__main__":
    main()
