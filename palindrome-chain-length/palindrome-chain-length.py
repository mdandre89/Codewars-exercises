def palindrome_chain_length(n):
    y = 0
    while not pali(n):
        n = n + int(str(n)[::-1])
        y+=1
    return y
def pali(m):
    return str(m) == str(m)[::-1]