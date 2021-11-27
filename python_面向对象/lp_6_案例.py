# CDUT 罗澎
# 开发时间：2021/11/27 15:01

class Person():

    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"我的名字是{self.name},体重是{self.weight}公斤"

    def run(self):
        print(f"{self.name}爱跑步")
        self.weight -= 0.5

    def eat(self):
        print(f"{self.name}是吃货，吃完再减肥")
        self.weight += 1

xiaoming = Person("小明", 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)


xiaomei = Person("小美",45)
xiaomei.eat()
xiaomei.run()
print(xiaomei)