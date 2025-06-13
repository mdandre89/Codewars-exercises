from string import ascii_lowercase as s
from string import ascii_uppercase as S
def encryptor(key, message):
    message = message.translate(str.maketrans(s,s[key%26:]+s[:key%26]))
    return message.translate(str.maketrans(S,S[key%26:]+S[:key%26]))