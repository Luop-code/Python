# CDUT 罗澎
# 开发时间：2021/11/27 20:41

class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        # 1.创建对象时，new方法会被自动调用
        print("创建对象，分配空间")

        # 2.为对象分配空间
        # 这里new是静态方法，重新调用父类的new，要主动传递参数cls，静态方法不代表就不会传参
        instance = super().__new__(cls)

        # 3.返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player =MusicPlayer()
print(player)