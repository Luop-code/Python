# CDUT 罗澎
# 开发时间：2021/11/27 19:37

class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print(f"{self.name} 蹦蹦跳跳地玩耍")

class XiaoTianQuan(Dog):

    def game(self):
        print(f"{self.name}飞上天玩耍")

class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print(f"{self.name}和 {dog.name} 快乐地玩耍")

        # 让狗玩耍
        dog.game()


# 创建一个狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianQuan("飞天旺财")

# 创建一个小明对象
xiaoming = Person("小明")

# 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)