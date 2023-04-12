def array(strng):
    return " ".join(strng.split(",")[1:-1]) if len(strng.split(",")) >2 else None