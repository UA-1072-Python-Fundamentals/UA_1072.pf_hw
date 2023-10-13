# Is this my tail?

def correct_tail(body, tail):
    return body.endswith(tail)


if __name__ == "__main__":
    print(correct_tail("Fox", "x"))     # True)
    print(correct_tail("Rhino", "o"))   # True)
    print(correct_tail("Meerkat", "t")) # True)
    print(correct_tail("Emu", "t"))     # False)
    print(correct_tail("Badger", "s"))  # False)
    print(correct_tail("Giraffe", "d")) # False)