# CDUT 罗澎
# 开发时间：2021/11/26 17:23


# 开发时，应该把模块中的所有全局变量定义在所有函数上方
num = 10


def demo1():
    # 希望修改全局变量的值  使用globa声明一下变量即可
    # global关键字会告诉解释器后面的变量是全局变量，再使用赋值语句时，就不会创建局部变量
    global num

    # python中，不允许直接修改全局变量的值
    # 如果使用赋值语句，会在函数内部定义一个局部变量

    num = 99
    print(f"demo1 ==> {num}")


def demo2():
    print(f"demo2 ==> {num}")

demo1()
demo2()