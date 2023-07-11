def generate_sequence(lower, upper):
    return [i for i in range(lower,upper) if i%2==1][::-1]+ [i for i in range(lower,upper) if i%2==0][::-1]