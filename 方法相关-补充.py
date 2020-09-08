# class Person:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#
#     def __str__(self):
#         return "姓名%s,年龄%s"%(self.name, self.age)
#
# p1 = Person("sz", 18)
# print(p1)
#
# p2 = Person("lb", 19)
# print(p2)
#
# s = str(p1)
# print(s, type(s))

# ------------------- repr -------------------

# class Person:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#
# #     def __str__(self):
# #         return "姓名%s,年龄%s"%(self.name, self.age)
#
#     def __repr__(self):
#         return "repr"
#
# p1 = Person("sz", 18)
# print(p1) # 1
#
# p1        # 2

# ------------------- call -------------------

class Person:
    def __call__(self, *args, **kwargs):
        print("xxx", args, kwargs)

p = Person()

p(123, 456, name = "sz")