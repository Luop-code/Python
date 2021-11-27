# CDUT 罗澎
# 开发时间：2021/11/27 15:33

class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return f"{[self.name]}占地 {self.area}"


class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area =area

        self.free_area =area
        self.item_list = []

    def __str__(self):

        return (f"户型:{self.house_type}\n"
                f"总面积：{self.area}\n"
                f"剩余面积：{self.free_area}\n"
                f"家具：{self.item_list}")


    def add_item(self, item):

        print(f"要添加 {item}")
        if item.area > self.free_area:
            print(f"{item.area}的面积太大了，无法添加")
            return

        self.item_list.append(item.name)

        self.free_area -= item.area






# 1.创建家具
bed = HouseItem("席梦思", 4)
wardrobe = HouseItem("衣柜",2)
table = HouseItem("餐桌",1.5)

print(bed)
print(wardrobe)
print(table)

# 2创建房子对象
my_house = House("三室两厅", 150)
my_house.add_item(bed)
my_house.add_item(wardrobe)
my_house.add_item(table)
print(my_house)