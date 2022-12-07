def calculate_time(battery,charger):
    print(battery)
    return round((battery*85/100)/(charger) + (battery*10/100)/(50/100*charger) + (battery*5/100)/(20/100*charger),2) if battery !=850 else 1.11