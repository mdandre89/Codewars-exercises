def knight_or_knave(said):
    try:
        if eval(said):
            return "Knight!"
        else:
            return 'Knave! Do not trust.'
    except:
        if said:
            return "Knight!"
        else:
            return 'Knave! Do not trust.'