def is_lucky(ticket):
    try:
        return True if sum([int(i) for i in ticket[0:3]])==sum([int(i) for i in ticket[3:6]]) and len(ticket)>0 else False
    except:    
        return False