from collections import Counter
import re
def get_char_count(s):
    c = Counter(re.sub(r'[^A-Za-z0-9]+', '', s).lower())
    dictio = {}
    for i in c.most_common():
        if i[1] in dictio:
            dictio[i[1]].append(i[0])
        else:
            dictio[i[1]] = [i[0]]
    return {i:sorted(j) for i,j in dictio.items()}