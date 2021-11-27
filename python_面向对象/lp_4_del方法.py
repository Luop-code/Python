# CDUT 罗澎
# 开发时间：2021/11/27 14:49

class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print(f"{self.name}来了")

    def __del__(self):
        # del方法被调用，生命周期结束
        print(f"{self.name}去了")

# tom是一个全局变量
tom = Cat("Tom")
print(tom.name)

# del关键字可以删除一个对象
del tom
print("-"*50)
