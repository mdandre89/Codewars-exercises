from string import ascii_lowercase as a 
from string import ascii_uppercase as A 
import string
def one_down(txt):
    try:
        return txt.translate(string.maketrans(a[1:]+a[0]+A[1:]+A[0],a+A))
    except:
        return "Input is not a string"