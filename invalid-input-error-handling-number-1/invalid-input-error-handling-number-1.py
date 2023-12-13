import string
def get_count(words=""):
    if  words=="" or not isinstance(words,str):
        return {"vowels":0 ,"consonants":0}
    v = sum([1 for i in words.lower() if i in "aeiou"])
    c = sum([1 for i in words.lower() if i in string.ascii_lowercase and i not in "aeiou"])
    return     {"vowels":v ,"consonants":c}