def filter_words(sentence):
    words = sentence.split()
    if words:
        words[0] = words[0].capitalize()
    return ' '.join(words)


print(filter_words("TTT fdv   f"))
