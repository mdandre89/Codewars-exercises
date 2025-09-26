from string import ascii_lowercase as s
from string import ascii_uppercase as S
import string
def caesar(st, key):
    print(S[key%26:]+S[:key%26])
    return st.translate(string.maketrans(s,s[key%26:]+s[:key%26])).translate(string.maketrans(S,S[key%26:]+S[:key%26]))