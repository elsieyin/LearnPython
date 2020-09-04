#  求三个数的最大值
def max2(x, y):
    if x > y:
        return x
    else:
        return y


def max3(x, y, z):
    res1 = max2(x, y)
    res2 = max2(res1, z)
    return res2


print(max3(11, 199, 2))