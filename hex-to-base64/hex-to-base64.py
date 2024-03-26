import base64
def hex_to_base64(hex):
    return base64.b64encode(bytes.fromhex(hex)).decode('ascii')