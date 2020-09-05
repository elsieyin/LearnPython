class Person:

    # 主要作用：创建好一个实例对象之后，会自动调用这个方法，来初始化这个对象
    def __init__(self):
        self.__age = 18

    def setAge(self, value):
        if isinstance(value, int) and 0 < value < 200:
            self.__age = value
        else:
            print("你输入的数据有问题，请重新输入，需为合理值的正整数")

    def getAge(self):
        return self.__age

p1 = Person()
# print(p1._Person__age) # 不建议
p1.setAge(-10)