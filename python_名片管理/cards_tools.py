# CDUT 罗澎
# 开发时间：2021/11/25 20:13

# 记录所有名片字典
card_list = []

def menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("")
    print("*" * 50)


def new_card():
    """
新增名片
    """
    print("-"*50)
    print("新增名片")
    # 1.提示用户输入名片的信息
    name_str = input("请输入姓名：")
    phone = input("请输入手机号：")
    qq = input("请输入qq：")
    email = input("请输入邮箱：")

    # 2.使用用户信息建立一个名片字典
    card_dict = {"name":name_str,
                 "phone":phone,
                 "qq":qq,
                 "email":email}

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示用户添加成功
    print(f"添加{name_str}的名片成功")

def show_all():
    """
显示所有名片
    """
    print("-"*50)
    print("显示所有名片")
    # 表头
    for name in ["姓名","电话","qq","eamil"]:
        print(name,end="\t\t\t\t")

    print("")

    # 打印分隔线
    print("="*50)
    # 遍历名片列表，依次输出字典
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))




def search_card():
    """
搜索名片1

    """
    print("-"*50)
    print("搜索名片")
