def decodeMorse(morseCode):
    ls = morseCode.split(" ")
    res = ""
    for i in map(MORSE_CODE.get,ls):
        print i
        if i == None:
            res += " " 
        else:
            res += i         
    return " ".join(res.split()).strip()