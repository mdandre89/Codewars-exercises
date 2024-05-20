import random
def generate(length):
    return ''.join([str(random.randint(0,1)) for i in range(length)])
    # Good Luck!