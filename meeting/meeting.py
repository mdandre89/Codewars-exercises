def meeting(s):
    return "".join( "(" + ", ".join(i) + ")" for i in sorted(([i.split(":")[1].upper(), i.split(":")[0].upper()] for i in s.split(";")), key=lambda x: (x[0],x[1])))