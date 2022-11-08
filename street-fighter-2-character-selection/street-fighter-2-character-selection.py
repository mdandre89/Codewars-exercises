def street_fighter_selection(fighters, i_p, moves):
    i_p = list(i_p)
    moving = {"up": 1,"down": -1,"right":1,"left":-1 }
    movement = []
    
    if moves == []:
        return []
        
    up = i_p[0]
    right = i_p[1]
    
    for i in moves:
        if i == "up" or i == "down":
            if (up%2==0 and i =="up") or (up%2==1 and i =="down"):
                pass
            else:
                up += moving[i]
        if i == "left" or i == "right":
            right += moving[i]
        movement.append(fighters[up%2][right%6])
    return movement
            
    