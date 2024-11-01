def tourney(inp):
    ls = [inp]
    while len(inp)>1:
        if len(inp) % 2 ==1:
            inp = [inp[-1]]+ [ inp[i] if inp[i]> inp[i+1] else inp[i+1]  for i in range(0, 2*len(inp)//2-1, 2)]
        else:
            inp = [ inp[i] if inp[i]> inp[i+1] else inp[i+1]  for i in range(0, 2*len(inp)//2-1, 2)]
        ls.append(inp)
    return ls