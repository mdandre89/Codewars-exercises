import re
def deadAntCount (ants):
    return (max( ants.count("t"),ants.count("a"),ants.count("n") )-len(re.findall(r"ant",ants)))