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
        self.archer_card_surf_small = pygame.transform.scale(self.archer_card_image,(50,75))
        self.archer_card_rect = self.archer_card_surf.get_rect(center=(300,100))

        self.sparta_card_image = pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta card.png').convert_alpha()
        self.sparta_card_surf = pygame.transform.scale(self.sparta_card_image,(100,150))
        self.sparta_card_surf_small = pygame.transform.scale(self.sparta_card_image,(50,75))
        self.sparta_card_rect = self.sparta_card_surf.get_rect(center=(500,100))

        self.wizard_card_image = pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard card.png').convert_alpha()
        self.wizard_card_surf = pygame.transform.scale(self.wizard_card_image,(100,150))
        self.wizard_card_surf_small = pygame.transform.scale(self.wizard_card_image,(50,75))
        self.wizard_card_rect = self.wizard_card_surf.get_rect(center=(700,100))

        self.giant_card_image = pygame.image.load('War of stick/Picture/stickman giant/stickman giant card.png').convert_alpha()
        self.giant_card_surf = pygame.transform.scale(self.giant_card_image,(100,150))
        self.giant_card_surf_small = pygame.transform.scale(self.giant_card_image,(50,75))
        self.giant_card_rect = self.giant_card_surf.get_rect(center=(900,100))
    
class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption('Store')
        self.cards = Item_card()
        self.backpack = False
        self.store = True
        self.font = pygame.font.Font(None, 30)
        self.price_font = pygame.font.Font(None, 25)
            
        self.set_up()
        
    def set_up(self):
        #load background
        self.background_image = pygame.image.load('War of stick/Picture/store/store background.png').convert_alpha()
        self.background_surf = pygame.transform.scale(self.background_image,(1000,600))

        self.button_background_surf = pygame.image.load('War of stick/Picture/store/button_for_store.png')
        self.button_background_surf = pygame.transform.scale(self.button_background_surf, (150,75))

        #refresh button image
        self.refresh_button_surf = pygame.image.load('War of stick/Picture/store/refresh button.png').convert_alpha()
        self.refresh_button_surf = pygame.transform.scale(self.refresh_button_surf,(95,75))
        self.refresh_button_rect = self.refresh_button_surf.get_rect(midright=(870,398))
        
        #words for the topic
        self.topic_word_surf = pygame.font.Font(None, 60)
        self.topic_word_surf = self.topic_word_surf.render('War of stick store', True, 'Black')
        self.topic_word_rect = self.topic_word_surf.get_rect(center=(462,60))

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

        #money for purchase 
        self.money_image_surf = pygame.image.load('War of stick/Picture/store/money.png')
        self.money_image_surf = pygame.transform.scale(self.money_image_surf, (15,10))

        #Create word
        self.unlock_text_surf = self.font.render('Unlock', True, 'Black')
        self.unlock_text_rect = self.unlock_text_surf.get_rect()

        self.store_list = [
            {'image' : self.cards.archer_card_surf_small, 'name' : 'archer','button': self.button_background_surf, 'locked' : True, 'money' : self.money_image_surf, 'price' : '200'},
            {'image' : self.cards.sparta_card_surf_small, 'name' : 'sparta','button': self.button_background_surf, 'locked' : True, 'money' : self.money_image_surf, 'price' : '350'},
            {'image' : self.cards.wizard_card_surf_small, 'name' : 'wizard','button': self.button_background_surf, 'locked' : True, 'money' : self.money_image_surf, 'price' : '450'},
            {'image' : self.cards.giant_card_surf_small, 'name' : 'giant','button': self.button_background_surf, 'locked' : True,  'money' : self.money_image_surf, 'price' : '550'}
        ]

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                #check if the refreash button is clicked
                if self.refresh_button_rect.collidepoint(mouse_pos):
                    print('refresh button clicked')

                for item in self.store_list:
                    if item['locked']:
                        if button_background_rect.collidepoint(mouse_pos):
                            print('halo')
            # if click on backpack:
            #     self.store = False
            #     self.backpack = True
            # if click on bacl:
            #     self.backpack = False
            #     self.store =True

    def game_start(self):
        if self.store:
            self.screen.blit(self.background_surf, (0, 0))
            self.screen.blit(self.topic_word_surf, self.topic_word_rect) 

            self.screen.blit(self.refresh_button_surf, self.refresh_button_rect)

            #define the x,y coordiante for the card
            x_coords = ([325,470,610,325,470,610,325,470,610])
            y_coords = ([200,200,200,336,336,336,477,477,477])
            
            for index, item in enumerate(self.store_list):
                if item['locked']:
                    card_image = item['image']
                    card_rect = card_image.get_rect(center=(x_coords[index], y_coords[index]))
                    self.screen.blit(card_image, card_rect)

                    text=self.font.render(f"{item['name'].capitalize()}", True, 'Red')
                    text_rect = text.get_rect(center=(x_coords[index], y_coords[index] -50))
                    self.screen.blit(text,text_rect)

                    button_background_surf = item['button']
                    button_background_rect = button_background_surf.get_rect(center=(x_coords[index], y_coords[index]+45))
                    self.screen.blit(button_background_surf,button_background_rect)

                    money_image_surf = item['money']
                    money_image_rect = money_image_surf.get_rect(center=(x_coords[index] +20, y_coords[index] +45))
                    self.screen.blit(money_image_surf,money_image_rect)

                    price_text_surf = self.price_font.render(item['price'].capitalize(), True, 'Black')
                    price_text_rect = price_text_surf.get_rect(center=(x_coords[index] -7, y_coords[index] +46))
                    self.screen.blit(price_text_surf,price_text_rect)

            # shuffle(list)
            # for _ in list :
            #     if _[2] == locked:
            #         blit(300,y)
            #         blit(600,y)
            #         blit(900,y)
            #         y+=

        elif self.backpack:
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