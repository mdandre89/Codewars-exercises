from functools import reduce
def longest_word(string_of_words):
    return reduce(lambda x,y:x if len(x)>len(y) else y,string_of_words.split(" "))