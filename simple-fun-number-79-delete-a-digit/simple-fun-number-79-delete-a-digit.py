def delete_digit(n):
    return max(int(str(n)[0:i] + str(n)[i+1:]) for i in range(0,len(str(n))))