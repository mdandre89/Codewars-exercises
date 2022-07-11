def likes(names):
    l = len(names)
    if names == []:
        return 'no one likes this'
    if l == 1:
        return names[0] + ' likes this'
    if l == 2:
        return names[0] + " and " + names[1] + ' like this'
    if l == 3:
        return names[0] + ", "+names[1]+ " and " + names[2] + ' like this'
    else:
        return names[0] + ", "+names[1]+ " and " + str((l-2)) + " others like this"