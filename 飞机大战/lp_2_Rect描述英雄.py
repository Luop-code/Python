# CDUT 罗澎
# 开发时间：2021/11/28 17:09
import pygame

hero_rect =pygame.Rect(100,500,120,125)
print("英雄的原点：{} {} " .format(hero_rect.x, hero_rect.y))
print("英雄的尺寸：{} {} " .format(hero_rect.w, hero_rect.h))
print("{}" .format(hero_rect.size))