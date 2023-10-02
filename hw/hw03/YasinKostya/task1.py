with open('zen.txt') as f:
    python_philosophy = f.read()
    #print(python_philosophy)
count_better = python_philosophy.lower().count("better")
count_never = python_philosophy.lower().count("never")
count_is = python_philosophy.lower().count("is")

uppercase_text = python_philosophy.upper()
replaced_text = python_philosophy.replace("i", "&")

print("Occurrences of 'better':", count_better)
print("Occurrences of 'never':", count_never)
print("Occurrences of 'is':", count_is)
print("Text in uppercase:", uppercase_text)
print("Text with 'i' replaced by '&':", replaced_text)