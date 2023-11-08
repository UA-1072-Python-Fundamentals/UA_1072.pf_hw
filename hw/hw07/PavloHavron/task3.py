def count():
    print("Enter something?")
    inp_str = input()
    out = {x : inp_str.count(x) for x in set(inp_str )} 
    print ("Occurrence of all characters in you string is "+ str(out)) 
count()



