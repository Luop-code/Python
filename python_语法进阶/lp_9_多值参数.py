# CDUT 罗澎
# 开发时间：2021/11/26 21:12

def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


"""demo(1)
demo(1, 2, 3, 4,name="小明",age=18)
"""


def sum_numbers(*args):
    num = 0
    print(args)

    for n in args:
        num += n
    return num


result = sum_numbers(1,2,3,4,5)
print(result)