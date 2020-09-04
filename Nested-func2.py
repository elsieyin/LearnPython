# 示例2
# 函数在定义阶段不执行函数体内的代码
def f1():
    print('f1')

    def f2():
        print('f2')

        def f3():
            print('f3')

        f3()

    f2()


f1()