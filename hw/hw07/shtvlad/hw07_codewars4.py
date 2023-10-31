def convert_to_str(num):
    print(num,type(num))
    print(str(num),type(str(num)))
    print("%s" % num, type("%s" % num))
    print("{}".format(num), type("{}".format(num)))
    print(f"{num}", type(f"{num}"))

convert_to_str(int(input("Input any number: ")))
