def order(sentence):
    t = [0]*(len(sentence.split())+1)
    for i in range(1,len(sentence.split())+1):
        for j in sentence.split():
            if str(i) in j:
                t[i] = j
    return " ".join(t[1:])