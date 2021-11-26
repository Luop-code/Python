# CDUT 罗澎
# 开发时间：2021/11/26 20:42

def demo(num_list):

    print("函数内部的代码")

    # 使用方法修改列表内容
    num_list.append(9)
    print(num_list)
    print("执行完成")


gl_list = [1,2,3]
demo(gl_list)
print(gl_list)