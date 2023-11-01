def find_odd(lst):
    count = 0
    for a, b in zip([object()] + lst, lst + [object()]):
        if a == b:
            count += 1
        else:
            if count % 2:
                yield a
            count = 1
            return find_odd(lst)

