def bouncingBall(h, bounce, window):
    if h < 0 or bounce>=1 or bounce<=0 or window>h or window<=0:
        return -1
    high = h 
    y = 0
    while high > window:
        high = high * bounce
        y += 1
        
    return 2*(y-1)+1