def reverseAndMirror(s1,s2):
    return(s2[::-1].swapcase()+"@@@"+s1[::-1].swapcase()+s1.swapcase())