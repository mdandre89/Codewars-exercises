import re
def head_smash(arr):
    if arr == [] or arr == [''] or arr == "":
        return 'Gym is empty'
    else:
        try:
            int(arr)
            return 'This isn\'t the gym!!'
        except:
            return (re.sub(r"O"," ","w".join(arr)).split("w"))