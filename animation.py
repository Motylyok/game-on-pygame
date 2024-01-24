import pygame


def animation(character):
    image_path = 'Image/character.png'

    if character.key_d and not character.key_a:
        character.image_character = pygame.image.load('Image/character_right.png')

    elif character.key_a and not character.key_d:
        character.image_character = pygame.image.load('Image/character_left.png')

    else:
        character.image_character = pygame.image.load(image_path)

    character.image_character = pygame.transform.smoothscale(character.image_character,
                                                             (character.WIDTH // 19.2, character.HEIGHT // 18))
