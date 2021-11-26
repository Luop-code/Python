# CDUT 罗澎
# 开发时间：2021/11/26 21:28

def sum_number(num):
    if num == 1:
        return 1

    tmp = sum_number(num - 1)
    return num + tmp


result = sum_number(100)
print(result)
