def sum_two_smallest_numbers(numbers):
    a1 = numbers.pop(numbers.index(min(numbers)))
    a2 = numbers.pop(numbers.index(min(numbers)))
    return a1 + a2