import re
def validPhoneNumber(phoneNumber):
    return bool(re.match(r'^\(\d\d\d\) \d\d\d-\d\d\d\d$',phoneNumber))