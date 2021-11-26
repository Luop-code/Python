# CDUT 罗澎
# 开发时间：2021/11/26 21:22

def demo(*args, **kwargs):

    print(args)
    print(kwargs)


gl_num = (1,2,3)
gl_dict = {"name":"小明",
           "age":18}
demo(gl_num,gl_dict)

demo(*gl_num,**gl_dict)