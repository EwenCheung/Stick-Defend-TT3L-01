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
        self.currency = 500

    def set_up(self):
        # Scrolling Background
        self.background_image = pygame.image.load('War of stick/map_bg.jpg')

        # Troop One
        self.troop_one_image = pygame.image.load('War of stick/background_photo.jpg')
        self.troop_one_image = pygame.transform.scale(self.troop_one_image, (100,100))
        self.troop_one_button = Button(self.troop_one_image, (50, 50), (100, 100))

         # Troop Two
        self.troop_two_image = pygame.image.load('War of stick/background_photo.jpg')
        self.troop_two_image = pygame.transform.scale(self.troop_two_image, (100,100))
        self.troop_two_button = Button(self.troop_two_image, (50, 50), (200, 100))    

        # Troop Three
        self.troop_three_image = pygame.image.load('War of stick/background_photo.jpg')
        self.troop_three_image = pygame.transform.scale(self.troop_three_image, (100,100))
        self.troop_three_button = Button(self.troop_three_image, (50, 50), (300, 100))

         # Troop Four
        self.troop_four_image = pygame.image.load('War of stick/background_photo.jpg')
        self.troop_four_image = pygame.transform.scale(self.troop_four_image, (100,100))
        self.troop_four_button = Button(self.troop_four_image, (50, 50), (400, 100))   

         # Troop Five
        self.troop_five_image = pygame.image.load('War of stick/background_photo.jpg')
        self.troop_five_image = pygame.transform.scale(self.troop_five_image, (100,100))
        self.troop_five_button = Button(self.troop_five_image, (50, 50), (500, 100))    

    def event_handling(self):
        clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check if left mouse button is pressed
                    clicked = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.bg_x += self.scroll_speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.bg_x -= self.scroll_speed

        self.bg_x = max(self.bg_x, 1000 - self.background_image.get_width())
        self.bg_x = min(self.bg_x, 0)

        # Check if the left mouse button was clicked and handle accordingly
        if clicked:
            mouse_pos = pygame.mouse.get_pos()
            if self.troop_one_button.is_clicked(mouse_pos):
                if self.currency >= 50:
                    self.currency -= 50
                    self.show_background = True  # Set flag to show background image
        self.troop_one_button.reset()   # Reset the button to make it make to the size i set

        if clicked:
            if self.troop_two_button.is_clicked(mouse_pos):
                if self.currency >= 50:
                    self.currency -= 50
                    self.show_background = True  # Set flag to show background image
        self.troop_two_button.reset()

        if clicked:
            if self.troop_three_button.is_clicked(mouse_pos):
                if self.currency >= 50:
                    self.currency -= 50
                    self.show_background = True  # Set flag to show background image
        self.troop_three_button.reset()    

        if clicked:
            if self.troop_four_button.is_clicked(mouse_pos):
                if self.currency >= 50:
                    self.currency -= 50
                    self.show_background = True  # Set flag to show background image
        self.troop_four_button.reset()

        if clicked:
            if self.troop_five_button.is_clicked(mouse_pos):
                if self.currency >= 50:
                    self.currency -= 50
                    self.show_background = True  # Set flag to show background image
        self.troop_five_button.reset()

    def game_start(self):
        self.screen.fill((255, 255, 255))  # Clear screen
        self.screen.blit(self.background_image, (self.bg_x, 0))

        if self.show_background:
            self.screen.blit(self.troop_one_image, (100, 100))  # Blit army on the screen

        if self.show_background:
            self.screen.blit(self.troop_two_image, (200, 100))  # Blit army on the screen

        if self.show_background:
            self.screen.blit(self.troop_three_image, (300, 100))  # Blit army on the screen

        if self.show_background:
            self.screen.blit(self.troop_four_image, (400, 100))  # Blit army on the screen

        if self.show_background:
            self.screen.blit(self.troop_five_image, (500, 100))  # Blit army on the screen


        self.troop_one_button.draw(self.screen)
        self.troop_two_button.draw(self.screen)
        self.troop_three_button.draw(self.screen)
        self.troop_four_button.draw(self.screen)
        self.troop_five_button.draw(self.screen)

        font = pygame.font.Font(None, 36)
        currency_text = f"Currency = {self.currency}"
        currency_text = font.render(currency_text, True, (0, 0, 0))
        self.screen.blit(currency_text, (10, 10))  # Display currency at top left corner

    def run(self):
        while True:
            self.event_handling()
            self.game_start()

            pygame.display.update()  # Update the display
            self.clock.tick(60)  # Limit frame rate to 60 FPS

if __name__ == "__main__":
    Game().run()

