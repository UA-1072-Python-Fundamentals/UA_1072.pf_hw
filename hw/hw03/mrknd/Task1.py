print("Task1 -> ", __name__)

zen = '''1.Beautiful is better than ugly.
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
'''

print(zen)

#Task 1.1
quote = input('Paste your quote and i will count words: ')
quote = quote.lower()
print("I found the word [better]", quote.count('better'), "times")
print("I found the word [never]", quote.count('never'), "times")
print("I found word [is]", quote.count('is'), "times")
print()
#Task 1.2
print(zen.upper())

#Task 1.3
print(zen.replace('i', '&'))