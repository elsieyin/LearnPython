# class Person(object):
#     def __init__(self):
#         self.__age = 18
#
#     # 主要作用：可以以使用属性的方式，来使用这个方法
#     @property
#     def age(self):
#         return self.__age
#
# p1 = Person()
# # print(p1.__age)       # 私有属性，取不到
# # print(p1.__dict__)    # 可以._Person__age取
# # print(p1._Person__age)
#
# p1.age = 18
# print(p1.__dict__)      # 会在p1加一个属性:age
#
# print(p1.age)
# # p1.age = 666            # 如果不用property，这里修改也不会报错,会在p1加一个属性:age
# # print(p1.age)
# # print(p1.__dict__)

# ----------------------------------------

class Person:
    # 当我们通过 “实例.属性 = 值”，给一个实例增加一个属性，或者说，修改一下属性值的时候，都会调用这个方法
    # 在这个方法内部，才会真正的把这个属性，以及对应的数据，给存储到__dict__字典里面
    def __setattr__(self, key, value):
        print(key, value)

        # 1. 判定: key 是否是我们需要设置的只读属性的名称
        if key == "age" and key in self.__dict__.keys():
            print("这个属性是只读属性，不能设置数据")
        # 2. 如果不是，讲这个非只读属性真正的添加到这个实例中去
        else:
            # self.key = value    # 此时进入死循环
            self.__dict__[key] = value

p1 = Person()
p1.age = 18
# p1.name = "sz"
print(p1.age)
print(p1.__dict__)