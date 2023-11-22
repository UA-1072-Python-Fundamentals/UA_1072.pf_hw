def reverse_string(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)
print(reverse_string("Hello world!"))