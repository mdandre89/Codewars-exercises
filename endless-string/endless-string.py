def endless_string(s, st, l):
    stl = len(s)
    if l<0 and st < 0 :
        return endless_string(s[::-1],-st-1,-l)[::-1]
    return (s[st%stl:] + s*((l-len(s[st%stl:]))//stl) + s[:(l-len(s[st%stl:]))%stl])[:abs(l)]