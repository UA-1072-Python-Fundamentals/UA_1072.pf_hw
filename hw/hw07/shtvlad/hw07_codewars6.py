def rev_string(lst):
    rev_lst = []
    for ele in range(len(lst), 0, -1):
        rev_lst.append(lst[ele - 1])
    print(f"{lst} = {rev_lst}")

lst = input("Input elements of list: ").split()
rev_string(lst)

