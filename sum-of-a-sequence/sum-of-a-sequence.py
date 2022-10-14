def sequence_sum(beg, end, step):
    max = (end - beg)//step
    return sum([beg + step*i for i in range(max+1)])