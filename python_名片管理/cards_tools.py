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
    print("-" * 50)
    print("新增名片")
    # 1.提示用户输入名片的信息
    name_str = input("请输入姓名：")
    phone = input("请输入手机号：")
    qq = input("请输入qq：")
    email = input("请输入邮箱：")

    # 2.使用用户信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone,
                 "qq": qq,
                 "email": email}

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示用户添加成功
    print(f"添加{name_str}的名片成功")


def show_all():
    """
显示所有名片
    """
    print("-" * 50)
    print("显示所有名片")
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请添加")
        return
    # 表头
    for name in ["姓名", "电话", "qq", "eamil"]:
        print(name, end="\t\t\t\t")

    print("")

    # 打印分隔线
    print("=" * 50)
    # 遍历名片列表，依次输出字典
    for card_dict in card_list:
        print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s" % (card_dict["name"],
                                                    card_dict["phone"],
                                                    card_dict["qq"],
                                                    card_dict["email"]))


def search_card():
    """
搜索名片1

    """
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要查找的名片
    find_name = input("请输入要查找的姓名：")

    # 2.遍历名片列表，查询，若没找到，需提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t\t\t电话\t\t\t\tqq\t\t\t\t邮箱\t\t\t\t")
            print("=" * 50)
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s" % (card_dict["name"],
                                                        card_dict["phone"],
                                                        card_dict["qq"],
                                                        card_dict["email"]))
            # TODO 针对找到的名片进行修改和删除
            deal_card(card_dict)

            break

    else:
        print(f"没有找到{find_name}")


def deal_card(find_dict):
    """
处理查找到的名片
    :param find_dict: 查找到的名片
    """
    print(find_dict)
    action_str = input("请选择要执行的操作：1.修改  2.删除  0.返回  ")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")

        print("修改")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除成功！")


def input_card_info(dict_value, tip_message):
    """
输入名片信息
    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容，就返回该内容，如果没有就返回原值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
