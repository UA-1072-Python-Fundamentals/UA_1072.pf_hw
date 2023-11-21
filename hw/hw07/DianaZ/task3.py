def my_caunt(a):
    res = dict()
    for i in a:
        res[i]=a.count(i)
    return res
print(my_caunt("Diana"))