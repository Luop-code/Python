# CDUT 罗澎
# 开发时间：2021/11/24 19:05

# lp = {'name': 'luopeng',
#       'age': 21,
#       'gender': 'man', }

# 取值
# print(lp['name'])

# 如果key不存在，则增加键值对
# lp['qq'] = 1656488310
# print(lp)

# 如果key存在，会修改已经存在的键值对
# lp['name'] = '罗澎'

# 删除
# lp.pop('qq')
# print(lp)

"""lp = {'name': 'luopeng',
      'age': 21,
      'gender': 'man', }"""

# print(len(lp))
# tmp = {'qq':16564853310}
# update合并字典
# lp.update(tmp)
# print(lp)
# 清除字典
# lp.clear()

# 变量k是每一次循环中，获取到的键值对的key
"""for k in lp:

      print(f'{k}-{lp[k]}')"""



card_list = [
      {'name':'zhangsan',
       'age':20,
       'gender':'man'},
      {'name': 'luopeng',
      'age': 21,
      'gender': 'man', }
      ]
for card_info in card_list:
      print(card_info)

