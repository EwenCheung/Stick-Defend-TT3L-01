# coding: utf-8

import pygame
from sys import exit

pygame.init()


class Game():
    def __init__(self):
        pygame.display.set_caption('Pokemon vs Naruto')  # title name
        self.screen = pygame.display.set_mode((1000, 600))
        self.bg_x = 0
        self.scroll_speed = 10

    def event_handling(self):
        # Event handling
        for event in pygame.event.get():
            # press 'x' to quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.bg_x += self.scroll_speed
            elif keys[pygame.K_d]:
                self.bg_x -= self.scroll_speed
            self.bg_x = max(self.bg_x, 1000 - self.background_image.get_width())
            self.bg_x = min(self.bg_x, 0)

    def set_up(self):
        self.background_image = pygame.image.load('War of stick/map_bg.jpg')

    def game_start(self):
        self.screen.blit(self.background_image, (self.bg_x, 0))

    def run(self):
        while True:

            self.set_up()
            # event_handling_control_function
            self.event_handling()

            self.game_start()

            pygame.display.flip()  # redraw the screen


if __name__ == "__main__":
    Game().run()
