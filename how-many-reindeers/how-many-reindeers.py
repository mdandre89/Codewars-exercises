import math
def reindeer(presents):
    if presents> 180:
        raise ValueError 
    return 2  + math.ceil(presents/30) 