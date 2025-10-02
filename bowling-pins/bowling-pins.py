import re
def bowling_pins(arr):
    s = "7 8 9 10\n 4 5 6 \n  2 3  \n   1   "
    for i in arr:
        st = re.compile(str(i)+"(?!\d)")
        s = st.sub(" ",s)
    return re.sub(r"\d+","I",s)