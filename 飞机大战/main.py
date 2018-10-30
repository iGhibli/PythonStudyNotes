import pygame

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


# 游戏循环
while True:
    # 指定循环体内部代码的执行频率
    clock.tick(60)

    # 改变飞机位置
    if hero_rect.y < 0:
        hero_rect.y += 6
    else:
        hero_rect.y -= 6

    # 绘制到屏幕
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 更新显示
    pygame.display.update()

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

pygame.quit()
