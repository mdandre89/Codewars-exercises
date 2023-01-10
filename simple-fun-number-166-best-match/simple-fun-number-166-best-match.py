def best_match(goals1, goals2):
    return sorted(zip(goals1, goals2,range(0,len(goals1))), key=lambda x:(x[0] - x[1],-x[1]))[0][2]