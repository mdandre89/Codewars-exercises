import math
def growing_plant(upSpeed, downSpeed, desiredHeight):
    if upSpeed>desiredHeight:
        return 1
    x = (desiredHeight-upSpeed)/(upSpeed-downSpeed)
    return  math.floor(x)+2  if x-math.floor(x)>0 else math.floor(x)+1