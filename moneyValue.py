import pygame


class MoneyValue:
    def __init__(self, screen, money_Values):
        self.screen = screen
        self.money_Values = money_Values

        f1 = pygame.font.Font('ttf/my_font.ttf', 20)

        moneyValues = f1.render(f"MONEY: {self.money_Values}", 1, (180, 0, 0))
        self.moneyValues = moneyValues

    def conclusion_moneyValue(self):
        """Вывод"""
        self.screen.blit(self.moneyValues, (10, 30))





