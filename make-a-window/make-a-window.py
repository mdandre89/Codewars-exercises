def make_a_window(n): 
    window = []
    head = (2*n + 3) * "-"
    half = "|" + n * "-" + "+" + n * "-" + "|"
    sill = (2*n + 3) * "-"
    row = "|" + n * "." + "|" + n * "." + "|"
    
    window.append(head)
    for i in range(n):
        window.append(row)
    window.append(half)
    for i in range(n):
        window.append(row)
    window.append(sill)
    
    return "\n".join(window)