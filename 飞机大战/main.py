import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""
    def __init__(self):
        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 4. 设置定时器事件 - 创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

    def start_game(self):
        """游戏开始"""
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新、绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

            pass

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    @staticmethod
    def __game_over():
        """游戏结束"""
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()


"""
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
"""


