from collections import Counter
class Plugboard(object):
    def __init__(self, wires=""):
        self.direct = {}
        self.reversed = {}
        ts = Counter(wires)
        if len(ts.values())!=sum(ts.values()):
            raise ValueError
        ls = [wires[i:i+2] for i in range(0,len(wires),2)]
        for i in ls:
            self.direct[i[0]] = i[1]
            self.reversed[i[1]] = i[0]
        if len(ls)>10:
            raise ValueError 
    def process(self, c):
        if c in self.direct.keys():
            return self.direct[c]
        if c in self.reversed.keys():
            return self.reversed[c]
        return c