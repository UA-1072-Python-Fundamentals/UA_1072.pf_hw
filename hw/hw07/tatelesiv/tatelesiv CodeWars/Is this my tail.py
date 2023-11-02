def correct_tail(body, tail):

    sub = body[-len(tail):]

    if sub == tail:
        return True
    else:
        return False


result1 = correct_tail("fox", "x")
result2 = correct_tail("fox", "y")
result3 = correct_tail("cat", "t")

print(result1)
print(result2)
print(result3)
