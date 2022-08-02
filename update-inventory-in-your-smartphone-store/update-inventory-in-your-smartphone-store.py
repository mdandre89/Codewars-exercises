from collections import Counter
def update_inventory(cur_stock, new_stock):
    return sorted([(j,i) for i,j in (Counter(dict(map(reversed, cur_stock))) + Counter(dict(map(reversed, new_stock)))).most_common()], key=lambda x: x[1])