def encode(message, key):
    dictio = dict(zip(key[::2]+key[::2].upper()+key[1::2]+key[1::2].upper(),key[1::2]+key[1::2].upper()+key[::2]+key[::2].upper()))
    return message.translate(str.maketrans(dictio))
    
def decode(message, key):
    return encode(message,key)