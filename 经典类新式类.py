class Person:
    pass


print(Person.__base__)

# py2.x 没写继承自object就是经典类，否则就是新式类

# py3.x 不写也是隐式继承object，默认新式类