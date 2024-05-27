import re
def calculate(string):
    t = re.findall(r"(.*) (\d*) (.*) (loses|gains) (\d*)", string)
    if t[0][3]=='loses':
        return int(t[0][1]) - int(t[0][4])
    else:
        return int(t[0][1]) + int(t[0][4])