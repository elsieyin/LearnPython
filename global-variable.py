len = 0

def f1():
    len = 1

    def f2():
        # len = 2
        print(len)

    # len = 3
    f2()

f1()