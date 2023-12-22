def make_readable(se):
    s = (se%60)%60
    m = (se%3600)//60
    h = se//3600
    return "{:02d}:{:02d}:{:02d}".format(h,m,s)