import pygame
from plane_sprites import *

# 初始化pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 852))

# 绘制背景图像
bg = pygame.image.load("./image/background.png").convert()
screen.blit(bg, (0, 0))

# 绘制英雄飞机
hero = pygame.image.load("./image/hero1.png")
screen.blit(hero, (200, 500))

# 刷新显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义飞机初始位置
hero_rect = pygame.Rect(190, 700, 100, 124)

# 创建游戏精灵
enemy1 = GameSprite("./image/enemy1.png", 2, (100, 100))
enemy2 = GameSprite("./image/enemy1.png", 3, (200, 100))
# 创建游戏精灵组
enemy_group = pygame.sprite.Group(enemy1, enemy2)


# 游戏循环
while True:

    # 设置屏幕刷新帧率
    clock.tick(60)

    # 事件监听
    for event in pygame.event.get():

        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()

            # 直接退出系统
            exit()

    # 改变飞机位置
    if hero_rect.y < 0:
        hero_rect.y += 6
    else:
        hero_rect.y -= 6

    # 绘制到屏幕
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)

    # 更新显示
    pygame.display.update()




