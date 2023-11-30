def check_age(age):
    check=True
    while check:
        try:
            if int(age)<=0:
                raise ValueError
            elif int(age)%2==0:
                type="even"
            else:
                type = "odd"
            check=False
        except ValueError:
            print("Incorrect age. Try again")
            age=input("How old are your:")

    return f"Your age is {type}"

age = input("How old are your:")
print(check_age(age))
