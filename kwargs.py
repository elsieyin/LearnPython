def foo(x, y, z, **kwargs):  # kwargs={'c':3,'a':1,'b':2}
    print(x, y, z)
    print(kwargs)


foo(x=1, y=2, z=3, a=1, b=2, c=3)