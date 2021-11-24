# CDUT 罗澎
# 开发时间：2021/11/24 19:27

# str1 = "hello world"
# print(str1)

"""for k in str1:
    print(k)"""
# 统计某一子字符串出现的次数
# print(str1.count('o'))

# 某一个子字符串出现的位置
# print(str1.index('o'))

# 判断字符串中是否包含数字

"""num = '1'
print(num)
# 都不能判断小数

print(num.isdecimal()) # 只包含数字，返回True
print(num.isdigit())    # 返回True ，全角数字，（1），\u00b2
print(num.isnumeric())# 返回True，全角数字，汉字
"""

"""
str = "hello world"
print(str.startswith("hello"))
print(str.endswith("world"))

# find如果指定字符不存在，返回-1
print(str.find("wo"))
print(str.find("abc"))
# replace不会修改原字符串
print(str.replace("world","python"))
print(str)

"""

"""poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
"""
# for poem_str in poem:
    # 先使用strip方法去除字符串中的空白字符，再使用center方法居中显示文本
    # print('|{}\t|'.format(poem_str.strip().center(10)))


    # print('|{}\t|'.format(poem_str.center(10)))
    # print('|{}\t|'.format(poem_str.ljust(10)))
    # print('|{}\t|'.format(poem_str.rjust(10)))
"""
poem = "登鹳雀楼\t 王之涣\t 白日依山尽\t 黄河入海流\t\n 欲穷千里目\t 更上一层楼\t"
print(poem)

# 1.拆分字符串,将一个大的字符串拆分成一个列表
poem_list = poem.split()
print(poem_list)
# 2.合并字符串
result = "\n".join(poem_list)
print(result)
"""

num = "0123456789"
# 开始索引: 结束索引 : 截取步长    -1是倒数第一个索引
print(num[-1::-1])  # 逆序，步长为-1，从右向左截更上一层楼