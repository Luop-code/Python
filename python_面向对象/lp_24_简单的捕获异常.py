# CDUT 罗澎
# 开发时间：2021/11/27 21:21

try:
    # 不能确定正确执行的代码
    num = int(input("请输入一个整数："))
    result = 8 / num
    print(result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("请输入正确的整数：")




