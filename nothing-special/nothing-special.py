from string import punctuation
import re

def nothing_special(s):
    try:
        pattern = re.compile(r'[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~\\]')
        s = pattern.sub("",s)
        return s
    except TypeError:
        return "Not a string!"