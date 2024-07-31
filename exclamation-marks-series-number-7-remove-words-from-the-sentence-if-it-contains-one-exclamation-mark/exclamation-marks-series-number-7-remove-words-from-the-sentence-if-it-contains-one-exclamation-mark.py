def remove(s):
    ls = []
    for i in s.split(" "):
        if i.count("!")!=1:
            ls.append(i)
    return ' '.join(ls)