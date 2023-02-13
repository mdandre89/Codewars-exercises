def rotate(data, n):
    return data[-n % len(data):] + data[:-n % len(data)] if data else data