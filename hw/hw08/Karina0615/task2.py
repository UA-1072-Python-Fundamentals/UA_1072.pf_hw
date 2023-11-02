import re
password = '1H87634#'

def validation(password):
    
    characters = ['$', '#', "@"]
    digits  = ["0","1","2","3","4","5","6","7","8","9"]
    d,c,l,a = 0,0,0,0
    
    for i in password:
        if i in characters:
            c += 1
        elif i in digits:
            d += 1
        elif not re.search("[a-z]", password):
            l += 1
        elif not re.search('[A-Z]', password):
            a += 1
    
    
    if len(password)<=6:
        print("The password is short, at least 6 characters")
    elif len(password)>=12:
        print("The password is too long, maximum 12 characters")
    elif d == 0:
        print("The password should containe at least 1 digits")
    elif c == 0:
        print("The password should containe at least 1 characters from ($,#,@)")
    elif l > 0:
        print("The password should containe at least 1 letter between [a-z]")
    elif a > 0:
        print("The password should containe at least 1 letter between [A-Z]")
    else:
        print("Password saved")


validation(password)