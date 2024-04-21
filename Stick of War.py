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

    # this function make sure that when i press the button, the button will become small and become normal size again
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
        self.num_gold = 500
        self.num_diamond = 50
        self.gold_time = pygame.time.get_ticks()
        self.diamond_time = pygame.time.get_ticks()
        self.gold_interval = 2000
        self.diamond_interval = 2000
        self.set_up()
        self.show_one_background = False  # Flag to control background image display
        self.show_two_background = False
        self.show_three_background = False
        self.show_four_background = False
        self.show_five_background = False

    def set_up(self):
        # Scrolling Background
        self.background_image = pygame.image.load('War of stick/map_bg.jpg')

        #Gold assets
        self.pic_gold = pygame.image.load('War of stick/background_photo.jpg').convert_alpha()
        self.pic_gold_surf = pygame.transform.scale(self.pic_gold,(25,25))
        self.pic_gold_rect = self.pic_gold_surf.get_rect(center=(760,50))

        self.num_gold_font = pygame.font.Font(None,30)
        self.num_gold_surf = self.num_gold_font.render(str(self.num_gold), True, 'Black')
        self.num_gold_rect = self.num_gold_surf.get_rect(center=(800,50))

        #Diamond assets
        self.pic_diamond = pygame.image.load('War of stick/background_photo.jpg').convert_alpha()
        self.pic_diamond_surf = pygame.transform.scale(self.pic_diamond,(50,25))
        self.pic_diamond_rect = self.pic_diamond_surf.get_rect(center=(760,80))

        self.num_diamond_font = pygame.font.Font(None,30)
        self.num_diamond_surf = self.num_diamond_font.render(str(self.num_diamond), True, 'Black')
        self.num_diamond_rect = self.num_diamond_surf.get_rect(center=(800,80))

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

        current_time = pygame.time.get_ticks()
        if current_time - self.gold_time >= self.gold_interval:
            self.num_gold += 10
            self.gold_time = current_time

        if current_time - self.diamond_time >= self.diamond_interval:
            self.num_diamond += 5
            self.diamond_time = current_time
        
        # Check if the left mouse button was clicked and handle accordingly
        mouse_pos = pygame.mouse.get_pos()

        if clicked:
            if self.troop_one_button.is_clicked(mouse_pos):
                if self.num_gold >= 50:
                    self.num_gold -= 50
                    self.show_one_background = True  # Set flag to show background image
        self.troop_one_button.reset()   # Reset the button to make it make to the size i set

        if clicked:
            if self.troop_two_button.is_clicked(mouse_pos):
                if self.num_gold >= 50:
                    self.num_gold -= 50
                    self.show_two_background = True  # Set flag to show background image
        self.troop_two_button.reset()

        if clicked:
            if self.troop_three_button.is_clicked(mouse_pos):
                if self.num_gold >= 50:
                    self.num_gold -= 50
                    self.show_three_background = True  # Set flag to show background image
        self.troop_three_button.reset()    

        if clicked:
            if self.troop_four_button.is_clicked(mouse_pos):
                if self.num_gold >= 50:
                    self.num_gold -= 50
                    self.show_four_background = True  # Set flag to show background image
        self.troop_four_button.reset()

        if clicked:
            if self.troop_five_button.is_clicked(mouse_pos):
                if self.num_gold >= 50:
                    self.num_gold -= 50
                    self.show_five_background = True  # Set flag to show background image
        self.troop_five_button.reset()

    def game_start(self):
        self.screen.fill((255, 255, 255))  # Clear screen
        self.screen.blit(self.background_image, (self.bg_x, 0))

        self.screen.blit(self.pic_gold_surf,self.pic_gold_rect)
        self.num_gold_surf = self.num_gold_font.render(str(self.num_gold), True, 'Black')
        self.screen.blit(self.num_gold_surf,self.num_gold_rect)

        self.screen.blit(self.pic_diamond_surf,self.pic_diamond_rect)
        self.num_diamond_surf = self.num_diamond_font.render(str(self.num_diamond), True, 'Black')
        self.screen.blit(self.num_diamond_surf,self.num_diamond_rect)

        if self.show_one_background == True:
            self.screen.blit(self.troop_one_image, (100, 465))
            print('troop one')

        if self.show_two_background == True:
            self.screen.blit(self.troop_two_image, (200, 465))  # Blit army on the screen
            print('troop two')

        if self.show_three_background == True:
            self.screen.blit(self.troop_three_image, (300, 465))  # Blit army on the screen
            print('troop three')

        if self.show_four_background == True:
            self.screen.blit(self.troop_four_image, (400, 465))  # Blit army on the screen
            print('troop four')

        if self.show_five_background == True:
            self.screen.blit(self.troop_five_image, (500, 465))  # Blit army on the screen
            print('troop five')
            

        self.troop_one_button.draw(self.screen)
        self.troop_two_button.draw(self.screen)
        self.troop_three_button.draw(self.screen)
        self.troop_four_button.draw(self.screen)
        self.troop_five_button.draw(self.screen)

    def run(self):
        while True:
            self.event_handling()
            self.game_start()

            pygame.display.update()  # Update the display
            self.clock.tick(60)  # Limit frame rate to 60 FPS

if __name__ == "__main__":
    Game().run()

    