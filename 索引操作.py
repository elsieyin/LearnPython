class Person:
    def __init__(self):
        self.cache = {}

    def __setitem__(self, key, value):
        self.cache[key] = value

    def __getitem__(self, item):
        return self.cache[item]

    def __delitem__(self, key):
        del self.cache[key]

p = Person()
p['name'] = 'sz'
print(p['name'])
print(p.cache)
del p['name']
print(p.cache)

# -----------------------  slice  ---------------------

class Person:
    def __setitem__(self, key, value):
        # print(key, value)
        print(key.start)
        print(key.stop)
        print(key.step)
        print(value)

    def __getitem__(self, item):
        print("getitem", item)

    def __delitem__(self, key):
        print("delitem", key)

p = Person()
p[0: 4: 2] = [1, 2]
# slice

p [0: 5: 2]

del p [0: 5: 2]