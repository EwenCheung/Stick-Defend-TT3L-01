import pygame
from sys import exit
import importlib
from Firebase import firebase

pygame.init()
pygame.font.init()


class GameLevel:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Choose Level')
        self.begin_time = pygame.time.get_ticks()

        self.wood_plank_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.wood_plank_surface = pygame.transform.scale(self.wood_plank_surface, (100, 120))
        self.wood_plank_surface_back_and_store = pygame.transform.scale(self.wood_plank_surface, (90, 50))
        self.lock = pygame.image.load('War of stick/Picture/utils/lock.png')
        self.lock_surf = pygame.transform.scale(self.lock, (100, 100))
        self.level_bg = pygame.image.load('War of stick/Picture/utils/choose level.png')

        self.level_select_music = pygame.mixer.Sound('War of stick/Music/level.mp3')
        self.level_select_music.set_volume(0.2)
        self.level_select_music.play(loops=-1)

    def choose_level(self):
        self.wood_plank_rectangle_back = self.wood_plank_surface.get_rect(center=(115, 100))

        self.wood_plank_rectangle_store = self.wood_plank_surface.get_rect(center=(890, 100))

        self.wood_plank_rectangle_one = self.wood_plank_surface.get_rect(center=(180, 230))

        self.wood_plank_rectangle_two = self.wood_plank_surface.get_rect(center=(335, 230))
        self.lock_two_rect = self.lock_surf.get_rect(center=(335, 230))

        self.wood_plank_rectangle_three = self.wood_plank_surface.get_rect(center=(495, 230))
        self.lock_three_rect = self.lock_surf.get_rect(center=(495, 230))

        self.wood_plank_rectangle_four = self.wood_plank_surface.get_rect(center=(650, 230))
        self.lock_four_rect = self.lock_surf.get_rect(center=(650, 230))

        self.wood_plank_rectangle_five = self.wood_plank_surface.get_rect(center=(805, 230))
        self.lock_five_rect = self.lock_surf.get_rect(center=(805, 230))

        self.wood_plank_rectangle_six = self.wood_plank_surface.get_rect(center=(180, 410))
        self.lock_six_rect = self.lock_surf.get_rect(center=(180, 410))

        self.wood_plank_rectangle_seven = self.wood_plank_surface.get_rect(center=(335, 410))
        self.lock_seven_rect = self.lock_surf.get_rect(center=(335, 410))

        self.wood_plank_rectangle_eight = self.wood_plank_surface.get_rect(center=(495, 410))
        self.lock_eight_rect = self.lock_surf.get_rect(center=(495, 410))

        self.wood_plank_rectangle_nine = self.wood_plank_surface.get_rect(center=(650, 410))
        self.lock_nine_rect = self.lock_surf.get_rect(center=(650, 410))

        self.wood_plank_rectangle_ten = self.wood_plank_surface.get_rect(center=(805, 410))
        self.lock_ten_rect = self.lock_surf.get_rect(center=(805, 410))

        if firebase.stage_level == 1:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_two_rect)
            self.screen.blit(self.lock_surf, self.lock_three_rect)
            self.screen.blit(self.lock_surf, self.lock_four_rect)
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
        elif firebase.stage_level == 2:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_three_rect)
            self.screen.blit(self.lock_surf, self.lock_four_rect)
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
        elif firebase.stage_level == 3:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_four_rect)
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
        elif firebase.stage_level == 4:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
        elif firebase.stage_level == 5:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
        elif firebase.stage_level == 6:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
        elif firebase.stage_level == 7:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
        elif firebase.stage_level == 8:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
        elif firebase.stage_level == 9:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_nine)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
        else:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_nine)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_ten)
            self.screen.blit(self.level_bg, (0, 0))

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.wood_plank_rectangle_store.collidepoint(pygame.mouse.get_pos()):
                    self.go_store_py()
                elif self.wood_plank_rectangle_back.collidepoint(pygame.mouse.get_pos()):
                    self.go_home_py()

                if firebase.stage_level == 1:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()

                elif firebase.stage_level == 2:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()

                elif firebase.stage_level == 3:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()

                elif firebase.stage_level == 4:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_four.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()

                elif firebase.stage_level == 5:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_four.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()

                elif firebase.stage_level == 6:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_four.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_six.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()

                elif firebase.stage_level == 7:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_four.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_seven.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()

                elif firebase.stage_level == 8:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_four.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_seven.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_eight.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()

                elif firebase.stage_level == 9:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_four.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_seven.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_eight.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_nine.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()

                elif firebase.stage_level == 9:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_four.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_seven.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_eight.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_nine.collidepoint(pygame.mouse.get_pos()):
                        self.go_stick_war_py()
                    elif self.wood_plank_rectangle_ten.collidepoint(pygame.mouse.get_pos()):
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
