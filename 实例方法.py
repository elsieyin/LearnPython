class Person:
    def eat(self, food):
        print(self,"在吃", food)

    def eat2(xxx):
        print(xxx)

    # def eat3():
    #     print("123")

# 标准调用
p = Person()
# print(p)
# p.eat("土豆")

# 间接调用
# print(Person.eat)
#
# Person.eat(123, "abc")

func = Person.eat
func("abc", 999)

p.eat2()
