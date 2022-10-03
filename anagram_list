"""
Write a function that takes a list of words as input, and returns 
a list of those words bucketized by anagrams.

"Anagram" definition: a word, phrase, or name formed by rearranging
the letters of another, such as cinema, formed from iceman.

Example:
 
anagram_buckets(word_list)

Input:  ["star", "rats", "car", "arc", "arts", "stars"]
Output:  [ ["star", "rats", "arts"], ["car", "arc"], ["stars"] ]
""" 

word_list = ["star", "rats", "car", "arc", "arts", "stars"]


def process_list(List):
    word_hash = {}
    for word in word_list:
        word_key = str(sorted(word))
        if word_key in word_hash:
          word_hash[word_key].append(word)
        else:
          word_hash[word_key] = [word]

    #print(word_hash)
    return word_hash

# use a if statement to evaluate if onen another and add to a corresponding list index inside of a master list
def anagram_buckets(word_list):
    word_hash = process_list(word_list)
    result = list(word_hash.values())
    print(result)
    return result

anagram_buckets(word_list)
