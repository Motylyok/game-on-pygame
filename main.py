import pygame
import time
import json
import tkinter as tk
import events
from animation import animation
from object_interaction import border, conflict, collect_coins
import shutil
from bonuses import Bonuses
from score import Score
from moneyValue import MoneyValue
from meteorite import Meteorite
from character import Character

root = tk.Tk()
root.withdraw()

WIDTH = root.winfo_screenwidth() - 200
HEIGHT = WIDTH // 1.7777777777777777
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("did not invent")
clock = pygame.time.Clock()

background_image = pygame.image.load('image/Fon.png').convert_alpha()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

enemies = pygame.sprite.Group()
coinsGroup = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

time_meteorite = 400
my_event_id = pygame.USEREVENT + 1
pygame.time.set_timer(my_event_id, time_meteorite)
numbers_time = 10.0
numbers_time_for_money = 5.0

backup_file_path = "countALL_backup.txt"
shutil.copy2("countALL.txt", backup_file_path)

with open("countALL.txt", "r") as read_file:
    all_Info = json.load(read_file)

allValues = open('countALL.txt', 'w+')
allValues.write(json.dumps(all_Info))

start = time.time()


meteorite_instance = Meteorite(screen)
character_instance = Character(screen)
bonuses_instance = Bonuses(screen, 'image/coins.png')


while True:
    clock.tick(FPS)

    end = time.time()

    conclusion_score = Score(screen, end - start, all_Info['recordScore'])
    conclusion_score.conclusion_score()

    if int(int(end - start) // 3) > all_Info['recordScore']:
        allValues.seek(0)
        all_Info['recordScore'] = int(int(end - start) // 3)
        allValues.write(json.dumps(all_Info))

    coinsGroup.update()
    if end - start >= numbers_time_for_money:
        coin = Bonuses(screen, 'image/coins.png')
        coinsGroup.add(coin)  # type: ignore
        allsprites.add(coin)  # type: ignore
        numbers_time_for_money += 5
    allsprites.draw(screen)

    for coins in coinsGroup:
        if collect_coins(character_instance, coins):
            coins.kill_coins()
            allValues.seek(0)
            all_Info['moneyValue'] += 1
            allValues.write(json.dumps(all_Info))

    conclusion_moneyValue = MoneyValue(screen, all_Info['moneyValue'])
    conclusion_moneyValue.conclusion_moneyValue()

    for met in enemies:
        met.screen_met()
        met.movement()
        conflict(character_instance, met)

        if met.rect.centery >= met.screen_rect.bottom:
            met.kill()

        if end - start >= numbers_time:
            met.speed_range += 2 * (int(numbers_time) // 10)
            print(met.speed_range)
            if time_meteorite > 160:
                time_meteorite -= 20
                numbers_time += 10
                pygame.time.set_timer(my_event_id, time_meteorite)

    character_instance.conclusion()
    pygame.display.flip()
    pygame.display.update()

    events.events(character_instance, my_event_id, enemies, screen)
    character_instance.movement()
    border(character_instance)
    animation(character_instance)

    screen.blit(background_image, (0, 0))
