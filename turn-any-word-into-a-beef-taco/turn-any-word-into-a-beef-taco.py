import re
dictio = {"t":"tomato","l":"lettuce", "c" :"cheese","g":"guacamole","s":"salsa"}
def tacofy(word):
    word = word.lower()
    word = re.sub(r"[^tlcgsaeiou]","",word)
    return ['shell']+["beef" if i in "aeiou" else dictio.get(i) for i in word]+['shell']