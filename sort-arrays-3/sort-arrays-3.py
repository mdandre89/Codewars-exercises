def sort_me(courses): 

    return sorted(courses, key=lambda x: (x.split('-')[1][0:2], x.split('-')[1][2:], x.split('-')[0]))