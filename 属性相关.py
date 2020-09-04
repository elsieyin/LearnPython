class Person:
    height = 180
    pass

p = Person()

p.age = 18
print(id(p.age))
p.age = 20
print(id(p.age))

print(p.__dict__) # 对象的属性
print(Person.__dict__)

# e = Person()
# print(e.age)

# 可变类型
p.pets = ['小花', '小黑']
print(p.pets, id(p.pets))
p.pets.append('小刘')
# p.pets = [1, 2]

print(p.pets, id(p.pets))

q = Person()
print(id(p.height), id(q.height))