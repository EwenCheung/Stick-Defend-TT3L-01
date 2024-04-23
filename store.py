import pygame
from sys import exit

pygame.init()

class Item_card():
    def __init__(self):

        self.warrior_card_image = pygame.image.load('War of stick/Picture/stickman sword/stickman warrior card.png').convert_alpha()
        self.warrior_card_surf = pygame.transform.scale(self.warrior_card_image,(100,150))
        self.warrior_card_rect = self.warrior_card_surf.get_rect(center=(100,100))

        self.archer_card_image = pygame.image.load('War of stick/Picture/stickman archer/stickman archer card.png').convert_alpha()
        self.archer_card_surf = pygame.transform.scale(self.archer_card_image,(100,150))
        self.archer_card_rect = self.archer_card_surf.get_rect(center=(300,100))

        self.sparta_card_image = pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta card.png').convert_alpha()
        self.sparta_card_surf = pygame.transform.scale(self.sparta_card_image,(100,150))
        self.sparta_card_rect = self.sparta_card_surf.get_rect(center=(500,100))

        self.wizard_card_image = pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard card.png').convert_alpha()
        self.wizard_card_surf = pygame.transform.scale(self.wizard_card_image,(100,150))
        self.wizard_card_rect = self.wizard_card_surf.get_rect(center=(700,100))

        self.giant_card_image = pygame.image.load('War of stick/Picture/stickman giant/stickman giant card.png').convert_alpha()
        self.giant_card_surf = pygame.transform.scale(self.giant_card_image,(100,150))
        self.giant_card_rect = self.giant_card_surf.get_rect(center=(900,100))
    
class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption('Store')
        self.cards = Item_card()
        self.set_up()
        
    def set_up(self):
        self.button_background_surf = pygame.image.load('War of stick/Picture/utlis/button_for_store.jpeg')
        self.button_background_surf = pygame.transform.scale(self.button_background_surf, (100,50))

        #duplicate each of the troop has one background
        self.warrior_button_surf = self.button_background_surf.copy()
        self.archer_button_surf = self.button_background_surf.copy()
        self.sparta_button_surf = self.button_background_surf.copy()
        self.wizard_button_surf = self.button_background_surf.copy()
        self.giant_button_surf = self.button_background_surf.copy()

        #set the position for each button background
        self.warrior_button_rect = self.warrior_button_surf.get_rect(center=(100,220))
        self.archer_button_rect = self.archer_button_surf.get_rect(center=(300,220))
        self.sparta_button_rect = self.sparta_button_surf.get_rect(center=(500,220))
        self.wizard_button_rect = self.wizard_button_surf.get_rect(center=(700,220))
        self.giant_button_rect = self.giant_button_surf.get_rect(center=(900,220))

        #Create word
        self.font = pygame.font.Font(None, 30)
        self.unlock_text_surf = self.font.render('Unlock', True, 'White')
        self.unlock_text_rect = self.unlock_text_surf.get_rect()

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def game_start(self):
        self.screen.blit(self.cards.warrior_card_surf, self.cards.warrior_card_rect)
        self.screen.blit(self.cards.archer_card_surf, self.cards.archer_card_rect)
        self.screen.blit(self.cards.sparta_card_surf, self.cards.sparta_card_rect)
        self.screen.blit(self.cards.wizard_card_surf, self.cards.wizard_card_rect)
        self.screen.blit(self.cards.giant_card_surf, self.cards.giant_card_rect)

        #display the button image 
        self.screen.blit(self.warrior_button_surf, self.warrior_button_rect)
        self.screen.blit(self.archer_button_surf, self.archer_button_rect)
        self.screen.blit(self.sparta_button_surf, self.sparta_button_rect)
        self.screen.blit(self.wizard_button_surf, self.wizard_button_rect)
        self.screen.blit(self.giant_button_surf, self.giant_button_rect)

        #display text image
        self.screen.blit(self.unlock_text_surf, self.unlock_text_rect.move(65, 210))  
        self.screen.blit(self.unlock_text_surf, self.unlock_text_rect.move(265, 210))  
        self.screen.blit(self.unlock_text_surf, self.unlock_text_rect.move(465, 210))  
        self.screen.blit(self.unlock_text_surf, self.unlock_text_rect.move(665, 210))  
        self.screen.blit(self.unlock_text_surf, self.unlock_text_rect.move(865, 210))  
    def run(self):
        while True:
            self.screen.fill((255, 255, 255))

            self.event_handling()
            self.game_start()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    Game().run()