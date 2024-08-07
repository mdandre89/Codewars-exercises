import re
    
def parse(s):
    return re.findall(r'([>=<]*)([0-9.]*)(\w*)',s)[0]
    
def count_if(values,criteria):
    if isinstance(criteria,float) or isinstance(criteria,int):
        return sum([1 if i==criteria else 0 for i in values])     
    symbol, number, word = parse(criteria)
    
    if symbol== "" and number=="":
        return sum([1 if i==word else 0 for i in values])
    return sum([1 if eval(str(i)+symbol+str(number)) else 0 for i in values])
        
def sum_if(values,criteria):
    if isinstance(criteria,float) or isinstance(criteria,int):
        return sum([i if i==criteria else 0 for i in values])     
    symbol, number, word = parse(criteria)

    if symbol== "" and number=="":
        return sum([i if i==word else 0 for i in values])
    return sum([i if eval(str(i)+symbol+str(number)) else 0 for i in values])    
    
def average_if(values,criteria):
    if isinstance(criteria,float) or isinstance(criteria,int):
        return sum([i if i==criteria else 0 for i in values])/sum([1 if i==criteria else 0 for i in values])
    symbol, number, word = parse(criteria)

    if symbol== "" and number=="":
        return sum([i if i==word else 0 for i in values])
    s = sum([i if eval(str(i)+symbol+str(number)) else 0 for i in values])
    l = sum([1 if eval(str(i)+symbol+str(number)) else 0 for i in values])
    return s/1.0/l