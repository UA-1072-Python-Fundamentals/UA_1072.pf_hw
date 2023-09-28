#1.1 find separately the number of occurrences of the words "better", "never" and "is" in the given line

zen = '''
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
'''
zen = zen.lower()

count_better = (zen.count('better'))
count_never = (zen.count('never'))
count_is = (zen.count('is'))

print('"better" appears', count_better, 'times.')
print('"never" appears', count_never, 'times.')
print('"is" appears', count_is, 'times.' )

# 1.2 you need to display all text in uppercase (all letters in uppercase)

print(zen.upper())

#1.3 replace all occurrences of the symbol “i” with “&”

print(zen.replace('i','&'))

#2.1 find the product of the digits of this number

number = (2459)

digit_product =((number % 10) * ((number // 10) % 10) * ((number // 100) % 10) * (number // 1000))

print(f"digit_product: {digit_product}")

#2.2 write the number in reverse order

reverse_number = int(str(number)[::-1])

print(f"reverse_number: {reverse_number}")

#2.3 in ascending order, you need to sort the numbers included in the given number

sorted_number = int("".join(sorted(str(number))))

print(f"sorted_number: {sorted_number}")

#3 Interchange the values of two variables without using the third variable

a = 5
b = 10

# Interchange the values without using a third variable
a = a + b
b = a - b
a = a - b

print("After interchange:")
print("a =", a)
print("b =", b)



