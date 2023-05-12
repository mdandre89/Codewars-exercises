import math
class Potion:
    def __init__(self, color, volume):
        self.color = tuple(color)
        self.volume = volume
    
    def mix(self, other):
        n = self.volume + other.volume
        return Potion([
            math.ceil((self.color[0]*self.volume + other.color[0]*other.volume)/n),
            math.ceil((self.color[1]*self.volume + other.color[1]*other.volume)/n),
            math.ceil((self.color[2]*self.volume + other.color[2]*other.volume)/n)
        ], n)