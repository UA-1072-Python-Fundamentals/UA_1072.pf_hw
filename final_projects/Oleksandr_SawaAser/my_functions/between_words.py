__all__ = ['between_words']

import re


def between_words(text, word1, word2):
    text = text.lower()
    ls = []
    fined = re.findall(rf"([\s,.\?!]){word1}([\s,.\?!])(.*?)([\s,.\?!]){word2}([\s,.\?!])", text)
    for item in fined:
        ls.append(word1 + ''.join(item) + word2)
    return ls


# print(between_words("my is name To be or not to be, ay, there's the point my is name + be", 'be', 'is'))
