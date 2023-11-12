def rev_string(txt):
    txt_lst = txt.split()
    rev_lst = []
    for ele in range(len(txt_lst), 0, -1):
        rev_lst.append(txt_lst[ele - 1])
    print("Reversed string:"," ".join(rev_lst))

txt = input("Input string: ")
rev_string(txt)

