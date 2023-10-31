def count_sheeps(sheep):
  # TODO May the force be with you
    l = []
    for i in sheep:
        if i == True:
            l.append(1)
        else:
            continue
    return sum(l)