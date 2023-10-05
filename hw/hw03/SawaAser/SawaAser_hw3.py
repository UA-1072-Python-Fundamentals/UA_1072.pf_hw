the_zen_of_python_by_Tim_Peters = """
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








# Task1.1
print("Task1.1")
print(the_zen_of_python_by_Tim_Peters.count("better"))
print(the_zen_of_python_by_Tim_Peters.count("never"))
print(the_zen_of_python_by_Tim_Peters.count("is"))

# incorrect but possible
# split_text = the_zen_of_python_by_Tim_Peters.split()
# count_better = 0
# count_never = 0
# count_is = 0
# for i in range(len(split_text)):
#     if split_text[i] == "better":
#         count_better += 1
#     elif split_text[i] == "never" or split_text[i] == "never.":
#         count_never += 1
#     elif split_text[i] == "is" or split_text[i] == "it's":
#         count_is += 1
# print(f"\nTask1.1:\nbetter = {count_better}")
# print(f"never = {count_never}")
# print(f"is = {count_is}\n")


# Task1.2
new_upper_list = the_zen_of_python_by_Tim_Peters.upper()
print(f"\nTask1.2:\n{new_upper_list}")


# Task1.3
new_list_without_i = the_zen_of_python_by_Tim_Peters.replace("i" or "I", "&")
print(f"\nTask1.3:\n{new_list_without_i}")


# Task2.1:
specified_number = 3467
number_first = specified_number // 1000
number_second = (specified_number - number_first*1000) // 100
number_third = (specified_number - number_first*1000 - number_second*100) // 10
number_fourth = specified_number % 10

specified_number = [number_first, number_second, number_third, number_fourth]

summ = 0
for i in range(len(specified_number)):
    summ += specified_number[i]
print(f"\nTask2.1\nsum: {summ}")


# Task2.2
reserved_order = specified_number[::-1]
print(f"\nTask2.2\nreserved_order: {reserved_order}")


# Task2.3
for j in range(len(specified_number)):
    for i in range(len(specified_number)-1):
        if specified_number[i] > specified_number[i+1]:
            specified_number[i+1], specified_number[i] = specified_number[i], specified_number[i+1]
print(f"\nTask2.3\nsorted_list: {specified_number}")


# Task3
first_value = 100
second_value = 200
print("\nTask3:")
print(f"first_value = {first_value}")
print(f"second_value = {second_value}")

first_value, second_value = second_value, first_value
print(f"first_value = {first_value}")
print(f"second_value = {second_value}")
