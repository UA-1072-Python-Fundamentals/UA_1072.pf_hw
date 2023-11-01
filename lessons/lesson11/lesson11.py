# class Model:
#     @classmethod
#     def get_by_id(cls, id):
#         print(cls)
#         # obj = cls.objects.get(id)
#         # return obj
# class User(Model):
#     pass
#
# class Order(Model):
#     pass
#
# User.get_by_id(10)
# Order.get_by_id(10)

# x = int(input("x: "))
# y = int(input("y: "))
# print(x/y)
# print("end")


# a = [5, 6, 7, 8]
#
# print("Second element = {}".format(a[1]))
# # Throws error since there are only 4 elements in array
# print("Fifth element = {}".format(a[4]))
#
# print("end program")
# a = [5, 6, 7, 8]
# try:
#     print("Second element = {}".format(a[1]))
#     # Throws error since there are only 4 elements in array
#     print("Fifth element = {}".format(a[4]))
# except IndexError as err:
#     print("err", err)
#
# print("end program")

# Program to handle multiple errors with one except statement
# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# except(ZeroDivisionError, NameError, ValueError) as err:
#     print("Error Occurred and Handled", type(err), err)
# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# except ValueError:
#     print("Value Error!")
# except NameError:
#     print("NameError!")
# except ZeroDivisionError:
#     print("ZeroDivisionError!")
# except:
#     print("Error!")
# read = True
# while read:
#     try:
#         a = int(input("Enter your number: "))
#         if a < 4:
#             b = a / (a - 3)  # throws ZeroDivisionError for a = 3
#         if a >= 4:
#             print("Value of b = ", b)  # throws NameError
#     # note that braces () are necessary here for multiple exceptions
#     except ValueError:
#         print("Value Error!")
#     except NameError:
#         read = False
#         print("NameError!")
#     except ZeroDivisionError:
#         read = False
#         print("ZeroDivisionError!")
#     except:
#         read = False
#         print("Error!")
#     else:
#         read = False
#         print("Nothing went wrong")
#     finally:
#         print("all")

# def f(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 0
#     finally:
#         return "all"
# a = f(5, 5)
# print(a)

#
# while True:
#     try:
#         a = int(input("Enter your number: "))
#         if a < 4:
#             b = a / (a - 3)  # throws ZeroDivisionError for a = 3
#         if a >= 4:
#             print("Value of b = ", b)  # throws NameError
#     # note that braces () are necessary here for multiple exceptions
#
#     except ZeroDivisionError:
#         read = False
#         print("ZeroDivisionError!")
#     except ArithmeticError as err:
#         print("ArithmeticError", err)

# try:
#     value = int(input("Enter a positive integer: "))
#     if value <= 0:
#         raise ValueError("That is not a positive number!")
# except ValueError as e:
#     print(e)

# class CustomError(Exception):
#     pass
#
# total_score = int(input("Enter expert score: "))
# try:
#     num_of_group = int(input("Enter number of your group: "))
#     if num_of_group < 1:
#         raise CustomError("Number of your group can't be less than 1")
# except CustomError as e:
#     print("We obtain error:", e)

from log_conf import logging
logging.info("run")

class UserError(Exception):pass
class User:
    def __init__(self, id,  name, age, city):
        try:
            self.id = int(id)
        except ValueError as err:
            self.id = -1
            logging.error(f"not valid id {id}")

        self.name = name
        try:
            self.aga = int(age)
        except ValueError as err:
            self.aga = None
            logging.error(f"not valid age {age}")
        self.city = city
        logging.debug(f"create User {self}")
    def __str__(self):
        return f"id: {self.id} Name: {self.name}, Age: {self.aga}, City: {self.city}"
    def __repr__(self):
        return f"{self.id} {self.name}"


def get_by_id(id, users):
    for user in users:
        if user.id == id:
            return  user
    logging.error(f"invalid id {id}")
    raise UserError("invalid id")
users = []
with open("users.txt") as file:
    for row in file:
        data = row.split(",")
        print(data)
        users.append(User(*data))
print(users)

print(get_by_id(5, users))
# print(get_by_id(55, users))
logging.info("end run")