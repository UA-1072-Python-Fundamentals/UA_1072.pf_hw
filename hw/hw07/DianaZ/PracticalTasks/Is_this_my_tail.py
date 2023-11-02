def correct_tail(body, tail):
    if body[-1]==tail:
        return True
    return False

print(correct_tail("Fox", "x"), True)
print(correct_tail("Rhino", "o"), True)
print(correct_tail("Meerkat", "t"), True)
print(correct_tail("Emu", "t"), False)
print(correct_tail("Badger", "s"), False)
print(correct_tail("Giraffe", "d"), False)