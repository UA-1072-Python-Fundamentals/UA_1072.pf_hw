import json


class User:
    def __init__(self, id, name, age, city):
        self.id = int(id)
        self.name = name
        self.age = int(age)
        self.city = city

    def __str__(self):
        return f"id: {self.id} Name: {self.name}, Age: {self.age}, City: {self.city}"

    def __repr__(self):
        return f"{self.id} {self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "aga": self.age,
            "city": self.city,
        }


USERS = []
with open("users.txt") as file:
    for row in file:
        data = row.split(",")
        print(data)
        USERS.append(User(*data))

print(USERS)
print(json.dump([user.to_dict() for user in USERS],
                open("user.json", "w"),
                indent=6))
