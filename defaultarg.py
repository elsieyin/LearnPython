m = 10

def foo(x, y=m):
    print(x, y)

m = 'a'
foo(1)
foo(1, 11)
