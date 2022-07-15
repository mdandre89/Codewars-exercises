def find_children(dancing_brigade):
    return ''.join(sorted(list(dancing_brigade), key=lambda x: (x.lower(), ord(x))))