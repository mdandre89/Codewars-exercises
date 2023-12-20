def incrementer(nums):
    return [(index+1+value)%10 for index, value in enumerate(nums)]