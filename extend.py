l1 = [1, 2, 3, 4, 5, ]
l1.extend([6, 7, 8, 9])
print(l1)
l1.extend('abc')
print(l1)
l1.extend('a')  # 也是可迭代对象
print(l1)
# l1.extend(1)  # 报错，不可迭代
print(l1)
