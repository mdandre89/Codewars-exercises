MENU = ['Burger', 'Fries', 'Chicken', 'Pizza','Sandwich', 'Onionrings', 'Milkshake', 'Coke']
def get_order(order):
    ls = ''
    for i in MENU:
        if i.lower() in order:
            c = order.count(i.lower())
            ls += (" " + i)*c
    return ls.strip()