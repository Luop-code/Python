# CDUT 罗澎
# 开发时间：2021/11/26 20:56

"""gl_list = [6,3,9]
# 默认升序
gl_list.sort()

# 降序，需指定reverse参数
gl_list.sort(reverse=True)
print(gl_list)"""


def print_info(name,title="", gender=True):
    """
缺省参数默认值，必须在参数列表末尾
    :param title: 职位
    :param name: 班上的同学姓名
    :param gender: True 男生，False女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print(f"{name}是{gender_text}")


print_info("小明", True)
print_info("张三")
# 如果有多个缺省参数，需指定参数名
print_info("小美",gender=False)
