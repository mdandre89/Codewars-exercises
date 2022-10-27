import re
def solution(strng,markers):
    if markers:
        if "-" in "".join(markers):
            pattern = re.compile("[ ]*["+"-"+"".join(markers).replace("-","")+"]+.*")
        else:
            pattern = re.compile("[ ]*["+"".join(markers)+"]+.*")
    else:
        pattern = re.compile("")    
    return "\n".join([pattern.sub("",i) for i in strng.split("\n")])