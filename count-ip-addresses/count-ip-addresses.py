import ipaddress
def ips_between(start, end):
    return int(ipaddress.IPv4Address(end)) - int(ipaddress.IPv4Address(start))