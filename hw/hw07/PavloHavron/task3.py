def count():
    print("Enter something?")
    inp_str = input()
    out = {x : inp_str.count(x) for x in set(inp_str )} 
    print ("Occurrence of each character in you string is "+ str(out)) 



