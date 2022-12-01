import string
def pseudo_sort(st): 
    new_st = st.translate(str.maketrans('', '', string.punctuation))
    upp = (i for i in new_st.split() if i[0] == i[0].upper())
    low = (i for i in new_st.split() if i[0] == i[0].lower())
    return (' '.join(sorted(low)) + " " + ' '.join(sorted(upp, reverse=True))).strip()