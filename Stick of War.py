# coding: utf-8
import pygame
from sys import exit

pygame.init()

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Pokemon vs Naruto')  # title name
        self.screen = pygame.display.set_mode((1000, 600))
        self.bg_x = 0
        self.scroll_speed = 5
        self.set_up()  # Load the background image outside the loop

    def event_handling(self):
        # Event handling
        for event in pygame.event.get():
            # press 'x' to quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.bg_x += self.scroll_speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.bg_x -= self.scroll_speed

        self.bg_x = max(self.bg_x, 1000 - self.background_image.get_width())
        self.bg_x = min(self.bg_x, 0)

    def set_up(self):
        self.background_image = pygame.image.load('War of stick/map_bg.jpg')

    def game_start(self):
        self.screen.blit(self.background_image, (self.bg_x, 0))

    def run(self):
        while True:
            self.screen.fill((255, 255, 255))  # Clear screen

            self.event_handling()
            self.game_start()

            pygame.display.update()  # Update the display
            self.clock.tick(60)  # Limit frame rate to 60 FPS

if __name__ == "__main__":
    Game().run()
