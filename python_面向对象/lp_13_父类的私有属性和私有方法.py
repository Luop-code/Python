# CDUT 罗澎
# 开发时间：2021/11/27 19:00

class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print(f"私有方法{self.num1} {self.__num2}")


class B(A):

    def demo(self):


        # 1.子类不能访问父类的私有属性
        print(f"访问父类的私有属性{self.__num2}")

        # 2.子类不能调用父类的私有方法
        # self.__test
        # super().__num2

b = B()

print(b)

# 外界不能直接访问对象的私有属性/方法
# print(b.__num2)
# b.__test
