import pygame


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, menu_return: str, player_score: list[int]):
        pygame.mixer.music.load('asset/menu.wav')
        pygame.mixer.music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer.music.load('asset/menu.wav')
        pygame.mixer.music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame