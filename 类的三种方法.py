# 函数
def eat():
    print(1)
    print(2)
    print(3)

eat()

# 方法
class TestMethod:
    def normal(self):   # 补全self
        print("普通方法", self)

    @classmethod
    def class_method(cls):
        print("类方法", cls)

    @staticmethod
    def static_method():
        print("静态方法")

test = TestMethod()
test.normal()
# 普通方法 <__main__.TestMethod object at 0x00000236AEC5F908>
# TestMethod.normal()
# typeError: normal() missing 1 required positional argument: 'self'

# TestMethod.class_method()
# 类方法 <class '__main__.TestMethod'>

# TestMethod.static_method()

print(test.__dict__)
print(TestMethod.__dict__)