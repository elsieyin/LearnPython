class Person:
    def __init__(self, age, height):
        self.age = age
        self.height = height

    def __eq__(self, other):
        print(other)
        return self.age == other.age

    # 有ne走ne，没有走eq反结果
    # def __ne__(self, other):
    #     print("xxx")

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __lt__(self, other):
        print(self.age)
        print(other.age)
        return self.age < other.age

    # def __le__(self, other):
    #     pass

p1 = Person(18, 180)
p2 = Person(17, 190)
p3 = Person(18, 170)

# print(p1 == p2)
# print(p1 == p3)
# print(p1 != p3)

print(p1 < p2)
# print(p1 > p2)   # p2 < p1


# --------------------- @functools ----------------

import functools


@functools.total_ordering
class Person:
    def __lt__(self, other):
        print("lt")
        pass

    def __eq__(self, other):
        print("eq")
        pass


p1 = Person()
p2 = Person()

print(p1 <= p2)

import pprint

pprint.pprint(Person.__dict__)