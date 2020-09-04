class X:
    def go(self):
        print('x')

class A(X):
    def go(self):
        print('A')
        # super().go()

class B(X):
    def go(self):
        print('B')
        # super().go()

class C(A, B):
    def go(self):
        super().go()

c = C()
c.go()
print(C.mro())