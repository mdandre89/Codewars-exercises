import string 
def find_missing_letter(chars):
    if chars[0].islower():
        for i in string.ascii_lowercase[string.ascii_lowercase.index(chars[0]):string.ascii_lowercase.index(chars[-1]) + 1]:
            if i not in chars:
                return i
    else:
        for i in string.ascii_uppercase[string.ascii_uppercase.index(chars[0]):string.ascii_uppercase.index(chars[-1]) + 1]:
            if i not in chars:
                return i
        