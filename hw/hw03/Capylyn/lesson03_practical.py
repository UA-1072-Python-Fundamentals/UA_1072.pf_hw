#Task3.1

#creating a str
philosophy_python = """
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


findind_words01 = philosophy_python.find("better") #finding how many there are "better"
findind_words02 = philosophy_python.find("never") #finding how many there are "never"
findind_words03 = philosophy_python.find("is") #finding how many there are "is"
print(f'''There are that much 'better', 'never' and 'is' in Python zen:
Better - {findind_words01}
Never - {findind_words02}
Is - {findind_words03}''')

#Task 3.2, replacing every "i" with "&"
print(philosophy_python.upper().replace("I", "&"))

#Task 3.3
def sorting_brackets(my_list):  #function to remove square brackets from the output.
    my_list = ', '.join(str(item) for item in my_list)
    return my_list


numbers = [2,3,9,4]
print("The product of the numbers is", numbers[0]*numbers[1]*numbers[2]*numbers[3])

numbers_reversed = numbers[::-1] #creating a variable that will store reversed list
removing_brackets01 = sorting_brackets(numbers_reversed) #removing square brackets
print("The list of numbers in reverse looks like:", removing_brackets01)

#creating a variable to store the list in ascending order and removing square brackets
numbers_sorted = sorted(numbers)
removing_brackets02 = sorting_brackets(numbers_sorted)
print("The list of numbers sorted in ascending order: ", removing_brackets02)

#Task 3.3, interchanging the values of two variables without using the third variable.
fruit = "apple"
cars = ["Audi", "Mercedes", "Toyota"]
fruit, cars = cars, fruit
print(f"Fruits are {sorting_brackets(fruit)} and car is {cars}. Oops, something was mixed in this universe.")
