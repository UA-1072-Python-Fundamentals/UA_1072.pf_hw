 ##Task-3-1-1 print Python Zen in a str format

python_zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
print(python_zen)



 ## Task-3-1-2 Find and calculate the occurances of the words 'better', 'never' and 'is'

a = python_zen.count('better')
b = python_zen.count('never')
c = python_zen.count('is')
print(a, '  times we have word "better"')
print(b, '  times we have word "never"')
print(c, '  times we have word "is"')



 ## Task-3-1-3 Display Python Zen in Uppercase
uppercase = python_zen.upper()
print(uppercase)



 ## Task-3-1-4 Replace i with & in Pytnon Zen
i_to_ampersand = python_zen.replace('i', '&')
print(i_to_ampersand)




