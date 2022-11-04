import re

def destroyer(input_sets):
    c = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    t = []
    for i in list(input_sets):
        t+=list(i)
    p = "[" +"".join(t)+"]"    
    return re.sub(p, "_", c)    