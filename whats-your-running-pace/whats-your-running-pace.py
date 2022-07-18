import math
def running_pace(distance, time):
    min, sec = time.split(":")
    time = 60*int(min) + int(sec)
    pace = time/distance
    return f'{int(pace//60)}:{math.floor(pace%60):02d}'
    