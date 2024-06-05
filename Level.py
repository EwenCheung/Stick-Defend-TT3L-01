import pygame
from sys import exit
import importlib
from Firebase import firebase
from Stick_of_War import stick_of_war

pygame.init()
pygame.font.init()


class GameLevel:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Choose Level')
        
        self.wood_plank_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.wood_plank_surface = pygame.transform.scale(self.wood_plank_surface, (100, 120))
        self.wood_plank_surface_back_and_store = pygame.transform.scale(self.wood_plank_surface, (90,50))

        self.lock = pygame.image.load('War of stick/Picture/utils/lock.png')
        self.lock_surf = pygame.transform.scale(self.lock, ( 100, 100))

        self.no_star = pygame.image.load('War of stick/Picture/utils/no_star.png')
        self.no_star_surf = pygame.transform.scale(self.no_star, (90, 40))

        self.one_star = pygame.image.load('War of stick/Picture/utils/one_star.png')
        self.one_star_surf = pygame.transform.scale(self.one_star, (90, 40))

        self.two_star = pygame.image.load('War of stick/Picture/utils/two_star.png')
        self.two_star_surf = pygame.transform.scale(self.two_star, (90, 40))

        self.three_star = pygame.image.load('War of stick/Picture/utils/three_star.png')
        self.three_star_surf = pygame.transform.scale(self.three_star, (90, 40))

        self.level_bg = pygame.image.load('War of stick/Picture/utils/choose level.png')

        self.level_select_music = pygame.mixer.Sound('War of stick/Music/level.mp3')
        self.level_select_music.set_volume(0.2)
        self.level_select_music.play(loops=-1)

        # star rect for all level
        # level one
        self.no_star_one_rect = self.no_star_surf.get_rect(center=(180, 290))
        self.one_star_one_rect = self.one_star_surf.get_rect(center=(180, 290))
        self.two_star_one_rect = self.two_star_surf.get_rect(center=(180, 290)) #470
        self.three_star_one_rect = self.three_star_surf.get_rect(center=(180, 290))

        # level two
        self.no_star_two_rect = self.no_star_surf.get_rect(center=(335, 290))
        self.one_star_two_rect = self.one_star_surf.get_rect(center=(335, 290))
        self.two_star_two_rect = self.two_star_surf.get_rect(center=(335, 290))
        self.three_star_two_rect = self.three_star_surf.get_rect(center=(335, 290))

        # level three
        self.no_star_three_rect = self.no_star_surf.get_rect(center=(495, 290))
        self.one_star_three_rect = self.one_star_surf.get_rect(center=(495, 290))
        self.two_star_three_rect = self.two_star_surf.get_rect(center=(495, 290))
        self.three_star_three_rect = self.three_star_surf.get_rect(center=(495, 290))

        # level four
        self.no_star_four_rect = self.no_star_surf.get_rect(center=(650, 290))
        self.one_star_four_rect = self.one_star_surf.get_rect(center=(650, 290))
        self.two_star_four_rect = self.two_star_surf.get_rect(center=(650, 290))
        self.three_star_four_rect = self.three_star_surf.get_rect(center=(650, 290))

        # level five
        self.no_star_five_rect = self.no_star_surf.get_rect(center=(805, 290))
        self.one_star_five_rect = self.one_star_surf.get_rect(center=(805, 290))
        self.two_star_five_rect = self.two_star_surf.get_rect(center=(805, 290))
        self.three_star_five_rect = self.three_star_surf.get_rect(center=(805, 290))

        # level six
        self.no_star_six_rect = self.no_star_surf.get_rect(center=(180, 470))
        self.one_star_six_rect = self.one_star_surf.get_rect(center=(180, 470))
        self.two_star_six_rect = self.two_star_surf.get_rect(center=(180, 470))
        self.three_star_six_rect = self.three_star_surf.get_rect(center=(180, 470))

        # level seven
        self.no_star_seven_rect = self.no_star_surf.get_rect(center=(335, 470))
        self.one_star_seven_rect = self.one_star_surf.get_rect(center=(335, 470))
        self.two_star_seven_rect = self.two_star_surf.get_rect(center=(335, 470))
        self.three_star_seven_rect = self.three_star_surf.get_rect(center=(335, 470))

        # level eight
        self.no_star_eight_rect = self.no_star_surf.get_rect(center=(495, 470))
        self.one_star_eight_rect = self.one_star_surf.get_rect(center=(495, 470))
        self.two_star_eight_rect = self.two_star_surf.get_rect(center=(495, 470))
        self.three_star_eight_rect = self.three_star_surf.get_rect(center=(495, 470))

        # level nine
        self.no_star_nine_rect = self.no_star_surf.get_rect(center=(650, 470))
        self.one_star_nine_rect = self.one_star_surf.get_rect(center=(650, 470))
        self.two_star_nine_rect = self.two_star_surf.get_rect(center=(650, 470))
        self.three_star_nine_rect = self.three_star_surf.get_rect(center=(650, 470))

        # level ten
        self.no_star_ten_rect = self.no_star_surf.get_rect(center=(805, 470))
        self.one_star_ten_rect = self.one_star_surf.get_rect(center=(805, 470))
        self.two_star_ten_rect = self.two_star_surf.get_rect(center=(805, 470))
        self.three_star_ten_rect = self.three_star_surf.get_rect(center=(805, 470))

        self.level_one = [(self.no_star_surf, self.no_star_one_rect)]
        self.level_two = [(self.no_star_surf, self.no_star_two_rect)]
        self.level_three = [(self.no_star_surf, self.no_star_three_rect)]
        self.level_four = [(self.no_star_surf, self.no_star_four_rect)]
        self.level_five = [(self.no_star_surf, self.no_star_five_rect)]
        self.level_six = [(self.no_star_surf, self.no_star_six_rect)]
        self.level_seven = [(self.no_star_surf, self.no_star_seven_rect)]
        self.level_eight = [(self.no_star_surf, self.no_star_eight_rect)]
        self.level_nine = [(self.no_star_surf, self.no_star_nine_rect)]
        self.level_ten = [(self.no_star_surf, self.no_star_ten_rect)]

        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]

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
            self.achievement()
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
            self.achievement()
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
            self.achievement()
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
            self.achievement()
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
            self.achievement()
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
            self.achievement()
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
            self.achievement()
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
            self.achievement()

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
            self.achievement()

        elif firebase.stage_level == 10:
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
            self.achievement()

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.wood_plank_rectangle_store.collidepoint(pygame.mouse.get_pos()):
                    self.go_store_py()

                if self.wood_plank_rectangle_back.collidepoint(pygame.mouse.get_pos()):
                    self.go_home_py()

                if firebase.stage_level >=1:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
                        self.playing_lvl[0] = True
                        stick_of_war.run()
                        
                    
                if firebase.stage_level >= 2:
                    if self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
                        self.playing_lvl[1] = True
                        stick_of_war.run()


                if firebase.stage_level >= 3:
                    if self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
                        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
                        self.playing_lvl[2] = True
                        stick_of_war.run()

                if firebase.stage_level >= 4:
                    if self.wood_plank_rectangle_four.collidepoint(pygame.mouse.get_pos()):
                        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
                        self.playing_lvl[3] = True
                        stick_of_war.run()                    

                if firebase.stage_level >= 5:
                    if self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
                        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
                        self.playing_lvl[4] = True
                        stick_of_war.run()

                if firebase.stage_level >= 6:
                    if self.wood_plank_rectangle_six.collidepoint(pygame.mouse.get_pos()):
                        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
                        self.playing_lvl[5] = True
                        stick_of_war.run()

                if firebase.stage_level >= 7:
                    if self.wood_plank_rectangle_seven.collidepoint(pygame.mouse.get_pos()):
                        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
                        self.playing_lvl[6] = True
                        stick_of_war.run()

                if firebase.stage_level >= 8:
                    if self.wood_plank_rectangle_eight.collidepoint(pygame.mouse.get_pos()):
                        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
                        self.playing_lvl[7] = True
                        stick_of_war.run()

                if firebase.stage_level >= 9:
                    if self.wood_plank_rectangle_nine.collidepoint(pygame.mouse.get_pos()):
                        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
                        self.playing_lvl[8] = True
                        stick_of_war.run()

                if firebase.stage_level >= 10:     
                    if self.wood_plank_rectangle_ten.collidepoint(pygame.mouse.get_pos()):
                        self.playing_lvl = [False,False,False,False,False,False,False,False,False,False]
                        self.playing_lvl[9] = True
                        stick_of_war.run()

    def go_store_py(self):
        self.level_select_music.stop()
        store_module = importlib.import_module("Store")
        game_store = store_module.Game_Store()
        game_store.run()
        exit()

    def go_home_py(self):
        self.level_select_music.stop()
        pygame.quit()  # Cleanup before switching
        importlib.invalidate_caches()  # Clear any cached importlib entries
        home_module = importlib.import_module("Home")
        go_home = home_module.GameHome()
        go_home.run()
        exit()

    def achievement(self):
        stick_of_war.check_game_over()
        if stick_of_war.winner == "User":
            if firebase.stage_level >= 1:
                if self.playing_lvl[0] == True:
                    if 0 <= stick_of_war.elapsed_time_seconds <= 2:
                        self.level_one =[(self.three_star_surf, self.three_star_one_rect)]
                        
                    elif 2 < stick_of_war.elapsed_time_seconds <= 4:
                        self.level_one = [(self.two_star_surf, self.two_star_one_rect)]
                        
                    elif stick_of_war.elapsed_time_seconds > 4:
                        self.level_one = [(self.one_star_surf, self.one_star_one_rect)]
                    print("hi")
                    print(self.level_one)
                    self.playing_lvl[0] = False
                    
                for star in self.level_one:
                    self.screen.blit(star[0], star[1])

            if firebase.stage_level >= 2:
                if self.playing_lvl[1] == True:
                    
                    if 0 <= stick_of_war.elapsed_time_seconds <= 2:
                        self.level_two = [(self.three_star_surf, self.three_star_two_rect)]
                        
                    elif 2 < stick_of_war.elapsed_time_seconds <= 4:
                        self.level_two = [(self.two_star_surf, self.two_star_two_rect)]

                    elif stick_of_war.elapsed_time_seconds > 4:
                        self.level_two = [(self.one_star_surf, self.one_star_two_rect)] 

                    self.playing_lvl[1] = False
                for star in self.level_two:
                    self.screen.blit(star[0], star[1])

            if firebase.stage_level >= 3:
                if self.playing_lvl[2] == True:
                    if 0 <= stick_of_war.elapsed_time_seconds <= 2:
                        self.level_three = [(self.three_star_surf, self.three_star_three_rect)]

                    elif 2 < stick_of_war.elapsed_time_seconds <= 4:
                        self.level_three = [(self.two_star_surf, self.two_star_three_rect)]

                    elif stick_of_war.elapsed_time_seconds > 4:
                        self.level_three = [(self.one_star_surf, self.one_star_three_rect)]

                    self.playing_lvl[2] = False
                for star in self.level_three:
                    self.screen.blit(star[0], star[1])

            if firebase.stage_level >= 4:
                if self.playing_lvl[3] == True:
                    if 0 <= stick_of_war.elapsed_time_seconds <= 2:
                        self.level_four = [(self.three_star_surf, self.three_star_four_rect)]

                    elif 2 < stick_of_war.elapsed_time_seconds <= 4:
                        self.level_four = [(self.two_star_surf, self.two_star_four_rect)] 

                    elif stick_of_war.elapsed_time_seconds > 4:
                        self.level_four = [(self.one_star_surf, self.one_star_four_rect)]

                    self.playing_lvl[3] = False

                for star in self.level_four:
                    self.screen.blit(star[0], star[1])

            if firebase.stage_level >= 5:
                if self.playing_lvl[4] == True:
                    if 0 <= stick_of_war.elapsed_time_seconds <= 2:
                        self.level_five = [(self.three_star_surf, self.three_star_five_rect)]

                    elif 2 < stick_of_war.elapsed_time_seconds <= 4:
                        self.level_five = [(self.two_star_surf, self.two_star_five_rect)]

                    elif stick_of_war.elapsed_time_seconds > 4:
                        self.level_five = [(self.one_star_surf, self.one_star_five_rect)]

                    self.playing_lvl[4] = False
                for star in self.level_five:
                    self.screen.blit(star[0], star[1])

            if firebase.stage_level >= 6:
                if self.playing_lvl[5] == True:
                    if 0 <= stick_of_war.elapsed_time_seconds <= 2:
                        self.level_six = [(self.three_star_surf, self.three_star_six_rect)]

                    elif 2 < stick_of_war.elapsed_time_seconds <= 4:
                        self.level_six = [(self.two_star_surf, self.two_star_six_rect)]

                    elif stick_of_war.elapsed_time_seconds >= 4:
                        self.level_six = [(self.one_star_surf, self.one_star_six_rect)] 

                    self.playing_lvl[5] = False
                for star in self.level_six:
                    self.screen.blit(star[0], star[1])

            if firebase.stage_level >= 7:
                if self.playing_lvl[6] == True:
                    if 0 <= stick_of_war.elapsed_time_seconds <= 2:
                        self.level_seven = [(self.three_star_surf, self.three_star_seven_rect)]

                    elif 2 < stick_of_war.elapsed_time_seconds <= 4:
                        self.level_seven = [(self.two_star_surf, self.two_star_seven_rect)]

                    elif stick_of_war.elapsed_time_seconds >= 4:
                        self.level_seven = [(self.one_star_surf, self.one_star_seven_rect)]

                    self.playing_lvl[6] = False
                for star in self.level_seven:
                    self.screen.blit(star[0], star[1])

            if firebase.stage_level >= 8:
                if self.playing_lvl[7] == True:
                    if 0 <= stick_of_war.elapsed_time_seconds <= 2:
                        self.level_eight = [(self.three_star_surf, self.three_star_eight_rect)]

                    elif 2 < stick_of_war.elapsed_time_seconds <= 4:
                        self.level_eight = [(self.two_star_surf, self.two_star_eight_rect)]

                    elif stick_of_war.elapsed_time_seconds >= 4:
                        self.level_eight.clear()
                        self.level_eight = [(self.one_star_surf, self.one_star_eight_rect)]

                    self.playing_lvl[7] = False
                for star in self.level_eight:
                    self.screen.blit(star[0], star[1])

            if firebase.stage_level >= 9:
                if self.playing_lvl[8] == True:
                    if 0 <= stick_of_war.elapsed_time_seconds <= 2:
                        self.level_nine = [(self.three_star_surf, self.three_star_nine_rect)]

                    elif 2 < stick_of_war.elapsed_time_seconds <= 4:
                        self.level_nine = [(self.two_star_surf, self.two_star_nine_rect)] 

                    elif stick_of_war.elapsed_time_seconds > 4:
                        self.level_nine = [(self.one_star_surf, self.one_star_nine_rect)]

                    self.playing_lvl[8] = False
                for star in self.level_nine:
                    self.screen.blit(star[0], star[1])

            if firebase.stage_level >= 10:
                if self.playing_lvl[9] == True:
                    if 0 <= stick_of_war.elapsed_time_seconds <= 2:
                        self.level_ten = [(self.three_star_surf, self.three_star_ten_rect)]

                    elif 2 < stick_of_war.elapsed_time_seconds <= 4:
                        self.level_ten = [(self.two_star_surf, self.two_star_ten_rect)]

                    elif stick_of_war.elapsed_time_seconds > 4:  
                        self.level_ten = [(self.one_star_surf, self.one_star_ten_rect)]

                    self.playing_lvl[9] = False
                for star in self.level_ten:
                    self.screen.blit(star[0], star[1])

        elif stick_of_war.winner == "Enemy" or pygame.init:
            if firebase.stage_level >= 1:
                for star in self.level_one:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 2:
                for star in self.level_two:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 3:
                for star in self.level_three:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 4:
                for star in self.level_four:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 5:
                for star in self.level_five:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 6:
                for star in self.level_six:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 7:
                for star in self.level_seven:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 8:
                for star in self.level_eight:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 9:
                for star in self.level_nine:
                    self.screen.blit(star[0], star[1])
            if firebase.stage_level >= 10:
                for star in self.level_ten:
                    self.screen.blit(star[0], star[1])

                
    def run(self):
        while True:
            self.screen.fill((255, 255, 255))

            self.event_handling()

            self.choose_level()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    GameLevel().run()

level = GameLevel()
