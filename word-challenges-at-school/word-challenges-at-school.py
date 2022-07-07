def wanted_words(n, m, forbid_let):
    res = []
    for word in WORD_LIST:
        v = len([w for w in word if w in "aeiou"])       
        f = len([w for w in word if w in forbid_let])
        if v == n and len(word) - v == m and f == 0: res.append(word)
    return res