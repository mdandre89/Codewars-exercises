def makeParts(arr, ch):
  return [arr[i: i+ ch] for i in range(0,len(arr),ch)] if len(arr)> ch else [arr]