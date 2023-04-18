def validate_pin(pin):
    if len(pin)==6 or len(pin)==4:
        if pin.isdigit():
            return True    
    return False