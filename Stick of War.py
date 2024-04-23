# coding : utf-8

import pygame
from sys import exit

pygame.init()


class TroopButton:
    def __init__(self, image, size, position):
        self.image = image
        self.size = size
        self.position = position
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(center=self.position)
        self.clicked_image = pygame.transform.scale(image, (20, 20))  # Adjust size for clicked appearance
        self.clicked = False
        self.coordinate_x = 0

    # this function make sure that when I press the button, the button will become small and become normal size again
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

class Troop(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        #load stickman image
        # stickman_warrior_image = [pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 1.png').convert_alpha(),
        #                       pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 2.png').convert_alpha(),
        #                       pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 3.png').convert_alpha(),
        #                       pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 4.png').convert_alpha(),
        #                       pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 5.png').convert_alpha()]
        
        # stickman_sparta_image = [pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 1.png').convert_alpha(),
        #                        pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 2.png').convert_alpha(),
        #                        pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 3.png').convert_alpha(),
        #                        pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 4.png').convert_alpha(),
        #                        pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 5.png').convert_alpha()]
        
        # stickman_archer_image = [pygame.image.load('War of stick/Picture/stickman archer/stickman archer 1.png').convert_alpha(),
        #                          pygame.image.load('War of stick/Picture/stickman archer/stickman archer 2.png').convert_alpha()]
        
        # stickman_wizard_image = [pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard walk/stickman wizard walk 1.png').convert_alpha(),
        #                          pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard walk/stickman wizard walk 2.png').convert_alpha(),
        #                          pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard walk/stickman wizard walk 3.png').convert_alpha(),
        #                          pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard walk/stickman wizard walk 4.png').convert_alpha(),
        #                          pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard walk/stickman wizard walk 5.png').convert_alpha()]
        
        # stickman_giant_image = [pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 1.png').convert_alpha(),
        #                         pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 2.png').convert_alpha(),
        #                         pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 3.png').convert_alpha(),
        #                         pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 4.png').convert_alpha(),
        #                         pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 5.png').convert_alpha()]
        
        # #load stickman attack image
        # stickman_sword_attack = [pygame.image.load('War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 1.png').convert_alpha(),
        #                          pygame.image.load('War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 2.png').convert_alpha(),
        #                          pygame.image.load('War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 3.png').convert_alpha()]
        
        # stickman_sparta_attack = [pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta attack/stickman sparta 1.png').convert_alpha(),
        #                           pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta attack/stickman sparta 2.png').convert_alpha()]
        
        # stickman_wizard_attack = [pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard attack/stickman wizard attack 1.png').convert_alpha(),
        #                           pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard attack/stickman wizard attack 2.png').convert_alpha(),
        #                           pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard attack/stickman wizard attack 3.png').convert_alpha()]
        
        # stickman_giant_attakc = [pygame.image.load('War of stick/Picture/stickman giant/stickman giant attack/stickman giant attack 1.png').convert_alpha(),
        #                          pygame.image.load('War of stick/Picture/stickman giant/stickman giant attack/stickman giant attack 2.png').convert_alpha()]

        self.image = image
        self.coordinate_x = 0

    def spawn_troop(self, screen, bg_x):
        screen.blit(self.image, (self.coordinate_x + bg_x, 450))

    def update(self):
        self.coordinate_x += 2

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tower Defend')  # title name
        self.screen = pygame.display.set_mode((1000, 600))
        self.bg_x = 0
        self.scroll_speed = 10
        self.num_gold = 500
        self.num_diamond = 300
        self.gold_time = pygame.time.get_ticks()
        self.diamond_time = pygame.time.get_ticks()
        self.gold_interval = 1000
        self.diamond_interval = 1000
        self.troop_on_court = []

        self.set_up()

    def set_up(self):
        # Scrolling Background
        self.background_image = pygame.image.load('War of stick/Picture/utlis/map_bg.jpg')

        # Gold assets
        self.pic_gold = pygame.image.load('War of stick/Picture/utlis/gold.png').convert_alpha()
        self.pic_gold_surf = pygame.transform.scale(self.pic_gold, (25, 25))
        self.pic_gold_rect = self.pic_gold_surf.get_rect(center=(760, 50))

        self.num_gold_font = pygame.font.Font(None, 30)
        self.num_gold_surf = self.num_gold_font.render(str(self.num_gold), True, 'Black')
        self.num_gold_rect = self.num_gold_surf.get_rect(center=(800, 50))

        # Diamond assets
        self.pic_diamond = pygame.image.load('War of stick/Picture/utlis/diamond.png').convert_alpha()
        self.pic_diamond_surf = pygame.transform.scale(self.pic_diamond, (50, 25))
        self.pic_diamond_rect = self.pic_diamond_surf.get_rect(center=(760, 80))

        self.num_diamond_font = pygame.font.Font(None, 30)
        self.num_diamond_surf = self.num_diamond_font.render(str(self.num_diamond), True, 'Black')
        self.num_diamond_rect = self.num_diamond_surf.get_rect(center=(800, 80))

        # Troop One
        self.warrior_image = pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 1.png').convert_alpha()
        self.warrior_image = pygame.transform.scale(self.warrior_image, (100, 100))
        self.warrior_button = TroopButton(self.warrior_image, (50, 50), (100, 100))

        # Troop Two
        self.archer_image = pygame.image.load('War of stick/Picture/stickman archer/stickman archer 1.png').convert_alpha()
        self.archer_image = pygame.transform.scale(self.archer_image, (100, 100))
        self.archer_button = TroopButton(self.archer_image, (50, 50), (200, 100))

        # Troop Three
        self.wizard_image = pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard walk/stickman wizard walk 1.png').convert_alpha()
        self.wizard_image = pygame.transform.scale(self.wizard_image, (100, 100))
        self.wizard_button = TroopButton(self.wizard_image, (50, 50), (300, 100))

        # Troop Four
        self.sparta_image = pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 1.png').convert_alpha()
        self.sparta_image = pygame.transform.scale(self.sparta_image, (100, 100))
        self.sparta_button = TroopButton(self.sparta_image, (50, 50), (400, 100))

        # Troop Five
        self.giant_image = pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 1.png').convert_alpha()
        self.giant_image = pygame.transform.scale(self.giant_image, (100, 100))
        self.giant_button = TroopButton(self.giant_image, (50, 50), (500, 100))

    def event_handling(self):
        def clicked_troop(gold_cost, diamond_cost, button_name, troop_image):
            mouse_pos = pygame.mouse.get_pos()  # Check if the left mouse button was clicked and handle accordingly

            if button_name.is_clicked(mouse_pos):
                if self.num_gold >= gold_cost and self.num_diamond >= diamond_cost:
                    self.num_gold -= gold_cost
                    self.num_diamond -= diamond_cost
                    new_troop = Troop(troop_image)
                    self.troop_on_court.append(new_troop)
            button_name.reset()  # Reset the button to make it make to the size I set

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check if left mouse button is pressed
                    clicked_troop(10, 20, self.warrior_button, self.warrior_image)
                    clicked_troop(30, 20, self.archer_button, self.archer_image)
                    clicked_troop(50, 50, self.wizard_button, self.wizard_image)
                    clicked_troop(70, 20, self.sparta_button, self.sparta_image)
                    clicked_troop(70, 20, self.giant_button, self.giant_image)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.bg_x += self.scroll_speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.bg_x -= self.scroll_speed

        self.bg_x = max(self.bg_x, 1000 - self.background_image.get_width())
        self.bg_x = min(self.bg_x, 0)

        current_time = pygame.time.get_ticks()
        if current_time - self.gold_time >= self.gold_interval:
            self.num_gold += 3
            self.gold_time = current_time

        if current_time - self.diamond_time >= self.diamond_interval:
            self.num_diamond += 2
            self.diamond_time = current_time

    def game_start(self):
        self.screen.fill((255, 255, 255))  # Clear screen
        self.screen.blit(self.background_image, (self.bg_x, 0))

        self.screen.blit(self.pic_gold_surf, self.pic_gold_rect)
        self.num_gold_surf = self.num_gold_font.render(str(self.num_gold), True, 'Black')
        self.screen.blit(self.num_gold_surf, self.num_gold_rect)

        self.screen.blit(self.pic_diamond_surf, self.pic_diamond_rect)
        self.num_diamond_surf = self.num_diamond_font.render(str(self.num_diamond), True, 'Black')
        self.screen.blit(self.num_diamond_surf, self.num_diamond_rect)

        self.warrior_button.draw(self.screen)
        self.archer_button.draw(self.screen)
        self.wizard_button.draw(self.screen)
        self.sparta_button.draw(self.screen)
        self.giant_button.draw(self.screen)

        for troop in self.troop_on_court:
            troop.spawn_troop(self.screen, self.bg_x)
            troop.update()

    def run(self):
        while True:
            self.game_start()
            self.event_handling()

            pygame.display.update()  # Update the display
            self.clock.tick(60)  # Limit frame rate to 60 FPS


if __name__ == "__main__":
    Game().run()
