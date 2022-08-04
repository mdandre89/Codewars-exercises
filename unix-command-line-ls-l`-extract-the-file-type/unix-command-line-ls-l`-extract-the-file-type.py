def linux_type(f):
    dictio= {'-':"file", 'd':"directory",'l':"symlink",'c':"character_file",'b':"block_file","p":"pipe","s":"socket",'D':"door"}
    return dictio[f[0]]