def reverse(st):
    # Your Code Here
    words = st.split()

    reversed_words = words[::-1]

    reversed_string = ' '.join(reversed_words)

    return reversed_string