def characters_calculation():

    str1 = input('Please enter a string  ')
    str1 = str1.lower()
    l = []
    for i in str1:
        x = str1.count(i)
        l.append((i,x))
        
    d = dict(l)
    return d 
         

print(characters_calculation())

