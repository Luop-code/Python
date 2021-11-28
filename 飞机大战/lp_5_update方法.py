# CDUT 罗澎
# 开发时间：2021/11/28 17:17

import  pygame

pygame.init()

# 创建游戏窗口  480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1. 加载图像数据
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200,500))

# 可以在所有绘制工作完成后，统一调用update
pygame.display.update()

while True:
    pass

pygame.quit()