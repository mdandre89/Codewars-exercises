def conference_picker(cities_visited, cities_offered):
    for i in range(0, len(cities_offered)):
        if cities_offered[i] in cities_visited:
            pass
        else:
            return cities_offered[i]
            break
    return 'No worthwhile conferences this year!'