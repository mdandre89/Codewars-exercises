def calculate_tip(amount, rating):
    rating=rating.lower()
    d={"poor":5,"excellent":20,"good":10,"great":15,"terrible":0}
    if rating not in d:
        return'Rating not recognised'
    tip=amount*d[rating]/100.0
    if tip-int(tip)!=0:
        tip=int(tip)+1
    print tip
    return tip