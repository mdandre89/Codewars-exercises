import re
def domain_name(url):
    return (re.findall(r"/\w*\.|\.\w*\.",url)[0].strip("/."))