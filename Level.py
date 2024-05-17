import pygame
from sys import exit
import importlib
pygame.init()

class GameLevel:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Choose Level')

        self.wood_plank_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.wood_plank_surface = pygame.transform.scale(self.wood_plank_surface, (140, 50))


    def choose_level(self):
        wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(350, 430))
        self.screen.blit(self.wood_plank_surface, wood_plank_rectangle)
        back_choose_game = pygame.font.Font(None, 40).render('Back to Choose Game', True, (255, 255, 255))
        self.back_choose_game_rect = back_choose_game.get_rect(center=(350, 430))
        self.screen.blit(back_choose_game,self.back_choose_game_rect)

        wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(650, 430))
        self.screen.blit(self.wood_plank_surface, wood_plank_rectangle)
        store = pygame.font.Font(None, 40).render("Store", True, (255, 255, 255))
        self.store_rect = store.get_rect(center=(650, 430))
        self.screen.blit(store, self.store_rect)

        wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(500, 200))
        self.screen.blit(self.wood_plank_surface, wood_plank_rectangle)
        level_1= pygame.font.Font(None, 40).render("level 1", True, (255, 255, 255))
        self.level_1_rect = level_1.get_rect(center=(500, 200))
        self.screen.blit(level_1, self.level_1_rect)


    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.store_rect.collidepoint(pygame.mouse.get_pos()):
                    self.go_store_py()
                elif self.back_choose_game_rect.collidepoint(pygame.mouse.get_pos()):
                    self.go_home_py()
                elif self.level_1_rect.collidepoint(pygame.mouse.get_pos()):
                    self.go_stick_war_py()

    def go_store_py(self):
        store_module = importlib.import_module("Store")
        game_store = store_module.Game_Store()
        game_store.run()
        exit()

    def go_home_py(self):
        pygame.quit()  # Cleanup before switching
        importlib.invalidate_caches()  # Clear any cached importlib entries
        home_module = importlib.import_module("Home")
        go_home = home_module.GameHome()
        go_home.run()
        exit()

    def go_stick_war_py(self):
        stick_of_war_module = importlib.import_module("Stick_of_War")
        game_stick_of_war = stick_of_war_module.GameStickOfWar()
        game_stick_of_war.run()
        exit()

    def run(self):
        while True:
            self.screen.fill((255, 255, 255))

            self.event_handling()

            self.choose_level()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    GameLevel().run()
