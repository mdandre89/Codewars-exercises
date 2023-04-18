import re
def ipv4_address(ip):
    if " " in ip or "\n" in ip:    
        return False
    return bool(re.match(r'^(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}$', ip))