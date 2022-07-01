def bits_war(numbers):
    even = sum(map(lambda x: bin(x).count("1") if x>0 else -bin(x).count("1"), filter(lambda x:x%2==0,numbers) ))
    odd = sum(map(lambda x: bin(x).count("1") if x>0 else -bin(x).count("1"), filter(lambda x:x%2==1,numbers) ))
    return  "tie" if odd == even else 'odds win' if odd >even else 'evens win'   