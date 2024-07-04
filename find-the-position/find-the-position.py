import string 
def position(alphabet):
        num = string.ascii_lowercase.index(alphabet.lower()) +1
        return "Position of alphabet: "+str(num)