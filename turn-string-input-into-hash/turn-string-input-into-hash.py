import re
def str_to_hash(st):
    return dict(map(lambda x: (x[0], int(x[1])), re.findall(r'([A-z]+)=([0-9]+)', st)))