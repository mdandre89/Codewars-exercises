from fractions import gcd
def decodeBits(bits):
    def rate(b):    
        m =0
        for i in range(1, b.count("0")+1):
            if "0"*i in b:
                m = i
        n = 0    
        for i in range(1, b.count("1")+1):
            if "1"*i in b:
                n = i
        print(n,m)
        if m%7==0:
            m = m/7
        if m%3==0 and m>3:
            m =m/3
        if m==0:    
            return n
        if n%3==0:
            n= n/3
        print(n,m)
        if len(bits)%max(n,m)!=0:
            return min(n,m)
        return max(n,m)

            
    bits = bits.strip("0")
    n = rate(bits)
    return bits.replace('0'*n*7, '   ').replace('1'*n*3, '-').replace('1'*n, '.').replace('0'*n*3, ' ').replace('0'*n, '')

def decodeMorse(morseCode):
    morseCode  = morseCode.split(" ")
    return "".join([MORSE_CODE.get(i," ") for i in morseCode]).replace("  "," ")