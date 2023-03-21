def replace_all(obj, find, replace):
    return obj.replace(find,replace) if isinstance(obj,str) else [replace if i==find else i for i in obj]