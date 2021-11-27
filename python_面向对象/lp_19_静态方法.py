# CDUT 罗澎
# 开发时间：2021/11/27 20:19

class Dog(object):

    # 不访问实例属性/类属性
    @staticmethod
    def run(cls):
        print("小狗要跑...")

# 通过 类名. 调用静态方法 - 不需要创建对象
Dog.run(Dog)
