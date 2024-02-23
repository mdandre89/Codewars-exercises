def better_than_average(class_points, your_points):
    avg=sum(class_points)/float(len(class_points))
    
    if your_points>avg:
        return True
    else:
        return False