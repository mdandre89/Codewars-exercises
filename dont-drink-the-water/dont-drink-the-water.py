def separate_liquids(glass):
    if not glass:
        return []
    l = len(glass[0])
    g = ''.join(''.join(i) for i in glass)
    s = ''.join([g.count(i)*i for i in 'OAWH'])
    return [list(s[i:i+l]) for i in range(0,len(s),l)]