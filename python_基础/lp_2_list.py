# CDUT 罗澎
# 开发时间：2021/11/23 21:07


# name_list = ['张三','李四','王五']

# print(name_list[3])

# 知道数据的内容，想确定在列表的位置，index取索引
# print(name_list.index('李四'))

# 修改列表中的某个数据
# name_list[1] = 'lisi'

# 增加，append方法可向列表末尾追加数据
# name_list.append('赵六')

# insert可以在列表指定索引位置插入数据
# name_list.insert(1,'小明')

# extend把另一个列表的内容追加到当前列表末尾
# temp_list = ['孙悟空','猪八戒','沙悟净']
# name_list.extend(temp_list)

# remove从列表中删除指定的数据,若数据重复，则是删除第一个出现的数据
# name_list.remove('王五')

# pop默认可以把列表最后一个元素删除，可以指定要删除元素的索引
# name_list.pop()
# name_list.pop(3)

# clear可以清空列表
# name_list.clear()

# del关键字本质是用来将一个变量从内存中删除
# del name_list[1]


"""name_list = ['张三','李四','王五','张三']
list_len = len(name_list)
print(f'列表中有 {list_len} 个元素')
count = name_list.count('张三')
print(f'张三出现了 {count} 次')
"""


"""name_list = ['zhangsan','lisi','wangwu','zhaoliu']
num_list = [5,2,3,4,9]
"""
# 升序
"""name_list.sort()
num_list.sort()
"""
# 降序
"""name_list.sort(reverse=True)
num_list.sort(reverse=True)"""

# 逆序
"""name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)"""

name_list = ['zhangsan','lisi','wangwu','zhaoliu']

# 迭代遍历

"""
顺序的从列表中依次获取数据，每一次循环中，数据都保存在my_name变量中，在循环体内部可以访问到当前这一次获取到的数据
my_name是循环内使用的变量 in 列表
for my_name in name_list:
        循环内部对列表元素进行操作
    print(f'我的名字叫 {my_name} ')"""