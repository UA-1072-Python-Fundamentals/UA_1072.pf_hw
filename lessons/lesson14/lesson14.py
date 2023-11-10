# file = open("users.txt")
# text = file.read()
# print(text)
# # file = open("users.txt")
# file.seek(0)
# text = file.readline()
# print(text)
# # file = open("users.txt")
# text = file.readlines()
# print(text)
#
# file.seek(0)
# for line in file:
#     print(line)
# for line in open("../lesson12/users21.txt"):
#     print(line)
#
# for line in open("C:/data/github/UA_1072.pf_hw/lessons/lesson12/users22.txt"):
#     print(line)

# open("gjdsb") #error
# file = open("out1.txt", "w")
#
# import datetime
# file.write(str(datetime.datetime.now()))
#
# file = open("out1.txt", "a")
# import datetime
# file.write(f"start - {str(datetime.datetime.now())}\n")
# import time
# time.sleep(600)
# file.write(f"end - {str(datetime.datetime.now())}\n")
#
#
# # file = open("users.txt", "br")
# # text = file.read()
# # print(text)
# #
# # file.close()
#
# with open("users.txt") as file:
#     pass

import json

json_string = """
{
"firstName": "Ivan", "lastName": "King",
"hobbies": ["reading", "traveling", "singing"],
"age": 33,
"children":
[
{
"firstName": "Vira",
"age":
3
},{
"firstName": "Maksym",
"age":
5
}
]
}
"""

data = json.loads(json_string)
print(data)
print(data['firstName'])
data2 = json.load(open("data.json"))
print(data2["children"])