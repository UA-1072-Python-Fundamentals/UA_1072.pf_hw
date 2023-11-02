def check_pas(pas):
    test_low,test_up,test_num,test_chr=0,0,0,0
    up_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low_letter="abcdefghijklmnopqrstuvwxyz"
    spec_chr="$#@"
    if (len(pas)>=6) and (len(pas)<=16):
        for ele in pas:
            if ele in up_letter:
                test_up+=1
            if ele in low_letter:
                test_low+=1
            if ele.isdigit():
                test_num+=1
            if ele in spec_chr:
                test_chr+=1
    if (test_chr>=1 and test_up>=1 and test_num>=1 and test_low>=1 and test_num+test_up+test_low+test_chr==len(pas)):
        test=True
    else:
        test=False
    return test
print(f"Please, input password:\n"
      "* At least 1 letter between [a-z] and 1 letter between [A-Z]\n"
      "* At least 1 character from [$#@]\n"
      "* At least 1 number between [0-9]\n"
      "* Min length 6 characters and Max length 16 characters")
print("-"*100)
pas=input("Password: ")
while check_pas(pas)==False:
    print(f"Please, input correct password:\n"
          "* At least 1 letter between [a-z] and 1 letter between [A-Z]\n"
          "* At least 1 character from [$#@]\n"
          "* At least 1 number between [0-9]\n"
          "* Min length 6 characters and Max length 16 characters")
    print("-"*100)
    pas = input("Password: ")
print("Your password is valid")
