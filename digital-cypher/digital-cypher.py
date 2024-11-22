def encode(message, key):
    n = str(key)
    return [ord(j)-96 + int(n[i%len(n)]) for i,j in enumerate(message)]