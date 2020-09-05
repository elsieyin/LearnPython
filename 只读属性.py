class Person(object):
    def __init__(self):
        self.__age = 18

    # 主要作用：可以以使用属性的方式，来使用这个方法
    @property
    def age(self):
        return self.__age

p1 = Person()
# print(p1.__age)       # 私有属性，取不到
# print(p1.__dict__)    # 可以._Person__age取
# print(p1._Person__age)

p1.age = 18
print(p1.__dict__)      # 会在p1加一个属性:age

print(p1.age)
# p1.age = 666            # 如果不用property，这里修改也不会报错,会在p1加一个属性:age
# print(p1.age)
# print(p1.__dict__)