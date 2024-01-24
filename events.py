import pygame
import sys
from meteorite import Meteorite


def events(character, my_event_id, enemies, screen):

    for event in pygame.event.get():
        """Закрытие окна"""
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        """Добавление спрайта, за определенное время"""
        if event.type == my_event_id:
            enemies.add(Meteorite(screen))

        """Если клавиша нажата"""
        if event.type == pygame.KEYDOWN:  # если не ровнятеся проигрышу

            if event.key == pygame.K_d:
                character.key_d = True

            if event.key == pygame.K_a:
                character.key_a = True

            if event.key == pygame.K_w:
                character.key_w = True

            if event.key == pygame.K_s:
                character.key_s = True

            if event.key == pygame.K_LSHIFT:
                character.slowing_speed = True

        """Если клавиша отжата"""
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_d:
                character.key_d = False
                character.slowing_d = True
                character.speed_x = character.speed

            if event.key == pygame.K_a:
                character.key_a = False
                character.slowing_a = True
                character.speed_x = character.speed

            if event.key == pygame.K_w:
                character.key_w = False
                character.slowing_w = True
                character.speed_y = character.speed

            if event.key == pygame.K_s:
                character.key_s = False
                character.slowing_s = True
                character.speed_y = character.speed

            if event.key == pygame.K_LSHIFT:
                character.slowing_speed = False



