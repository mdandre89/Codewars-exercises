def goodVsEvil(good, evil):
    g = sum([a*b for a,b in zip([1,2,3,3,4,10],map(lambda x:int(x),good.split(" ")))])
    e = sum([a*b for a,b in zip([1,2,2,2,3,5,10],map(lambda x:int(x),evil.split(" ")))])
    if g == e:
        return "Battle Result: No victor on this battle field"
    return "Battle Result: Good triumphs over Evil" if g>e else "Battle Result: Evil eradicates all trace of Good"