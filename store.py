import pygame
from sys import exit
import random

pygame.init()

class Item_card():
    def __init__(self):

        self.warrior_card_image = pygame.image.load('War of stick/Picture/stickman sword/stickman warrior card.png').convert_alpha()
        self.warrior_card_surf = pygame.transform.scale(self.warrior_card_image,(100,150))
        self.warrior_card_surf_small = pygame.transform.scale(self.warrior_card_image,(50,75))
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
        self.store = True
        self.backpack = False
        self.detail_page = False
        self.font = pygame.font.Font(None, 30)
        self.price_font = pygame.font.Font(None, 25)
        #define the x,y coordiante for the card
        self.x_coords = ([325,470,610,325,470,610,325,470,610])
        self.y_coords = ([200,200,200,336,336,336,477,477,477])

        self.backpack_screen = pygame.Surface((700, 450))  # Creating a surface for backpack display
        self.detail_page_screen = pygame.Surface((600, 400))
            
        self.set_up()
        
    def set_up(self):
        #load background
        self.background_image = pygame.image.load('War of stick/Picture/store/store background.png').convert_alpha()
        self.background_surf = pygame.transform.scale(self.background_image,(1000,600))

        self.button_background_surf = pygame.image.load('War of stick/Picture/store/button_for_store.png')
        self.button_background_surf = pygame.transform.scale(self.button_background_surf, (150,75))

        #refresh button image
        self.refresh_button_surf = pygame.image.load('War of stick/Picture/store/refresh button.png').convert_alpha()
        self.refresh_button_surf = pygame.transform.scale(self.refresh_button_surf,(95,95))
        self.refresh_button_rect = self.refresh_button_surf.get_rect(midright=(870,398))

        #load the backpack image
        self.backpack_image_surf = pygame.image.load('War of stick/Picture/store/box.png').convert_alpha()
        self.backpack_image_surf = pygame.transform.scale(self.backpack_image_surf,(135,110))
        self.backpack_image_rect = self.backpack_image_surf.get_rect(bottomright = (900,570))
        
        #money for purchase 
        self.money_image_surf = pygame.image.load('War of stick/Picture/store/money.png').convert_alpha()
        self.money_image_surf = pygame.transform.scale(self.money_image_surf, (15,10))
        self.money_image_rect = self.money_image_surf.get_rect(topright =(750,5))

        #load the store low opacity picture
        self.backpack_background_surf = pygame.image.load('War of stick/Picture/store/store background_backpack.png').convert_alpha()
        self.backpack_background_surf = pygame.transform.scale(self.backpack_background_surf,(1000,600))
        
        #load the back button image
        self.back_button_surf = pygame.image.load('WAr of stick/Picture/store/back button.png').convert_alpha()
        self.back_button_surf = pygame.transform.scale(self.back_button_surf, (50,50))
        self.back_button_rect = self.back_button_surf.get_rect(bottomright=(850,450))
        
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

        #Create word
        self.unlock_text_surf = self.font.render('Unlock', True, 'Black')
        self.unlock_text_rect = self.unlock_text_surf.get_rect()

        self.store_list = [
            {'image' : self.cards.archer_card_surf_small, 'name' : 'archer','button': self.button_background_surf, 'locked' : True, 'money' : self.money_image_surf, 'price' : '200'},
            {'image' : self.cards.sparta_card_surf_small, 'name' : 'sparta','button': self.button_background_surf, 'locked' : True, 'money' : self.money_image_surf, 'price' : '350'},
            {'image' : self.cards.wizard_card_surf_small, 'name' : 'wizard','button': self.button_background_surf, 'locked' : True, 'money' : self.money_image_surf, 'price' : '450'},
            {'image' : self.cards.giant_card_surf_small, 'name' : 'giant','button': self.button_background_surf, 'locked' : True,  'money' : self.money_image_surf, 'price' : '550'}
        ]

        self.backpack_list = [
            {'image' : self.cards.warrior_card_surf_small, 'name' : 'warrior','button' : self.button_background_surf, 'locked' : False, 'money' : self.money_image_surf, 'price' : '200', 'level': 'lv 1'}
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
                    random.shuffle(self.store_list)

                if self.store:
                        for index, item in enumerate(self.store_list):
                            if item['locked']:
                                button_background_rect = item['button'].get_rect(center=(self.x_coords[index], self.y_coords[index] + 45))
                                if button_background_rect.collidepoint(mouse_pos):
                                    item_copy = item.copy()
                                    item_copy['level'] = 'lv 1'
                                    self.backpack_list.append(item_copy)
                                    item['locked'] = False
                                    del self.store_list[index]


                if self.backpack_image_rect.collidepoint(mouse_pos):
                    self.store = False
                    self.backpack = True

                if self.backpack:
                    if self.back_button_rect.collidepoint(mouse_pos):
                        self.store = True
                        self.backpack = False
                        self.detail_page = False
                    for index, item in enumerate(self.backpack_list):
                        card_image = item['image']
                        card_image_rect = card_image.get_rect(center=(self.x_coords[index], self.y_coords[index]))
                        if card_image_rect.collidepoint(mouse_pos):
                            self.store = False
                            self.backpack = False
                            self.detail_page = True 

    def game_start(self):
        if self.store:
            self.screen.blit(self.background_surf, (0, 0))
            self.screen.blit(self.topic_word_surf, self.topic_word_rect) 

            self.screen.blit(self.refresh_button_surf, self.refresh_button_rect)
            self.screen.blit(self.backpack_image_surf,self.backpack_image_rect)
            self.screen.blit(self.money_image_surf,self.money_image_rect)
            
            for index, item in enumerate(self.store_list):
                if item['locked']:
                    card_image = item['image']
                    card_rect = card_image.get_rect(center=(self.x_coords[index], self.y_coords[index]))
                    self.screen.blit(card_image, card_rect)

                    text=self.font.render(f"{item['name'].capitalize()}", True, 'Red')
                    text_rect = text.get_rect(center=(self.x_coords[index], self.y_coords[index] -50))
                    self.screen.blit(text,text_rect)

                    button_background_surf = item['button']
                    button_background_rect = button_background_surf.get_rect(center=(self.x_coords[index], self.y_coords[index]+45))
                    self.screen.blit(button_background_surf,button_background_rect)

                    money_image_surf = item['money']
                    money_image_rect = money_image_surf.get_rect(center=(self.x_coords[index] +20, self.y_coords[index] +45))
                    self.screen.blit(money_image_surf,money_image_rect)

                    price_text_surf = self.price_font.render(item['price'].capitalize(), True, 'Black')
                    price_text_rect = price_text_surf.get_rect(center=(self.x_coords[index] -7, self.y_coords[index] +46))
                    self.screen.blit(price_text_surf,price_text_rect)

        elif self.backpack:
            self.screen.blit(self.backpack_background_surf,(0,0))
            self.backpack_screen.fill((0,0,0))  
            self.screen.blit(self.backpack_screen, (150, 75))  # Adjust position as needed
            self.screen.blit(self.back_button_surf, self.back_button_rect)
            for index, item in enumerate(self.backpack_list):
                card_image = item['image']
                card_rect = card_image.get_rect(center=(self.x_coords[index], self.y_coords[index]))
                self.screen.blit(card_image, card_rect)

                level_display = item['level']  
                level_display_surf = self.font.render(level_display, True, 'White')
                level_display_rect = level_display_surf.get_rect(center=(self.x_coords[index], self.y_coords[index]+50))
                self.screen.blit(level_display_surf, level_display_rect)


        elif self.detail_page :
            self.screen.blit(self.backpack_background_surf, (0,0))
            self.screen.blit(self.detail_page_screen, (200,100))
            self.detail_page_screen.fill((0, 255, 255))



    def run(self):
        while True:
            self.screen.fill((255, 255, 255))

            self.event_handling()
            self.game_start()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    Game().run()