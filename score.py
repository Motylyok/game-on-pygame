import pygame


class Score:
    def __init__(self, screen, time, max_score):
        self.screen = screen
        self.time = time
        self.max_score = max_score

        f1 = pygame.font.Font('ttf/my_font.ttf', 20)
        count = int(int(time) // 3)

        score = f1.render(f"SCORE: {count}   MAX_SCORE {self.max_score}", 1, (180, 0, 0))
        self.score = score

    def conclusion_score(self):
        """Вывод"""
        self.screen.blit(self.score, (10, 10))
