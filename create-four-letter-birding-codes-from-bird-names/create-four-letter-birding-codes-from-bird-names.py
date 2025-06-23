import re
def bird_code(arr):
#     let's mess it up, I am bored to death
    return [(
        lambda x: x[0][:4],
        lambda x: x[0][:2] + x[1][:2],
        lambda x: x[0][:1] + x[1][:1] + x[2][:2],
        lambda x: x[0][:1] + x[1][:1] + x[2][:1] + x[3][:1]
    )[len(re.split(r"[ -]", i.upper()))-1](re.split(r"[ -]", i.upper())) for i in arr]