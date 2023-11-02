from flask import Flask, render_template, request, redirect

app = Flask(__name__)


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


def get_by_id(id):
    for user in USERS:
        if user.id == id:
            return user


@app.route('/')
def index():
    return render_template('index.html', users=USERS)


@app.route('/user/', methods=['GET', 'POST'])
def get_user():
    if request.method == 'GET':
        return render_template('uses/add.html', )
    elif request.method == 'POST':
        error = {}
        id = int(request.form['id'])
        user = get_by_id(id)
        if user:
            error["id"] = "error"
        name = request.form['name']
        age = int(request.form['age'])
        if age > 100 or age < 0:
            error["age"] = "error"
        city = request.form['city']
        if error:
            return render_template('uses/add.html', error=error)
        user = User(id, name, age, city)
        USERS.append(user)
        return redirect("/")


if __name__ == '__main__':
    # with app.test_request_context():
    #     print(url_for("hello_world"))
    #     print(url_for("hello"))
    #     print(url_for("get_user_by_name", name="Vasa"))
    #     print(url_for("get_user_by_name", name="Ira"))
    app.run()
    # app.run(host="0.0.0.0", port=80)
