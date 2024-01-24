import pygame
from random import randint

class Meteorite(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.meteorite = ['Image/meteorit_blue.png', 'Image/meteorit_yellow.png']
        image_meteorite = pygame.image.load(self.meteorite[randint(0, 1)]).convert_alpha()
        self.image_meteorite = image_meteorite

        self.WIDTH = self.screen.get_width() - 200  # Ширина
        self.HEIGHT = self.WIDTH // 1.7777777777777777

        self.image_meteorite = pygame.transform.smoothscale(self.image_meteorite,  # Уменьшение изображения
                                                            (70, 70))
        self.rect = self.image_meteorite.get_rect()  # Представление изображение как прямоугольник
        self.screen_rect = screen.get_rect()  # объект экрана

        """Расположение метеорита"""
        self.rect.centerx = randint(0, self.WIDTH - 30)
        self.rect.centery = self.screen_rect.top - 50  # верх, за экран

        self.speed_range = 6   # Для увеличение ускорости с течением времени
        self.speed = randint(self.speed_range-5, self.speed_range)  # случайныя скорость
        self.direction = randint(-2, 2)     # Направление

    def movement(self):
        self.rect.centery += self.speed
        self.rect.centerx -= self.direction

    def screen_met(self):
        """Вывод"""
        self.screen.blit(self.image_meteorite, self.rect)
