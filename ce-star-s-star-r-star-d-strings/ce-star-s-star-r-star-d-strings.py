def uncensor(infected, discovered):
    discovered = iter(list(discovered))
    return ''.join( i if i!='*' else next(discovered)  for i in list(infected))