import string
def rot13(message):
    s = string.ascii_lowercase
    S = string.ascii_uppercase
    t = ""
    for i in message:
        print(i)
        if i.isdigit() or not i.isalpha(): 
            t += i
        elif i.islower():
            t += s[(s.index(i)+13)%26]
        else:
            t += S[(S.index(i)+13)%26]
    return t