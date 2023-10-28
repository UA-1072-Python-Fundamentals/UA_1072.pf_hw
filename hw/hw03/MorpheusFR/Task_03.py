#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Given line of text
zen_str = """
The Zen of Python, by Tim Peters

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

# Task_03_1
# Find the number of occurrences of specific words
count_better = zen_str.lower().count("better")
count_never = zen_str.lower().count("never")
count_is = zen_str.lower().count("is")

print(f"Occurrences of 'better': {count_better}")
print(f"Occurrences of 'never': {count_never}")
print(f"Occurrences of 'is': {count_is}")

# Display all text in uppercase
zen_uppercase = zen_str.upper()

print(f"Text in uppercase:\n{zen_uppercase}")

# Replace all occurrences of "i" with "&"
repl_zen = zen_str.replace("i", "&")

print(f"Text with 'i' replaced by '&':\n{repl_zen}")

# Task_03_2
# Calculate the product of the digits
num = 2693
digit_prod = (num // 1000) * ((num // 100) % 10) * ((num // 10) % 10) * (num % 10)
print(digit_prod)

# Convert the number to a string and reverse it
num_str = str(num)
reversed_num = int(num_str[::-1])
print(reversed_num)

# Sort the digits in ascending order
sorted_num = int(''.join(sorted(num_str)))
print(sorted_num)

# Task_03_3
# Interchange the values of two variables without using the third variable.
a, b = 5, 2
print(f"A = {a}, B = {b}")

a, b = b, a
print(f"A = {a}, B = {b}")
