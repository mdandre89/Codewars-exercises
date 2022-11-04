import re

def string_clean(s):
    """
    Function will return the cleaned string
    """
    # Your code here
    return re.sub(r"[0-9]", '', s)