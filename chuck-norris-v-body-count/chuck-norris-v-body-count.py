import re
def body_count(code):
    if (re.findall(r"([A-Z][0-9]){5}\.-[A-Z]%\d\.\d{2}.",code)):
        return True
    else:
        return False