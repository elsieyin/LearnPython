# class Person:
#     def __init__(self):
#         self.result = 1
#
#     def __getitem__(self, item):
#         self.result += 1
#         if self.result >= 6:
#             raise StopIteration("停止遍历")
#         return self.result
#
# p = Person()
#
# for i in p:
#     print(i)


# --------------------------------------

# 方式2
# class Person:
#     def __init__(self):
#         self.result = 1
#
#     def __iter__(self):
#         print("iter")
#         # return iter([1, 2, 3, 4, 5])
#         return self
#
#     def __next__(self):
#         self.result += 1
#         if self.result >= 6:
#             raise StopIteration("停止遍历")
#         return self.result
#
#
# p = Person()
#
# for i in p:
#     print(i)

# ---------------------------

class Person:
    def __init__(self):
        self.age = 1

    def __iter__(self):
        self.age = 1  # 初始化值，复用迭代器
        return self

    def __next__(self):
        self.age += 1
        if self.age >= 6:
            raise StopIteration("停止遍历")
        return self.age


p = Person()

for i in p:
    print(i)

for i in p:
    print(i)