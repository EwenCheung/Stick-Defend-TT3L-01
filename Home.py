import pygame
from pygame.locals import *
from Stick_of_War import Game as StickGame, game_start as stick_game_start
from Pokemon_vs_Naruto import Game as PokemonGame, game_start as pokemon_game_start
from sys import exit


pygame.init()  

class LoadingBar:
    def __init__(self, x, y, height, width, colour, border_colour, border_width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour
        self.border_colour = border_colour
        self.border_width = border_width
        self.progress = 0  # the first progress variable is to calculate how much should it be filled in
        # if remove that the loading bar won't work

    def draw_bar(self, screen):
        pygame.draw.rect(screen, self.border_colour, (
            self.x - self.border_width, self.y - self.border_width, self.width + 2 * self.border_width,
            self.height + 2 * self.border_width))
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width * self.progress, self.height))


class Game_bg:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Home Page')
        self.loading_bar = LoadingBar(400, 500, 30, 200, (255, 255, 224), (0, 0, 0), 2)  # Fixed width initialization
        self.progress = 0  # this one is if I put 0.2 it will start the loading bar from 0.2

        self.image = pygame.image.load(
            "War of stick/Picture/utils/background_photo.jpg")  # Replace "home_image.jpg" with your image path
        self.image_rect = self.image.get_rect(center=(1000 // 2, 600 // 2))

        self.wood_plank_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.wood_plank_surface = pygame.transform.scale(self.wood_plank_surface, (140, 50))
        self.pokemon_vs_naruto_rect = None
        self.stick_of_war_rect = None

        self.loading = True
        self.finish_loading = False

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.stick_of_war_rect.collidepoint(pygame.mouse.get_pos()):
                    self.start_stick_of_war()  # Call a method to start Stick_of_war game
                elif self.pokemon_vs_naruto_rect.collidepoint(pygame.mouse.get_pos()):
                    self.start_pokemon_vs_naruto()  # Call a method to start Stick_of_war game

    def game_start_bg(self):
        self.screen.blit(self.image, self.image_rect)

    def update_progress(self):
        # Simulating loading progress

        if self.progress <= 1:
            self.progress += 0.005
            self.finish_loading = False

        else:
            self.progress = 1
            self.finish_loading = True
            self.loading = False

        self.loading_bar.progress = self.progress
        self.loading_bar.draw_bar(self.screen)

    def choose_game(self):
        wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(350, 430))
        self.screen.blit(self.wood_plank_surface, wood_plank_rectangle)
        pokemon_vs_naruto = pygame.font.Font(None, 40).render('Plant vs Zombie', True, (255, 255, 255))
        self.pokemon_vs_naruto_rect = pokemon_vs_naruto.get_rect(center=(350, 430))
        self.screen.blit(pokemon_vs_naruto, self.pokemon_vs_naruto_rect)

        wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(650, 430))
        self.screen.blit(self.wood_plank_surface, wood_plank_rectangle)
        stick_of_war = pygame.font.Font(None, 40).render("Stick of War", True, (255, 255, 255))
        self.stick_of_war_rect = stick_of_war.get_rect(center=(650, 430))
        self.screen.blit(stick_of_war, self.stick_of_war_rect)     

    def start_stick_of_war(self):
        pygame.quit()
        StickGame().stick_game_start()

    def start_pokemon_vs_naruto(self):
        pygame.quit()
        PokemonGame().pokemon_game_start()

    def run(self):
        while True:
            self.screen.fill((255, 255, 255))

            self.event_handling()
            self.game_start_bg()
            if self.loading:
                self.update_progress()
            elif self.finish_loading:
                self.choose_game()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    Game_bg().run()
