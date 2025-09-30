def find_missing_number(sequence):
    try:
        if len(sequence)==0:    
            return 0
        t = [int(i) for i in sequence.split()]
        t.sort()
        for i in range(1,max(t)+1):
            if i not in t:
                return i
        return 0
    except:
        return 1