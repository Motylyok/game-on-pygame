import pygame


class Character:

    def __init__(self, screen):

        self.screen = screen  # Экран
        self.image_character = pygame.image.load('Image/character.png')  # Загрузка изображения в проект

        self.WIDTH = screen.get_width() - 200  # Ширина
        self.HEIGHT = self.WIDTH // 1.7777777777777777

        self.image_character = pygame.transform.smoothscale(self.image_character,  # Уменьшение изображения
                                                            (self.WIDTH // 19.2, self.HEIGHT // 18))
        self.rect = self.image_character.get_rect()  # Представление изображение как прямоугольник
        self.screen_rect = screen.get_rect()  # объект экрана

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.slowing_speed = False
        self.speed = 10
        self.speed_y = self.speed
        self.speed_x = self.speed

        # Keyboard input attributes
        self.key_d = False
        self.key_a = False
        self.key_s = False
        self.key_w = False

        # Slowing attributes
        self.slowing_d = False
        self.slowing_a = False
        self.slowing_w = False
        self.slowing_s = False

    def conclusion(self):
        """Вывод игрока"""
        self.screen.blit(self.image_character, self.rect)

    def movement(self):

        """Замедление игрока"""
        if self.slowing_speed:
            self.slowing_d = False
            self.slowing_a = False
            self.slowing_w = False
            self.slowing_s = False
            self.speed_x = 5
            self.speed_y = 5

        """Передвижение"""
        if self.key_a:
            self.rect.centerx -= self.speed_x
            self.speed_x += 0.5

        if self.key_d:
            self.rect.centerx += self.speed_x
            self.speed_x += 0.5

        if self.key_w:
            self.rect.centery -= self.speed_y
            self.speed_y += 0.5

        if self.key_s:
            self.rect.centery += self.speed_y
            self.speed_y += 0.5

        """Ускорение торможения"""
        if self.slowing_d:
            self.speed_x -= 0.5
            self.rect.centerx += self.speed_x

            if self.speed_x <= 0:
                self.slowing_d = False
                self.speed_x = self.speed

        if self.slowing_a:
            self.speed_x -= 0.5
            self.rect.centerx -= self.speed_x

            if self.speed_x <= 0:
                self.slowing_a = False
                self.speed_x = self.speed

        if self.slowing_w:
            self.speed_y -= 0.5
            self.rect.centery -= self.speed_y

            if self.speed_y <= 0:
                self.slowing_w = False
                self.speed_y = self.speed

        if self.slowing_s:
            self.speed_y -= 0.5
            self.rect.centery += self.speed_y

            if self.speed_y <= 0:
                self.slowing_s = False
                self.speed_y = self.speed

        """ Обнуление усокрение торможение, если движение направленно в противоположную сторону """
        if self.key_d or self.key_a or self.key_w or self.key_s:

            if self.key_d:
                self.slowing_a = False

            if self.key_a:
                self.slowing_d = False

            if self.key_w:
                self.slowing_s = False

            if self.key_s:
                self.slowing_w = False
