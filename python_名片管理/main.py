import cards_tools

while True:
    # TODO 显示功能彩单
    cards_tools.menu()

    action_str = input("请选择希望执行的操作：")
    print(f"您选择的操作是{action_str}")

    if action_str in "1,2,3":
        if action_str == "1":
            cards_tools.new_card()

        elif action_str == "2":
            cards_tools.show_all()
        elif action_str == "3":
            cards_tools.search_card()

    elif action_str == "0":
        print("退出系统")
        break
    else:
        print("选择错误")
