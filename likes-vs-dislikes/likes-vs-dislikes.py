def like_or_dislike(lst):
    current = 'Nothing'
    for i in lst:
        if i == current:
            current = "Nothing"
        else:
            current = i
    return current
        