# 创建很多个画笔，画笔的类型（钢笔，铅笔），画笔的颜色（红色，黄色，兰色，绿色）

# print("创建了一个%s这个类型的画笔，它是%s的颜色" % ("钢笔","红色"))
# print("创建了一个%s这个类型的画笔，它是%s的颜色" % ("钢笔","绿色"))
# print("创建了一个%s这个类型的画笔，它是%s的颜色" % ("钢笔","黄色"))
# print("创建了一个%s这个类型的画笔，它是%s的颜色" % ("钢笔","兰色"))

# def createPen(pcolor, ptype):
#     print("创建了一个%s这个类型的画笔，它是%s的颜色" % (ptype, pcolor))
#
# createPen("钢笔","红色")
# createPen("钢笔","黄色")
# createPen("钢笔","兰色")
#
# import functools
#
# gangbiFunc = functools.partial(createPen, ptype = "钢笔")
#
# # gangbiFunc(pcolor = "红色")
# gangbiFunc("黄色")
# gangbiFunc("绿色")

class PenFactory:

    def __init__(self, ptype):
        self.ptype = ptype

    def __call__(self, pcolor):
        print("创建了一个%s这个类型的画笔，它是%s的颜色" % (self.ptype, pcolor))

gangbiF = PenFactory("钢笔")
gangbiF("红色")
gangbiF("黄色")
gangbiF("兰色")

qianbiF = PenFactory("铅笔")
qianbiF("红色")
qianbiF("黄色")
qianbiF("兰色")