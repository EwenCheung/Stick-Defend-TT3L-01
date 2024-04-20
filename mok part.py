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
        self.num_gold = 500
        self.num_diamond = 50
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

        #Currency for Gold
        self.pic_gold = pygame.image.load('Picture/gold.png').convert_alpha()
        self.pic_gold_surf = pygame.transform.scale(self.pic_gold,(25,25))
        self.pic_gold_rect = self.pic_gold_surf.get_rect(center=(760,50))


        self.num_gold_font = pygame.font.Font(None,30)
        self.num_gold_surf = self.num_gold_font.render(str(self.num_gold), True, 'Black')
        self.num_gold_rect = self.num_gold_surf.get_rect(center=(800,50))

        #Currency for diamond
        self.pic_diamond = pygame.image.load('Picture/diamond .png').convert_alpha()
        self.pic_diamond_surf = pygame.transform.scale(self.pic_diamond,(50,25))
        self.pic_diamond_rect = self.pic_diamond_surf.get_rect(center=(760,80))

        self.num_diamond_font = pygame.font.Font(None,30)
        self.num_diamond_surf = self.num_diamond_font.render(str(self.num_diamond), True, 'Black')
        self.num_diamond_rect = self.num_diamond_surf.get_rect(center=(800,80))


    def game_start(self):
        self.screen.blit(self.background_image, (self.bg_x, 0))

        self.screen.blit(self.pic_gold_surf,self.pic_gold_rect)
        self.screen.blit(self.num_gold_surf,self.num_gold_rect)

        self.screen.blit(self.pic_diamond_surf,self.pic_diamond_rect)
        self.screen.blit(self.num_diamond_surf,self.num_diamond_rect)

    def run(self):
        while True:
            self.screen.fill((255, 255, 255))  # Clear screen

            self.event_handling()
            self.game_start()

            pygame.display.update()  # Update the display
            self.clock.tick(60)  # Limit frame rate to 60 FPS




if __name__ == "__main__":
    Game().run()
