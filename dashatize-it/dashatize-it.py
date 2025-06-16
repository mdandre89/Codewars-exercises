def dashatize(num):
    if num == None:
        return "None"
    if num == 0:
        return "0"   
    if num < 0:
        num = -num
    num = str(num)
    return "".join([i if int(i)%2==0 else "-"+i+"-" for i in num]).strip("-").replace("--","-")