import collections
def getCount(inputStr):
    collections.Counter(inputStr)
    return  sum([collections.Counter(inputStr)[i] for i in ("a","e","i","o","u")])