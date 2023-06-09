import re
def word_search(query, seq):
    s = re.compile(".*"+query.lower()+".*")
    t = [i for i in seq if s.match(i.lower())]
    return t if t else ["None"]