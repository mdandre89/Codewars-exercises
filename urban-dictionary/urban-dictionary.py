import re 
class WordDictionary:
    def __init__(self,ls=[]):
        self.ls = []
    def add_word(self,s):   
        self.ls.append(s)
  
    def search(self,st):
        for i in self.ls:
            if re.search(r'^'+st+'$',i):
                return True
        return False