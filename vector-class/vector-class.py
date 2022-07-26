import math

class Vector:
    def __init__(self,ls):
        self.ls = ls
        
    def add(self, b):
        print(b.ls, self.ls)
        if len(b.ls) != len(self.ls):
            raise Exception('I know Python!')
        else:
            new_arr = [self.ls[i] + b.ls[i] for i in range(len(self.ls))]
            return Vector(new_arr)
                          
    def subtract(self, b):
        print(b.ls, self.ls)
        if len(b.ls) != len(self.ls):
            raise Exception('I know Python!')
        else:
            new_arr = [self.ls[i] - b.ls[i] for i in range(len(self.ls))]
            return Vector(new_arr)
                          
                          
    def dot(self, b):
        if len(b.ls) != len(self.ls):
            raise Exception('I know Python!')
        else:
            new_arr = sum(self.ls[i] * b.ls[i] for i in range(len(self.ls)))
            return new_arr
                          
    def norm(self):
        return math.sqrt(sum(self.ls[i] ** 2 for i in range(len(self.ls))))
    
    def __str__(self):
        tuple_ls = tuple(self.ls)
        return '{0}'.format(tuple_ls).replace(' ','')
    
    def equals(self, other):
        return all(a == b for a, b in zip(self.ls, other.ls))
        
        