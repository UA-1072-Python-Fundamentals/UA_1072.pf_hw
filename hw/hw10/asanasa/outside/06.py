def rename_class(old_class, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        new_class = type(new_name, old_class.__bases__, dict(old_class.__dict__))
        return new_class
    else:
        raise ValueError("Invalid class name format")


class MyClass:
    def __init__(self, value):
        self.value = value


SecondUsefulClass = rename_class(MyClass, "SecondUsefulClass")


print(SecondUsefulClass.__name__)
