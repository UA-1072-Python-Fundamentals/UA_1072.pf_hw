python_philosophy = """
BEAUTIFUL is better than ugly.
EXPLICIT is better than implicit.
SIMPLE is better than complex.
COMPLEX is better than complicated.
FLAT is better than nested.
SPARSE is better than dense.
READABILITY counts.
SPECIAL CASES aren't special enough to break the rules.
Although practicality beats purity.
ERRORS should never pass silently.
Unless explicitly silenced.
IN the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# Find occurrences
occurrences_better = python_philosophy.upper().count("BETTER")
occurrences_never = python_philosophy.upper().count("NEVER")
occurrences_is = python_philosophy.upper().count("IS")

# Display results
print(f"Occurrences of 'BETTER': {occurrences_better}")
print(f"Occurrences of 'NEVER': {occurrences_never}")
print(f"Occurrences of 'IS': {occurrences_is}")

# Display all text in uppercase
python_philosophy_upper = python_philosophy.upper()
print(f"All text in uppercase: {python_philosophy_upper}")

# Replace 'i' with '&'
python_philosophy_replaced = python_philosophy_upper.replace("I", "&")
print(f"Text with 'i' replaced with '&': {python_philosophy_replaced}")