def count_letters_and_digits(s):
    t = 0
    for i in s:
        if i.isalnum():
            t += 1
            
    return t