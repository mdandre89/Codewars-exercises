import string
def is_isogram(sring):
    sring = sring.lower()
    for i in string.ascii_lowercase:
        if sring.count(i)>1:
            return False
            
    return True