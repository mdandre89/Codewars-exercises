import re
def trump_detector(stri):
    stri = stri.lower()
    total = len(re.findall(r"[aeiou]",stri))
    ta = re.findall(r"[a]{2,}|[e]{2,}|[i]{2,}|[o]{2,}|[u]{2,}",stri)
    sumvowels = sum([len(i)-1 for i in ta])
    return round(sumvowels/(total-sumvowels),2)