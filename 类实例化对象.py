class Money:
    age = 18
    count = 1
    num = 666

one = Money()
two = Money()
print(id(one),id(two))
print(id(one.age),id(two.age))

class Test:
    sex = 'male'

one.__class__ = Test
print(one.sex)

one.sex = 'female'
print(one.sex)