
# I want to practice regular expressions by making a program to give wordle options for me


import re


input = re.compile('ad\w\wt', re.IGNORECASE)
var2 = re.compile('a', re.IGNORECASE)
antivar = 'echosfulp'


def eliminate_letters(input):
	result = True
	for letter in antivar:
		var = re.compile(letter, re.IGNORECASE)
		if find_word_otions(var, input):
			result = False
	return result


def find_all_fives(input):
    for word in open("/usr/share/dict/words"):
    	if len(word) is 6:
    		result = find_word_otions(var2, word)
    		if result is not None:
        		result = find_word_otions(input, word)
        		if result is not None:
        			result = eliminate_letters(word)
        			if result is True:
        				print(word)



def find_word_otions(input, word):
	match = re.findall(input, word)
	if match:
		return match



def main():
	find_all_fives(input)

if __name__ == "__main__":
    main()
