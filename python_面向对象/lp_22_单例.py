# CDUT 罗澎
# 开发时间：2021/11/27 20:56

class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None
    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        print("初始化播放器")


    pass

# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)