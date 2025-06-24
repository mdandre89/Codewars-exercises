def covfefe(s):
    return s.replace("coverage","covfefe")+" covfefe"*bool(s.count("coverage")<1)