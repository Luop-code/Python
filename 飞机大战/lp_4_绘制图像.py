# CDUT 罗澎
# 开发时间：2021/11/28 17:17

import  pygame

pygame.init()
# 创建游戏窗口  480*700

screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 1. 加载图像数据
bg = pygame.image.load("./images/background.png")

# 2.调用blit方法将图像绘制到指定位置
screen.blit(bg, (0, 0))

# 3.update更新屏幕显示
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200,500))
pygame.display.update()


while True:
    pass


pygame.quit()