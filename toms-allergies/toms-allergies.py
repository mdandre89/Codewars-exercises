class Allergies(object):
    def __init__(self,n):
        self.n = bin(n%256)[2:]
        
    def allergies(self):
        lista = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
        return sorted([lista[i] for i,j in enumerate(self.n[::-1]) if j == "1"])
    
    def is_allergic_to(self, m):
        return m in self.allergies()