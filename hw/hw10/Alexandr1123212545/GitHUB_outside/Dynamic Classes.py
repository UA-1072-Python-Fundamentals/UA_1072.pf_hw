class MyClass:
    pass


def class_name_changer(cls, new_name):
    """
    Class name  validity.
    """
    if not new_name.isalnum() or not  new_name[0].isupper():
        raise Exception
    else:
        cls.__name__ = new_name

if __name__ == "__main__":
    myObject = MyClass();
    print(MyClass.__name__)
    class_name_changer(MyClass, 'NewClass')
    print(MyClass.__name__)
    class_name_changer(MyClass, 'newClass')