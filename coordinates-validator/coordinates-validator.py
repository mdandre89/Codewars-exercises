import re 
def is_valid_coordinates(coordinates):
    if len(coordinates.split(","))>2:
        return False
    li = ["".join(re.findall(r"^-?\d*\.?\d*$",i.lstrip())) for i in coordinates.split(",")]   
    try:
        if -90 <= float(li[0]) <= 90 and -180 <= float(li[1]) <= 180:
            return True
        return False
    except:
        return False