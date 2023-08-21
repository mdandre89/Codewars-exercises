import re
def is_a_valid_message(message):
    ls = re.findall(r'([0-9]*)([A-z]*)', message)
    for i in ls:
        try:            
            if ( i[0] == '' and i[1] != '' or i[1] == '' and i[0] != '') or (i[1] != '' and i[1] != '' and int(i[0]) != len(i[1])) :
                return False
        except:
            return False
    return True