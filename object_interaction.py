import pygame
import sys


def border(character):
    """Телепортация из одной стороны в другую"""

    border = character.rect[2]//2.5     # На какое количество пикселей может зайти игрок за окно

    """Право-лево"""
    if character.screen_rect.right - character.rect.right < (-border) and (character.key_d or character.slowing_d):
        character.rect.centerx = character.screen_rect.left

    if character.rect.left < (-border) and (character.key_a or character.slowing_a):
        character.rect.centerx = character.screen_rect.right

    """Верх-низ"""
    if character.rect.top < (-border//1.5) and (character.key_w or character.slowing_w):
        character.rect.centery = character.screen_rect.bottom

    if character.screen_rect.bottom - character.rect.bottom < (-border//1.5) and (character.key_s or character.slowing_s):
        character.rect.centery = character.screen_rect.top


def conflict(character, met):
    """Проигрыш в случае столкновения"""
    if met.rect.centerx - 35 <= character.rect.centerx <= met.rect.centerx + 35:
        if met.rect.centery - 35 <= character.rect.centery <= met.rect.centery + 35:
            pygame.quit()
            sys.exit()


def collect_coins(character, coins):
    if coins.rect.centerx - 15 <= character.rect.centerx <= coins.rect.centerx + 15:
        if coins.rect.centery - 15 <= character.rect.centery <= coins.rect.centery + 15:
            return True
