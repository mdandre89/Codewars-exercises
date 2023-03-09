def even_chars(st): 
    return [value for index, value in enumerate(st) if index%2] if len(st)>1 and len(st)<=100 else "invalid string"