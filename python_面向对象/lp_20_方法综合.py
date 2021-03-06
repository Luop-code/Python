# CDUT 罗澎
# 开发时间：2021/11/27 20:25

class Game(object):

    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息： ")

    @classmethod
    def show_top_score(cls):
        print(f"历史记录：{cls.top_score}")

    def start_game(self):
        print(f"{self.player_name} 开始游戏")

# 1.查看游戏帮助信息
Game.show_help()

# 2.查看历史最高分
Game.show_top_score()

# 3.创建游戏对象
game = Game("小明")
game.start_game()
