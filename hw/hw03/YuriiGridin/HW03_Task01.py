# 1.1 write Python's philosophy in the string format

zen = """
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
print(zen)

# 1.2 find separately the number of occurrences of the words
# - "better", "never" and "is" in the given line

count_better = zen.count("better")
print(f"Count of 'better': {count_better}")

count_never = zen.count("never")
print(f"Count of 'never': {count_never}")

count_is = zen.count("is")
print(f"Count of 'is': {count_is}")

# 1.3 display all text in uppercase (all letters in uppercase)

zen_upper = zen.upper()
print(zen_upper)

# 1.4 replace all occurrences of the symbol “i” with “&”

zen_rep = zen.replace("i", "&")
print(zen_rep)

# 2 four-digit natural number is specified

num = 9568
print(num)

# 2.1 find the product of the digits of this number

num_str = str(num)
num_multi = (int(num_str[0]) * int(num_str[1])
             * int(num_str[2]) * int(num_str[3]))
print(num_multi)

# 2.2 write the number in reverse order

num_rev = int(num_str[::-1])
print(num_rev)

# 2.3 in ascending order, you need to sort the numbers
# included in the given number

num_list = list(str(num))
num_list.sort()
num_list = int(''.join(num_list))
print(num_list)

# 3. Interchange the values of two variables without using the third variable.

x = 5
y = "test"
print(f"x= {x}, y= {y}")
[x, y] = [y, x]
print(f"x= {x}, y= {y}")
