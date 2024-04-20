import pygame
from sys import exit

pygame.init()

class Button:
    def __init__(self, image, size, position):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=position)
        self.clicked_image = pygame.transform.scale(image, (20, 20))  # Adjust size for clicked appearance
        self.clicked = False

    def draw(self, screen):
        if self.clicked:
            screen.blit(self.clicked_image, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.clicked = True
            return True
        return False

    def reset(self):
        self.clicked = False

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tower Defend')  # title name
        self.screen = pygame.display.set_mode((1000, 600))
        self.bg_x = 0
        self.scroll_speed = 5
        self.set_up()
        self.show_background = False  # Flag to control background image display

    def set_up(self):
        #this two part later mok done ready only i can proceed
        self.troop_one_image = pygame.image.load('War of stick/background_photo.jpg')
        self.troop_one_image = pygame.transform.scale(self.troop_one_image, (500,500))
        self.troop_one_button = Button(self.troop_one_image, (50, 50), (100, 100))
        self.background_image = pygame.image.load('War of stick/map_bg.jpg')

    def event_handling(self):
        for event in pygame.event.get():
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

        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.troop_one_button.is_clicked(mouse_pos):
                print("Troop One button clicked!")  # Add your button functionality here
                self.show_background = True  # Set flag to show background image
        self.troop_one_button.reset() # make sure the button doesnt become small when i press

    def game_start(self):
        self.screen.fill((255, 255, 255))  # Clear screen
        self.screen.blit(self.background_image, (self.bg_x, 0))

        if self.show_background:
            self.screen.blit(self.troop_one_image, (100, 100)) #blit army on the screen

        self.troop_one_button.draw(self.screen)

    def run(self):
        while True:
            self.event_handling()
            self.game_start()

            pygame.display.update()  # Update the display
            self.clock.tick(60)  # Limit frame rate to 60 FPS

if __name__ == "__main__":
    Game().run()