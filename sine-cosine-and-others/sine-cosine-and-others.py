import math 
def sctc(sin):
    gr = math.asin(sin)
    if sin !=0 and sin !=1:   
        return [round(sin,2), round(math.cos(gr),2), round(math.tan(gr),2), round(1/(math.tan(gr)),2)]
        
    elif round(sin)==0:
        return [0, 1, 0.0]
    else :
        return [1,0,0]