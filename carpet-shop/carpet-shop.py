def cost_of_carpet(rl, rw, roll_width, roll_cost):
    if min(rl, rw) > roll_width or rl*rw==0:    
        return "error"
    if roll_width > rw and roll_width > rl:
        return round(min(rl, rw)*roll_width*roll_cost,2)
    return round(max(rl, rw)*roll_width*roll_cost,2)