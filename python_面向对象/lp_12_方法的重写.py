# CDUT 罗澎
# 开发时间：2021/11/27 18:44

class Animal():
    def eat(self):
        print("吃--")

    def drink(self):
        print("喝--")

    def run(self):
        print("跑--")

    def sleep(self):
        print("睡--")


class Dog(Animal):
    # 子类拥有父类的所有属性和方法

    # def eat(self):
    #     print("吃")
    #
    # def drink(self):
    #     print("喝")
    #
    # def run(self):
    #     print("跑")
    #
    # def sleep(self):
    #     print("睡")

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

    # 方法覆盖
    # def bark(self):
    #     print("叫得跟神一样...")

    # 方法扩展
    def bark(self):


        # 1.针对子类特有的需求编写代码
        print("神一样的叫唤...")

        # 2.使用super(). 调用父类的方法
        super().bark()

        # 3.增加其他子类的代码
        print("$#%##$$")

xtq = XiaoTianQuan()
# 如果子类重写了父类的方法，会调用子类中重写的方法
xtq.bark()