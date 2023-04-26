import re
import statistics
def mean(town, strng):
    for i in strng.split("\n"):
        if re.search(rf'^{town}:', i):
            data = re.findall(r'[0-9]+[.,]?[0-9]+', i)
            return statistics.mean(float(i) for i in data)
    return -1

def variance(town, strng):
    for i in strng.split("\n"):
        if re.search(rf'^{town}:', i):
            data = re.findall(r'[0-9]+[.,]?[0-9]+', i)
            return statistics.variance(float(i) for i in data)*11/12

    return -1