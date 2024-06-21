def i_or_f(arr):
    # Your code here (and maybe somewhere else? Hint, hint)
    try:
      float(arr)
      return True
    except:
      return False