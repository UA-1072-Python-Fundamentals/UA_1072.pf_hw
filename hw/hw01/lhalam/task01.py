with open("./users.txt") as f:
    users = f.readlines()
    for i in range(1,60):
        print(f"{i} - {users[int(i%32)]}")