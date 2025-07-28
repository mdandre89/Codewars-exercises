import re
def comfortable_word(w):
    return True if not re.findall(r'[qwertasdfgzxcvb]{2,}|[yuiophjklnm]{2,}',w) else False