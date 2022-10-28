def my_parse_int(strin):
    try:  
        return int(strin.strip())
    except:
        return "NaN"