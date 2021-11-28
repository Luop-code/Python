# CDUT 罗澎
# 开发时间：2021/11/28 16:19

# open默认 只读方式打开
# w，只写方式打开，若存在会被覆盖
# file = open("README","w")

# a ，追加
file = open("README","a")

file.write("123 hello")

file.close()