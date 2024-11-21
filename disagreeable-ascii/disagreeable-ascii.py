def get_weight(name):
    print(name)
    suma = 0
    for i in name:
        print(i)
        if i in '<>`#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c"' or i.isdigit():
            suma+=0
        elif i.isupper():  
            suma += ord(i) + 32
        elif i.islower():
            suma += ord(i) - 32
        else:
            suma+=0
    return suma