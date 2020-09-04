class Person:
    age = 18
    def eat(self):
        pass

def run(self):
    print("跑", self)

xxx = type("Dog",(), {"age": 1, "run": run})
print(xxx)

d = xxx()
print(d)

d.run()