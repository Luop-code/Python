# CDUT 罗澎
# 开发时间：2021/11/27 16:49

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


class Cat(Animal):

    def catch(self):
        print("抓老鼠")


"""wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()"""

# 创建一个啸天犬类
xtq = XiaoTianQuan()
xtq.fly()
xtq.bark()
xtq.eat()
