def lowercase_count(strng):
    count=0
    for a in strng:
        if a.islower()==True:
            count=count+1
        else:
            False
    return count