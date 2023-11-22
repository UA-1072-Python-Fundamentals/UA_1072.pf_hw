def cls_name_changer(cls, new_name):
    old_name=cls.__name__
    if new_name.isalnum() and new_name[0].isupper():
        cls.__name__ = new_name
        return old_name
    else:
        raise NameError('Invalid class name!')
class MyClass:
    pass

myObject = MyClass();
print(MyClass.__name__)
print(f"{cls_name_changer(MyClass, 'UsefulClass')} was renamed into {MyClass.__name__}")
print(f"{cls_name_changer(MyClass, 'SecondUsefulClass')} was renamed into {MyClass.__name__}")
