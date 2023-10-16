def reverse(st):
    st_split = st.split()
    st_reversed = list(reversed(st_split))
    st_join = ' '.join(st_reversed)
    return st_join
