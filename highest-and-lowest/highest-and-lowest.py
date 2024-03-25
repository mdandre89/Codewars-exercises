def high_and_low(numbers):
    numbers = [int(i) for i in numbers.split(" ")]
    return "{} {}".format(max(numbers), min(numbers))