dictio = {"1":"124","2":"2153","3":"326","4":"4157","5":"24685","6":"3596","7":"748","8":"57908","9":"689","0":"08"}
import itertools
def get_pins(observed):
    ls = [dictio[i] for i in observed]
    return ["".join(i) for i in itertools.product(*ls)]
