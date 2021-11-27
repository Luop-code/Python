# CDUT 罗澎
# 开发时间：2021/11/27 14:20
# CDUT 罗澎
# 开发时间：2021/11/27 14:08

class   Cat:


    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print(f"{self.name}吃鱼")

    def drink(self):
        print("猫喝水")


# 创建猫对象
tom = Cat()
# 使用 .属性名 利用赋值语句,不推荐外部设置，通常直接封装在类里面
tom.name = "汤姆"
tom.eat()
tom.drink()
print(tom)

"""tim = Cat()
tim.eat()
tim.drink()
print(tim)"""
