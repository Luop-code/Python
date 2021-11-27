# CDUT 罗澎
# 开发时间：2021/11/27 15:28



class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return f"{[self.name]}占地 {self.area}"


# 1.创建家具
bed = HouseItem("席梦思", 4)
wardrobe = HouseItem("衣柜",2)
table = HouseItem("餐桌",1.5)

print(bed)
print(wardrobe)
print(table)