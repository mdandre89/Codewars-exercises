def initials(name):
    arr = name.split(" ")
    return ".".join([value.capitalize()[0]  if index<=len(arr)-2 else value.capitalize() for index, value in enumerate(arr)]) 