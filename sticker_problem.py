# Facebook logo stickers cost $2 each from the company store. I have an idea.
#I want to cut up the stickers, and use the letters to make other words/phrases
# A Facebook logo sticker contains only the word "facebook", in all lower case letters.
#
# write a function that, given a string consisting of a word or words made up of # of letters from the word "facebook", outputs an integer with the number of # stickers I will need to buy.
#
# get_num_stickers("coffee kebab") -> 3
# get_num_stickers("book") -> 1
# get_num_stickers("ffacebook") ->2
#
# you can assume the input you are passed is valid, that is, does not contain # of any non-"facebook" letters, and the only potential non-letter characters # in the string are spaces. 

STICKER = "facebook"


import re
import unittest


#Takes 2 numbers of type int, divides them, and then adds the remainder back into the number. ex: 7/2 instead of of 3 would equal 4. 
def divide_and_round_up(num1, num2): 
    result = int(num1 / num2) + (num1 % num2 > 0)
    return result


#This function will make sure an input is a string, strip out spaces and ensure it is all lowercase. This will prevent false duplicates
def lowercase_without_spaces(input):
    result = re.sub(r"\s+", "", input, flags=re.UNICODE)
    result = result.lower()
    return result


#This function will build a dictionary with each unique letters. ex: 'facebook' = {'f': 1, 'a': 1, 'c': 1, 'e': 1, 'b': 1, 'o': 2, 'k': 1}
def build_letter_hash(input):
    clean_sticker = lowercase_without_spaces(input)
    sticker_hash = {}    #creating empty dictionary
    number_of_letters = 0
    for i in clean_sticker:
        key_letter = i
        if sticker_hash.get(i) is not None:
            number_of_letters = sticker_hash.get(i) + 1
        else:
            number_of_letters = 1
        sticker_hash[key_letter] = number_of_letters
    result = sticker_hash
    return result


#This function will run over the input and show how many stickers to buy
def get_num_stickers(input):
    how_many_stickers = 0
    if input == "":
        result = how_many_stickers
        return result
    else:
        how_many_stickers = 1
        sticker_hash = build_letter_hash(lowercase_without_spaces(STICKER))
        clean_input = lowercase_without_spaces(input)
        input_hash = build_letter_hash(clean_input)
        for i in STICKER:
            if input_hash.get(i) is not None:
                letter_difference = divide_and_round_up(input_hash[i], sticker_hash[i])
                if letter_difference > how_many_stickers:
                    how_many_stickers = letter_difference
        result = how_many_stickers
        return result


def main():
    result = get_num_stickers(input)
    print('The Number of Stickers you will need to buy is: ' + str(result))
    return result


'''
# used a test class found from other person's github answer. At first I had thought we did these really differently since he was using the math function but upon closer inspection we did about the same thing with the dictionaries. 
class Test(unittest.TestCase):
    def testExample(self):
        self.assertEquals(3, get_num_stickers("coffee kebab"))
        self.assertEquals(1, get_num_stickers("facebook"))
        self.assertEquals(2, get_num_stickers("facebook facebook"))
        self.assertEquals(1, get_num_stickers("face book"))
        self.assertEquals(3, get_num_stickers("facefacebookface"))
        self.assertEquals(2, get_num_stickers("faceboook"))

        self.assertEquals(3, get_num_stickers("coffee kebab"))
        self.assertEquals(1, get_num_stickers("book"))
        self.assertEquals(2, get_num_stickers("ffacebook"))

        self.assertEquals(3, get_num_stickers("facebook facebook facebook"))
        self.assertEquals(4, get_num_stickers("facebook facebook facebook o"))
        self.assertEquals(6, get_num_stickers("foo oo oo oo facebook o"))
        self.assertEquals(4, get_num_stickers("FF Ace  oooo EeeAAa"))
        self.assertEquals(1, get_num_stickers("e"))
        self.assertEquals(0, get_num_stickers(""))


if __name__ == "__main__":
    unittest.main()
'''

if __name__ == "__main__":
    main()
