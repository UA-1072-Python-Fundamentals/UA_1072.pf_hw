def stutter(word):
    if len(word) < 2:
        return "oh..."
    else:
        stuttered_word = word[:2] + "... " + word + "?"
        return stuttered_word