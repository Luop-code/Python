# CDUT 罗澎
# 开发时间：2021/11/27 15:53

class Gun:

    def __init__(self, model):
        # 1.枪的型号
        self.model = model
        # 2.子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1.判断子弹数量
        if self.bullet_count <= 0:
            print(f"{self.model} 没有子弹了")
            return
        # 2.发射子弹 -1
        self.bullet_count -= 1
        # 3.提示发射信息
        print(f"{self.model} 突突突...{self.bullet_count}")


class Soldier:

    def __init__(self, name):
        self.name = name
        # 新兵没有枪
        self.gun = None

    def fire(self):
        # 1.判断士兵是否有枪
        # is 身份运算符，用于比较两个对象的内存地址是否一直，即是否是对同一个对象的引用
        # ==判断引用变量的值是否相等
        if self.gun is None:
            print(f"{self.name} 还没有枪")
            return
        # 2.高喊口号
        print(f"冲啊...{self.name}")
        # 3.让枪装子弹
        self.gun.add_bullet(50)
        # 4.发射
        self.gun.shoot()


# 1.创建Gun对象
ak47 = Gun("AK47")

# 2.创建Soldier对象

xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)
