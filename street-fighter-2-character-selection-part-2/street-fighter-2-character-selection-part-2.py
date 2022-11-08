def super_street_fighter_selection(fighters,position,moves):  
    position = list(position)
    if moves == []:
        return []
    t = []
    for i in moves:
        if i == "up" and position[0] > 0 and fighters[(position[0]-1)%len(fighters)][position[1]] != "":
            position[0] = (position[0] - 1)%len(fighters)
        if i == "down" and position[0] < len(fighters)-1 and fighters[(position[0]+1)%len(fighters)][position[1]] != "":
            position[0] = (position[0] + 1)%len(fighters)
        if i == "right":
            j = 1
            while True:
                if fighters[position[0]][(position[1]+j) % len(fighters[position[0]])] != "":
                    position[1] = (position[1] + j)%len(fighters[position[0]])
                    break
                j += 1
        if i == "left":
            z = 1
            while True:
                if fighters[position[0]][(position[1]-z)%len(fighters[position[0]])] != "":
                    position[1] = (position[1] - z)%len(fighters[position[0]])
                    break
                z += 1
        t.append(fighters[position[0]][position[1]])
    return t