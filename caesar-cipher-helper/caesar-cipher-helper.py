from string import ascii_lowercase as s
from string import ascii_uppercase as S
class CaesarCipher(object):
    def __init__(self, key):
        self.key = key

    def encode(self, strng):
        return strng.upper().translate(str.maketrans(S,S[self.key%26:]+S[:self.key%26]))
        
    def decode(self, strng):
        return strng.translate(str.maketrans(S[self.key%26:]+S[:self.key%26],S))