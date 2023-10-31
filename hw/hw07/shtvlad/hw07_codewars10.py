def convert(val):
    res="Yes" if val==True else "No"
    return res
print(convert(input("True or False?: ").lower()=="true"))


