def number_char(word):
    lst = {}
    for char in word:
        cnt=word.count(char)
        lst.update({char:cnt})
    return lst
word=input("Input any word: ")
print(f"Number of characters in '{word}':\n",number_char(word))