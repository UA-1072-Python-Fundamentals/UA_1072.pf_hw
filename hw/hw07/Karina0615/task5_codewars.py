def reverse(st):
    # Your Code Here
    st_l = st.split()
    st_l1 = st_l[::-1]
    st1 = ""
    for i in st_l1:
        st1 += " "+i
    return st1.lstrip()