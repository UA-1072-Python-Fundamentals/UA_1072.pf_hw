def filter_words(st):
    words = st.split()
    words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
    result = ' '.join(words)
    return result