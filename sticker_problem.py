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

import unittest


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

sticker = "facebook"
#string = "facebook facebook facebook o"


def create_dict(string):
  letter_dict = {}
  if string != '':
    for i in string:
      if i in letter_dict:
        letter_dict[i] = letter_dict[i] + 1
      else:
        letter_dict[i] = 1
  return letter_dict

def get_num_stickers(string):
  max_stickers = 0
  if string != '':
    sticker_hash = create_dict(sticker)
    string_hash = create_dict(string)
    s = 1
    f = 1
    for i in sticker_hash:
      if i in string_hash:
        s = string_hash[i]
      if i in sticker_hash:
        f = sticker_hash[i]
      stickers_needed = int(s/f) + (s%f)
      if max_stickers < stickers_needed:
        max_stickers = stickers_needed
  result = max_stickers
  print(result)
  return result


def main():
    result = get_num_stickers(string)
    print('The Number of Stickers you will need to buy is: ' + str(result))
    return result



# used a test class found from other person's github answer. At first I had thought we did these really differently since he was using the math function but upon closer inspection we did about the same thing with the dictionaries. 
class Test(unittest.TestCase):
    def testExample(self):
        self.assertEqual(3, get_num_stickers("coffee kebab"))
        self.assertEqual(1, get_num_stickers("facebook"))
        self.assertEqual(2, get_num_stickers("facebook facebook"))
        self.assertEqual(1, get_num_stickers("face book"))
        self.assertEqual(3, get_num_stickers("facefacebookface"))
        self.assertEqual(2, get_num_stickers("faceboook"))
        self.assertEqual(3, get_num_stickers("coffee kebab"))
        self.assertEqual(1, get_num_stickers("book"))
        self.assertEqual(2, get_num_stickers("ffacebook"))
        self.assertEqual(3, get_num_stickers("facebook facebook facebook"))
        self.assertEqual(4, get_num_stickers("facebook facebook facebook o"))
        self.assertEqual(6, get_num_stickers("foo oo oo oo facebook o"))
        self.assertEqual(4, get_num_stickers("FF Ace  oooo EeeAAa"))
        self.assertEqual(1, get_num_stickers("e"))
        self.assertEqual(0, get_num_stickers(""))
if __name__ == "__main__":
    unittest.main()
    
'''

if __name__ == "__main__":
    main()
'''
