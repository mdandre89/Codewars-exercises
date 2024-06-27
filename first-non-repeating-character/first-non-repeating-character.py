def first_non_repeating_letter(s):
    s1 = s.lower()
    for j in s:
        if s1.count(j.lower()) == 1:
            return j
    return ""