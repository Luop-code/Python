# CDUT 罗澎
# 开发时间：2021/11/28 16:13

# 1.打开文件
file = open("README")

# 2.读取文件内容
text = file.read()
print(text)
print(len(text))

print("-"*50)

# 执行read后，文件指针移动到读取内容的末尾
text = file.read()
print(text)
print(len(text))

# 3.关闭文件
file.close()
