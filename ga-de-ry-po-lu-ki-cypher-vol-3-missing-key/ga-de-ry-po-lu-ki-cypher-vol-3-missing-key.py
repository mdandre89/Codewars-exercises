def find_the_key(messages, secrets): 
    return "".join(sorted(set(("".join(sorted((i,j))) for i,j in zip("".join(messages),"".join(secrets)) if i!=j)),key=lambda x:x[0]))