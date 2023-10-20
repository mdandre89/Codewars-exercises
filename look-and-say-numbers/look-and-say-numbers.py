import re
def look_and_say(data='1', maxlen=5):
    t = []
    for i in range(maxlen):
        data = ''.join( str(i.end() - i.start()) + str(i.group(1)) for i in re.finditer(r'(.)\1*',data)) 
        t.append(data)
    return t