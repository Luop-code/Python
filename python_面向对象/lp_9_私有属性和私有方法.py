# CDUT 罗澎
# 开发时间：2021/11/27 16:21

class Women:

    def __init__(self, name):
        self.name = name
        # 定义私有属性：在属性前面增加两个下划线 __
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print(f"{self.name}的年龄是{self.__age}")


xiaomei = Women("小美")
# 私有属性在外界不能被直接访问
# print(xiaomei.__age)

# 私有方法同样不允许外部直接访问
# xiaomei.__secret()

# python中没有真正意义的私有