import pygame
import random


class Bonuses(pygame.sprite.Sprite):
    def __init__(self, screen, image_coins):
        super(Bonuses, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(image_coins).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

        self.WIDTH = self.screen.get_width() - 200  # Use the screen parameter to get the screen width
        self.HEIGHT = self.WIDTH // 1.7777777777777777

        self.rect.x = random.randrange(30, self.WIDTH - 30)
        self.rect.y = 0
        self.speed = random.randint(1, 7)

    def kill_coins(self):
        self.kill()

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom > self.HEIGHT:
            self.kill()
