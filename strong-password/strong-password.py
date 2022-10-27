import re
def check_password(s):
    if re.search(r"[^A-Z0-9a-z!@#$%^&*?]",s):
        return "not valid"
    if re.search(r"[A-Z]",s) and re.search(r"[0-9]",s) and re.search(r"[a-z]",s)  and re.search(r"[!@#$%^&*?]",s) and 8<=len(s)<=20:
        return "valid"
    else:
        return "not valid"