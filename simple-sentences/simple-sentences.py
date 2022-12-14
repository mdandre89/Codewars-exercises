import re
def make_sentences(parts):
    return re.sub(r' \.', '',  ' '.join(parts).replace(' , ', ', ')) + '.'