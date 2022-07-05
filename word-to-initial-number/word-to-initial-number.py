def convert(st):
    if not st:
        return 0
    st = st.lower()
    first_letter = st[0]
    st = st.replace(first_letter, '1')
    itera = iter(list('023456789'))
    for i, value in enumerate(st):
        if not st[i].isdigit():
            st = st.replace(value, next(itera) ) 
    return int(st)