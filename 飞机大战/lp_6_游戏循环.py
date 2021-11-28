# CDUT 罗澎
# 开发时间：2021/11/28 17:50

# CDUT 罗澎
# 开发时间：2021/11/28 17:17

import  pygame

# 游戏的初始化

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

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环： 游戏正式开始
i = 0
while True:

    # 时钟对象调用tick，可以指定循环体内部的代码执行的频率，帧
    clock.tick(60)
    print(i)
    i += 1
    pass

pygame.quit()