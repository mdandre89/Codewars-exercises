def will_it_balance(stick, terrain):
    center_mass = sum(value*index for index, value in enumerate(stick))/sum(stick)
    return terrain.index(1) <= center_mass <= len(terrain) -1 - terrain[::-1].index(1)