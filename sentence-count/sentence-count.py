import re
def sentence_count(paragraph):  
    return len(re.findall(r"\w[.?!]",paragraph))