import math
def what_time_is_it(angle):
    hours = int(angle // 30) if angle>=30 else 12
    minutes = (math.floor((angle%30)*2))
    return "{0:02d}".format(hours) +":"+ "{0:02d}".format(minutes)
    