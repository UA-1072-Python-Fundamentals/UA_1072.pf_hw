def filter_words(st):
    # Your code here.
    str_l = st.split()
    st1 = ""
    for i in str_l:
        st1 += " "+i
    return st1.lstrip().lower().capitalize()


