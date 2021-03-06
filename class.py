"""
# 在程序中，务必保证：先定义（类），后使用（产生对象）
PS:
1.
在程序中特征用变量标识，技能用函数标识
2.
因而类中最常见的无非是：变量和函数的定义
3.
定义类，使用关键字class + 空格 + 类名，类名用大驼峰命名，变量名推荐使用“_”这种方式就是为了区分
"""

# 程序中的类
class DeepshareStudent:
    # 用变量表示特征
    school = 'deepshare'

    # 用函数表示技能
    def learn(self):
        """
        self是你使用Pycharm自动添加的，你写成xxx也是一样的，
        他就是一个位置参数，必须被传值，具体意义请看下文
        """
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')

    print('=======>')
    # 类是特征与技能的结合体，所以类中最常见的就是变量和函数，但是类中也可以有任意的Python代码
# 执行以上代码，你会发现会打印那一行箭头，这就说明前面的代码也运行了，
# 这就说明在定义类的阶段会立刻执行类体内的代码，
# 既然执行了，有变量有函数，那就会将产生的名字存放于类的名称空间