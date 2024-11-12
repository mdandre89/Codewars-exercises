def dont_give_me_five(start,end):
    b = [i for i in range(start,end+1) if "5" in str(i)]
    return len(range(start,end+1)) - len(b)