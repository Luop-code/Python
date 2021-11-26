# CDUT 罗澎
# 开发时间：2021/11/26 20:02

a = 10
b = 20

# 使用临时变量
"""c = a
a = b
b = c
"""
# 不使用临时变量
"""a = a + b
b = a - b
a = a - b
"""
# python专有:利用元组
# a, b = (b, a)  ，括号可省略
a, b = b, a
print(a)
print(b)
