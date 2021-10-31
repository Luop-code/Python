# CDUT 罗澎
# 开发时间：2021/11/22 22:20
import random

"""
age = int(input('请输入年龄：'))

if age >= 18:
    print('已成年')
    print('已成年')

# if语句下面的缩进代码部分看成完整的if部分代码块
else:
    print('哈哈哈哈')
    print('哈哈哈哈')
print('这句代码什么时候执行')

"""

"""
is_employee = True
if not is_employee:
    print("非本公司人员，请勿入内")
else:
    print("请进")
"""
"""
holiday_name = '平安夜'
if holiday_name == '情人节':
    print('玫瑰')
elif holiday_name == '平安夜':
    print('苹果')
    """

"""has_ticket = 1
knife_length = 10
if has_ticket == True:
    if knife_length >= 20:
        print("禁止通过")
    else:
        print("通过")
else:
    print("禁止进入，请买票")
"""

# 石头剪刀布，随机数

player = int(input('请输入：1.石头 2.剪刀 3.布 \n'))
computer = random.randint(1, 3)
print('玩家选择的是{},电脑出的是{}'.format(player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print('玩家胜')
elif player == computer:
    print('平局')
else:
    print('电脑赢')
