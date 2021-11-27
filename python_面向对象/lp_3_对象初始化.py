# CDUT 罗澎
# 开发时间：2021/11/27 14:34

class Cat():

    def __init__(self, new_name):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        # self.name = "汤姆"
        self.name = new_name

    def eat(self):
        print(f"{self.name}爱吃鱼")


# 使用类名（）创建对象时，会自动调用初始化方法 __init__
tom = Cat("汤姆")
print(tom.name)

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
