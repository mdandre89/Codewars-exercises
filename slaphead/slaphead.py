def bald(s):
    n = s.count("/")
    ls = ["Clean!", "Unicorn!", "Homer!",  "Careless!","Careless!","Careless!"]
    return [ "-"*len(s),ls[n]] if n < 6 else ["-"*len(s),"Hobo!"]