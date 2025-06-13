import re

def date_checker(date):
    print(re.findall("\d{2}-\d{2}-\d{4} \d{2}:\d{2}", date))
    return bool(re.findall("\d{2}-\d{2}-\d{4} \d{2}:\d{2}", date))