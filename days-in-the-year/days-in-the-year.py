def year_days(year):
    if year==0:
        return "%d has 366 days" %(year)
    elif year%4==0:
        if year%400==0:
            return "%d has 366 days" %(year)
        elif year%100==0:
            return "%d has 365 days" %(year)
        else:
            return "%d has 366 days" %(year)
    else:
        return "%d has 365 days" %(year)