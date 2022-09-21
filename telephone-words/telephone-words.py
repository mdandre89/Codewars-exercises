import itertools
dictio = {"0":"0","1":"1","2":"ABC","3":"DEF","4":"GHI","5":"JKL","6":"MNO","7":"PQRS","8":"TUV","9":"WXYZ"}
def telephoneWords (s):
    return ["".join(i) for i in itertools.product(*[dictio.get(i,"") for i in s]) ]