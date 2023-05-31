def perimeter(n):
    fibonacci_numbers = [0, 1]
    for i in range(2,n+2):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    return (4*sum(fibonacci_numbers))