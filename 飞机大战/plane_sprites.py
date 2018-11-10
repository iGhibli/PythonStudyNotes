import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 852)


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵"""

    def __init__(self, image_name, speed=1, origin=(0, 0)):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = pygame.Rect(origin[0], origin[1], self.image.get_rect().width, self.image.get_rect().height)
        self.speed = speed

    def update(self):

        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def update(self):
        # 1. 调用父类的方法实现
        super().update()

        # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -self.rect.height
