def vowel_2_index(stri):
    return "".join([j if j.lower() not in "aeiou" else str(i+1) for i,j in enumerate(stri)])