# positional argument follows keyword argument
def foo(x, y, z):
    print(x, y, z)

# WRONG : foo(x=1, y=2 ,3)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

"""
 This function can be called in several ways:
 giving only the mandatory argument: ask_ok('Do you really want to quit?')
 giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
 or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

"""

