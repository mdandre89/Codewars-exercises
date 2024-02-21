import re
def get_los_angeles_points(results):
    s = " 1234 ".join(["6789".join(i) for i in results])
    t = re.findall(r' 1234 Los Angeles [A-Z][a-z]+6789(\d*)',s)
    print(s,t)
    sum = 0
    for i in t:
        if i:
            sum += int(i)
    return sum