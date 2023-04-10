def shorten_to_date(long_date):
    i=long_date.find(",")
    r=long_date[:i]
    return r