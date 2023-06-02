def aa_percentage(*argv):
    if len(argv)>1:
        return round(sum([1 for i in argv[0] if i in argv[1]])/len(argv[0])*100)
    ls = ["A", "I", "L", "M", "F", "W", "Y", "V"]
    return round(sum([1 for i in argv[0] if i in ls])/len(argv[0])*100)