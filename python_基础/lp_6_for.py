# CDUT 罗澎
# 开发时间：2021/11/24 22:50

"""for num in [1,2,3]:
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用break退出循环，则else就不会执行
    print("会执行吗？")

print("循环结束")"""


students = [
    {"name":"张三"},
    {"name":"李四"},
]

# 在学员列表搜索指定的名字
find_name = "小明"

for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print(f"找到了{find_name}")
        break
else:
    print(f"没有找到{find_name}")
print("循环结束")