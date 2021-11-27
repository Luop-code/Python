# CDUT 罗澎
# 开发时间：2021/11/27 14:56

class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print(f"{self.name}来了")

    def __del__(self):
        # del方法被调用，生命周期结束
        print(f"{self.name}去了")

    def __str__(self):
        # 必须返回一个字符串
        return  f"我是小猫{self.name}"



# tom是一个全局变量
tom = Cat("Tom")
print(tom)

