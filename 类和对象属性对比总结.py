class Person:
    age = 10
    pass

p = Person()

p.age +=5
# p.age = p.age + 5 右边查询
# p.age = 15 修改

print(Person.age)
print(p.age)