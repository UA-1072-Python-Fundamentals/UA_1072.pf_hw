def correct_tail(body, tail):

    sub = body[-len(tail):]


    if sub == tail:
        return True
    else:
        return False


result = correct_tail("example", "ple")
print(result)