def running_average():
    def wrap(n, ls=[]):
        ls.append(n)
        return round(sum(ls)/len(ls), 2) 
    return wrap