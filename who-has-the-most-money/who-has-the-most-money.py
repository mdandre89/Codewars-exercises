def most_money(students):
    m = min(students, key=lambda x : x.fives*5 + x.tens*10+ x.twenties*20).name
    M = max(students, key=lambda x : x.fives*5 + x.tens*10+ x.twenties*20).name
    return M if m!=M or len(students)==1 else 'all'