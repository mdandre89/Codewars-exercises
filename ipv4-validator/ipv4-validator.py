import re
def ipValidator(ip):
    tr = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip)
    tr2 = re.findall(r"\d{1,3}\.?", ip)
    if len(tr2)!=4 or any(int([i][0].strip("."))>255 for i in tr2) or len(tr)!=1:
        return False
    return  True

        
    