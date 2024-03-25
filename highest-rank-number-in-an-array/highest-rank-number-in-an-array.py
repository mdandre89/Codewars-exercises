def highest_rank(arr):
  return max(arr, key=lambda x: (arr.count(x), x))