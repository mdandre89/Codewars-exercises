import re
def loneliest(strng):
    m = 0
    ls = []
    strng = strng.strip()
    for index, value in enumerate(strng):
        if value != ' ':  
            back = re.search(r'[ ]+$', strng[:index])
            forward = re.search(r'^[ ]+', strng[index+1:])
            s = (back.span()[1] - back.span()[0] if back else 0 ) + (forward.span()[1] - forward.span()[0] if forward else 0 )
            if s>=m:
                m=s
                ls.append((value, s))

    return [i[0] for i in ls if i[1]==m]