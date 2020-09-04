# 示例1
def func1():
    print('from func1')

    def func2():
        print('from func2')

    print(func2)
    func2()


func1()
func2()
#print(func2)
