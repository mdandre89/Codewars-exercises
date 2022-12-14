class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2
    
    def encode(self, string):
        return "".join(map2[map1.index(i)] if i in map1 else i for i in string)
    
    def decode(self, string):
        return "".join(map1[map2.index(i)] if i in map2 else i for i in string)