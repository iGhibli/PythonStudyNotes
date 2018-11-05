import pygame


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵"""

    def __init__(self, image_name, speed=1, origin=(0, 0)):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = pygame.Rect(origin[0], origin[1], self.image.get_rect().width, self.image.get_rect().height)
        self.speed = speed

    def update(self):

        self.rect.y += self.speed
