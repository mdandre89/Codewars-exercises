def first_non_repeated(s):
    try:
        return [i for i in s if s.count(i)==1][0]
    except:
        return None