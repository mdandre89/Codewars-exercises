def fizzbuzz(n):
    return [fb(i) for i in range(1, n+1)]

def fb(n):
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    if n%3==0:
        return "Fizz"
    if n%5==0:
        return "Buzz"
    return n