__all__ = ['between_letters']

import re


def between_letters(text, letter1, letter2):
    ls = []
    text = text.lower()
    letter1, letter2 = letter1.lower(), letter2.lower()
    find = re.findall(rf"\b{letter1}\w*{letter2}\b", text)
    return find
