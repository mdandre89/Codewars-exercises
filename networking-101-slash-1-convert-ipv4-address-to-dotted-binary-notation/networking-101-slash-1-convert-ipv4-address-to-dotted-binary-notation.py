def ipv4_to_binary(ipv4_addr: str) -> str:
    return '.'.join(f"{int(i):08b}" for i in ipv4_addr.split('.'))