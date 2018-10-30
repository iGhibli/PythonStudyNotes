import pygame

pygame.init()

screen = pygame.display.set_mode((480, 852))

bg = pygame.image.load("./image/background.png").convert()
screen.blit(bg, (0, 0))

hero = pygame.image.load("./image/hero1.png")
screen.blit(hero, (200, 500))

pygame.display.update()


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

pygame.quit()
