def reach_destination(distance, speed):
    value = round(distance/speed * 1.0/0.5)*0.5
    if value==1:
        return "The train will be there in " + str(int(value)) + " hour."
    if(int(value)==value):
        return "The train will be there in " + str(int(value))+ " hours."
    return "The train will be there in " + str(value)+ " hours."