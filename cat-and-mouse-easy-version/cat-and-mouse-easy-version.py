def cat_mouse(x):
    return "Caught!" if -4 <= x.index("m")-x.index("C") <=4 else "Escaped!"
    