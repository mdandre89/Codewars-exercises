import re
def remove_exclamation_marks(s):
    return "".join(re.findall(r'[A-Za-z,? ]',s))