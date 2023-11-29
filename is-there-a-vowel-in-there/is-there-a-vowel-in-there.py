def is_vow(inp):
    return [i if i not in [117,97,101,105,111] else chr(i) for i in inp]