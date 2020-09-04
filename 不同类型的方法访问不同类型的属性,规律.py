class Person:
    age = 0
    def shilifangfa(self):
        print(self)
        print(self.age)
        print(self.num)

    @classmethod
    def leifangfa(cls):
        print(cls)
        print(cls.age)
        print(cls.num)

    @staticmethod
    def jingtaifangfa():
        print(Person.age)

p = Person()
p.num = 10

# p.shilifangfa()

# p.leifangfa()
# Person.leifangfa()

Person.jingtaifangfa()
