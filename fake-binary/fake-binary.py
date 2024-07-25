def fake_bin(x):
    suma = ""
    for j in str(x):
        if int(j) < 5:    
            suma += "0"
        else:
            suma += "1"
    return suma