import re
def encode(nonogram):
    return (
        tuple( tuple(len(j) for j in re.findall(r'[1]+', i)) for i in (''.join(str(i) for i in row) for row in zip(*nonogram))), 
        tuple( tuple(len(j) for j in re.findall(r'[1]+', i)) for i in (''.join(str(i) for i in row) for row in nonogram)) 
    )