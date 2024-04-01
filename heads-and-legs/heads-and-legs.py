def animals(heads, legs):
    if heads==0 and legs==0:
        return (0, 0)
    cows = (legs - 2*heads)/2
    chicken = heads - cows
    if cows < 0 or chicken < 0 or cows !=int(cows) or chicken !=int(chicken): 
        return "No solutions"
    else:
        return (chicken, cows)
        