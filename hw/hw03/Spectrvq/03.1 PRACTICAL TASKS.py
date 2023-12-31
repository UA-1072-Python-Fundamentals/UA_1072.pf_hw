the_zen_of_python_by_tim_peters = """
1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!
20.Beautiful is better than ugly.
21.Explicit is better than implicit.
22.Simple is better than complex.
23.Complex is better than complicated.
24.Flat is better than nested.
25.Sparse is better than dense.
26.Readability counts.
27.Special cases aren't special enough to break the rules.
28.Although practicality beats purity.
29.Errors should never pass silently.
30.Unless explicitly silenced.
31.In the face of ambiguity, refuse the temptation to guess.
32.There should be one-- and preferably only one --obvious way to do it.
33.Although that way may not be obvious at first unless you're Dutch.
34.Now is better than never.
35.Although never is often better than *right* now.
36.If the implementation is hard to explain, it's a bad idea.
37.If the implementation is easy to explain, it may be a good idea.
38.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
39.Explicit is better than implicit.
40.Simple is better than complex.
41.Complex is better than complicated.
42.Flat is better than nested.
43.Sparse is better than dense.
44.Readability counts.
45.Special cases aren't special enough to break the rules.
46.Although practicality beats purity.
47.Errors should never pass silently.
48.Unless explicitly silenced.
49.In the face of ambiguity, refuse the temptation to guess.
50.There should be one-- and preferably only one --obvious way to do it.
51.Although that way may not be obvious at first unless you're Dutch.
52.Now is better than never.
53.Although never is often better than *right* now.
54.If the implementation is hard to explain, it's a bad idea.
55.If the implementation is easy to explain, it may be a good idea.
56.Namespaces are one honking great idea -- let's do more of those!
"""


# Task 1. You need to write Python's philosophy in the string format:
# - find separatelythe number of occurrences of the words
#   "better", "never" and "is" in the given line
print(the_zen_of_python_by_tim_peters.count("better"))
print(the_zen_of_python_by_tim_peters.count("never"))
print(the_zen_of_python_by_tim_peters.count("is"))

# - you need to display all text in uppercase (all letters in uppercase)
print(the_zen_of_python_by_tim_peters.upper())

# - replace all occurrences of the symbol "i" with "g"
print(the_zen_of_python_by_tim_peters.replace("i", "g"))


# Task 2. A four-digit natural number is specified:
# - find the product of the digits of this number
number = input("Type four digit natural number: ")
print(int(number[0]) * int(number[1]) * int(number[2]) * int(number[3]))

# - write the number in reverse order
number = input("Type four digit natural number: ")
print(number[-1] + number[-2] + number[-3] + number[-4])

# - in ascending order, you need to sort the numbers included in the given number
number = input("Type four digit natural number: ")
softed_number = sorted(number)
print(softed_number)


# Task 3. lnterchange the values of two variables without usíng the thírd variable.
a = input("Type a: ")
b = input("Type b: ")
a, b = b, a
print(f"a = {a}\nb = {b}")
