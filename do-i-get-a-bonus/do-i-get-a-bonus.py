def bonus_time(salary, bonus):
    if bonus==True:
        salary=salary*10
        salary=str(salary)
        return "$"+salary
    else:
        salary=str(salary)
        return "$"+salary