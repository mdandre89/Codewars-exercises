def calculate_total(subtotal, tax, tip):
    return round(subtotal + subtotal*(tax + tip)/100,2)