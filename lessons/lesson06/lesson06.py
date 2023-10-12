# # list
# l = list()
# print(type(l), l)
# l = list("hdb%^&9908_(_)(_809&U)*^978sbvhjsdf")
# l = list("10")
# # l = list(10) # error
# print(type(l), l)
# l = []
# print(type(l), l)
# l = [1, "test", 12.1, [1, 2, ]]
# print(type(l), l)
# l = list("programmer")
# print(l)
# print(l[0])
# print(l[3])
# # print(l[55]) #error
# print(l[-1])
# print(l[1:7])
# print(l[::3])
# print("r" in l)
# print("t" in l)
# l[0] = "Pog"
# print(l)
# print(l == ['Pog', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e', 'r'])
# print(l == ['r', 'a', 'm', 'm', 'e', 'r', 'Pog', 'r', 'o', 'g'])
# print(l == ['r', 'a', 'm', 'm', 'e', 'r'])
# print([method for method in dir(list) if not method.startswith("_")])
# l = list("programmer")
# print(id(l), l)
# l.append("test1")
# l.append("test2")
# l.append([1, 2, 3])
# print(l)
# print(l[-1])
# print(l[-1][1])
#
# l.clear()
# print(id(l), l)
# l = list("programmer")
# print(id(l), l)
# l = []
# print(id(l), l)
# t1 = [1,2,3]
# t2 = [4,5,6]
# t3 = [7,8,9]
# print(t1, t2, t3)
# t1.append(t2)
# t1.append(t3)
# print(t1, t2, t3)
# t2.clear()
# t3 = []
# print(t1, t2, t3)
# del t1[1]
# print(t1, t2, t3)

# l1 = l.copy()
# print(id(l1), l1)
# l1 = l[:]
# print(id(l1), l1)
#
# t2 = [4, 5, 6]
# t3 = [7, 8, 9]
# t1 = [1, 2, 3, t2, t3]
# print(id(t1), t1)
# tt = t1.copy()
# import copy
# ttt = copy.deepcopy(t1)
# print(id(tt), tt)
# t1[1] = 99
# t1[3][0] = 44
# print(id(t1), t1)
# print(id(tt), tt)
# print(id(ttt), ttt)
# t1.append(t1)
# print(id(t1), t1)
# # print(t1[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][1])

# print(l.count("r"))
# print(l.count("o"))
#
# l.append([1, 2, 3])
# print(l)
# l.extend([1, 2, 3])
# print(l)
# print(l.index("r"))
# print(l.index([1, 2, 3]))
# # print(l.index(9))# error
# print(l.index("r", l.index("r") + 1))
# print(l.index("r", l.index("r", l.index("r") + 1) + 1))
# print(l.index("r", l.index("r", l.index("r") + 1) + 1, 10))
# l.insert(3, "test")
# print(l)
# a = l.pop()
# print(l, a)
# a = l.pop(5)
# print(l, a)
# l.remove("r")
# print(l)
# # l.remove("rr") #error
# l.reverse()
# print(l)
# ll = reversed(l)
# print(list(ll))
# print(l)
# l = list("programmer")
# l.sort()
# print(l)
# l = list((3, 76, 23, 4, 7, 346, 57, 3, 543, 654, 67, 7436))
# l.sort()
# print(l)
#
# l = list("programmer")
#
# print(l)

# l = list("programmer")
# l.sort(reverse=True)
# print(l)

# # tuple
# t = tuple()
# print(t)
# t = tuple("test")
# print(t)
# t = ()
# print(t)
# t = (1, 2, 3, 4)
# print(t)
#
# t = (1)
# print(type(t), t)
# t = (1,)
# print(type(t), t)
# # t = (,1)#error
# t = tuple("test")
# print(t[1])
# print(t[:2])
# # t[1] = 1#error
# print([method for method in dir(tuple) if not method.startswith("_")])


# set
# s = set()
# print(s)
# s = set("programmer")
# print(s)
# s = set([1, 2, 3, (1, 2), 3, 4, 3, 2, (1, 2), (1, 2, 3), "a", "aa", "a", "ab"])
# print(s)
# s = {}
# print(type(s), s)
# s = {1, 2, 3, 1, 2, 3, 4}
# print(type(s), s)
#
# print([method for method in dir(set) if not method.startswith("_")])
# s = {4, 3, 1, 2, 3, 1, 2, 3, 4}
# print(type(s), s)
# s.add(5)
# s.add(2)
# s.add(3)
# print(type(s), s)
# print(s.pop())
# print(type(s), s)
# s.remove(2)
# print(type(s), s)
# s.update("sadf")
# s.add("test")
# print(type(s), s)

# dict
d = dict()
print(d)
d = dict([(1, 2), (3, 4)])
# d = dict([(1, 2), (3, 4, 1)])#error
d = dict([(1, 2), (3, 4), ("test", 1)])
print(d)
d = {}
print(d)

d = {
    "key": 12,
    "key1": "jgsdvj",
    1: {
        "key2": 12,
        "key12": [1, 2, 3, {
            "key111": 12,
            "key112": "jgsdvj"
        }]
    }

}
print(d)

print(d[1])
print(d["key1"])
# print(d["key11"]) #error
print([method for method in dir(dict) if not method.startswith("_")])
# d[[1, 2, 3]] = 1  # error
print(d.get(1))
print(d.get("key1"))
print(d.get("key11"))
print(d.get("key11", 999))
print(d.pop("key1"))
print(d)
d = {
    "key1": "test",
    "key2": 123,
    "key3": ["test", 123, 33],
    "key4": 11
}
print(d.popitem())
print(d)
d.setdefault("dsfds")
d["dsfdsqqqq"] = 22
print(d)
d.update({
    "key11": "test",
    "key21": 123,
    "key3": 999,
    "key5": 11
})

print(d)
dd = d.fromkeys("sadfas",234)
print(dd)

print(d.keys())
print(d.values())
print(d.items())

for key in d:
    print(f"key:{key} values:{d[key]}")


for key, values in d.items():
    print(f"key:{key} values:{values}")