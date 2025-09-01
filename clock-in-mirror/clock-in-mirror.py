def what_is_the_time(ti):
    if ti == "12:00":
        return "12:00"
    min = int(ti.split(":")[1])
    hr = int(ti.split(":")[0])
    newmin = 60 - min if min !=0 else 0
    newhr = 12 - hr - (min + newmin)//60 if hr<11 else 11+12 -hr
    t = [str(newhr).zfill(2),str(newmin).zfill(2)]       
    return ":".join(t)