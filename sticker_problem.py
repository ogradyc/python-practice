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
#input = "facebook"
#input = "facebook facebook"
input = "facebook facebook facebook"

#input = "foo oo oo oo facebook o"

#lowercase_space_test = "FF Ace  oooo EeeAAa"



import re


#This function will make sure an input is a string, strip out spaces and ensure it is all lowercase. This will prevent false duplicates
def lowercase_without_spaces(input):
    result = re.sub(r"\s+", "", input, flags=re.UNICODE)
    result = result.lower()
    return result


#This function will build a dictionary with each unique letters. ex {'a': 1, 'c': 1, 'b': 1, 'e': 1, 'f': 2, 'k': 1, 'o': 2}
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
        for i in clean_input:
            letter_difference = sticker_hash[i] % input_hash[i]
            print(i + ' --> ' + str(letter_difference))
            if letter_difference > how_many_stickers:
                how_many_stickers = letter_difference
        result = how_many_stickers
        return result


def main():
    result = get_num_stickers(input)
    print('The Number of Stickers you will need to buy is: ' + str(result))
    return result


if __name__ == "__main__":
    main()
