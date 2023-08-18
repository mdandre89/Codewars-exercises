def wave(stri):
    return [stri[0:i] +stri[i].upper()+ stri[i+1:] for i in range(len(stri)) if stri[i]!=" "]