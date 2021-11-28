# CDUT 罗澎
# 开发时间：2021/11/28 14:15

def input_password():
    pwd = input("请输入密码：")

    if len(pwd) >= 8:
        return pwd
    # 如果 < 8主动抛出异常
    print("主动抛出异常")
    # 1.创建异常对象 -可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够 ")
    # 2.主动抛出异常
    raise ex

try:
    print(input_password())
except Exception as result:
    print(result)