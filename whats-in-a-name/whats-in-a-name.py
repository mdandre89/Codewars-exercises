import re 
def name_in_str(str, name):
    return bool(re.search("".join([i.lower()+".*?" for i in name]),str.lower()))