#preloaded variable: "dictionary"

def make_backronym(acronym):
    #your code here
    return " ".join(dictionary[i.upper()] for i in acronym)