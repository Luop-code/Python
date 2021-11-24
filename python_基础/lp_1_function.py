# CDUT 罗澎
# 开发时间：2021/11/23 20:44

def print_line(char, times):
    """打印单行分隔线

    :param char: 分隔字符
    :param times: 重复次数
    """
    print(char * times)


def print_lines(char, times):
    """打印多行分割线
    :param char: 分隔线用的字符
    :param times:分隔线重复次数
    """
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


name = '罗澎'
