import pygame
from sys import exit

pygame.init()

class StartButton():
    pass

class LoadingBar():
    def __init__(self, x, y, height, width, colour, border_colour, border_width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour
        self.border_colour = border_colour
        self.border_width = border_width
        self.progress = 0 # the first progress variable is to calculate how much should it be filled in
                          # if remove that the loading bar wont work

    def draw_bar(self, screen):
        pygame.draw.rect(screen, self.border_colour, (self.x - self.border_width, self.y - self.border_width, self.width + 2*self.border_width, self.height + 2*self.border_width))
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width * self.progress, self.height))

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption('Home Page')
        self.loading_bar = LoadingBar(400, 500, 30, 200, (255, 255, 224), (0, 0, 0), 2)  # Fixed width initialization
        self.progress = 0  # this one is if i put 0.2 it will start the loading bar from 0.2

        self.set_up()

    def set_up(self):
        self.image = pygame.image.load("War of stick/Picture/utlis/background_photo.jpg")  # Replace "home_image.jpg" with your image path
        self.image_rect = self.image.get_rect(center=(1000 // 2, 600 // 2))

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def game_start(self):
        self.screen.blit(self.image, self.image_rect)
        self.loading_bar.draw_bar(self.screen)

    def update_progress(self):
        # Simulating loading progress
        self.progress += 0.005
        if self.progress >= 1:
            self.progress = 1

        self.loading_bar.progress = self.progress

    def run(self):
        while True:
            self.screen.fill((255, 255, 255))

            self.event_handling()
            self.game_start()
            self.update_progress()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    Game().run()


