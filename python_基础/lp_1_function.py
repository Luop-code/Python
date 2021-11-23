# CDUT 罗澎
# 开发时间：2021/11/23 20:44

def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    """打印多行分割线"""
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


print_lines('-',50)
