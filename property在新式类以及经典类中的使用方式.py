    # class Person(object):
    #     def __init__(self):
    #         self.__age = 18
    #
    #     def get_age(self):
    #         print("---, get")
    #         return self.__age
    #
    #     def set_age(self, value):
    #         print("---, set")
    #         self.__age = value
    #
    #     age = property(get_age, set_age)
    #
    # p = Person()
    # print(p.age)
    # print(p.__dict__)
    #
    # p.age = 90
    # print(p.age)

# 第二种方法

class Person(object):
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        print("--- get")
        return self.__age

    @age.setter
    def age(self, value):
        print("--- set")
        self.__age = value

p = Person()
print(p.age)

p.age = 18
print(p.age)

# 经典类略麻烦，懒得总结