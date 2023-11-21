def reverse(st):
    words = st.strip().split()[::-1]
    return ' '.join(words)