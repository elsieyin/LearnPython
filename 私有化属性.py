class Animal:
    __x = 10
    def test(self):
        print(Animal.__x)
        print(self.__x)

# class Dog(Animal):
#     def test2(self):
#         print(Dog.x)
#         print(self.x)

# 测试代码
# Name Mangling 不同解释器可能规则不同 不建议
print(Animal.__dict__)
print(Animal._Animal__x)


# a = Animal()
# a.test()

# d = Dog()
# d.test2()

# print(Animal.x)
# print(Dog.x)
# print(a.x)
# print(d.x)
