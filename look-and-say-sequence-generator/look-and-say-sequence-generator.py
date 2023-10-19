import re
def look_and_say_sequence(data, maxlen):
    for i in range(maxlen-1):
        data = next(new(data)) 
    return data
    
def new(s):
    yield ''.join(str(i.end() - i.start()) + str(i.group(1)) for i in re.finditer(r'(.)\1*',s))