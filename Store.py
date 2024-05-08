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
        self.font = pygame.font.Font(None, 30)
        self.price_font = pygame.font.Font(None, 25)
        # self.selected_card = None
        self.num_money = 50000
        #define the x,y coordiante for the card
        self.x_coords = ([325,470,610,325,470,610,325,470,610])
        self.y_coords = ([200,200,200,336,336,336,477,477,477])
        self.x_button_coordinate = ([547,647,747,847])
        self.y_button_coordinate = ([218,218,218,218])
        self.selected_category = 'Castle'
        self.set_up()
        
    def set_up(self):
        #store
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
        self.backpack_image_surf = pygame.image.load('War of stick/Picture/store/backpack.png').convert_alpha()
        self.backpack_image_surf = pygame.transform.scale(self.backpack_image_surf,(90,90))
        self.backpack_image_rect = self.backpack_image_surf.get_rect(bottomright = (870,570))
        
        #money for purchase 
        self.money_image_surf = pygame.image.load('War of stick/Picture/store/money.png').convert_alpha()
        self.money_image_surf = pygame.transform.scale(self.money_image_surf, (15,10))
        self.money_image_rect = self.money_image_surf.get_rect(topright =(920,10))

        #load blank card image
        self.blank_card_surf = pygame.image.load('War of stick/Picture/store/blank card image.png').convert_alpha()
        self.blank_card_surf = pygame.transform.scale(self.blank_card_surf,(50,75))

        #backpack 
        #load backpack image
        self.backpack_background_surf = pygame.image.load('War of stick/Picture/store/backpack background.png').convert_alpha()
        self.backpack_background_surf = pygame.transform.scale(self.backpack_background_surf,(800,400))

        self.castle_image_surf = pygame.image.load('War of stick/Picture/store/castle.png').convert_alpha()
        self.castle_image_surf = pygame.transform.scale(self.castle_image_surf,(300,300))

        self.health_image_surf = pygame.image.load('War of stick/Picture/store/health.png').convert_alpha()
        self.health_image_surf = pygame.transform.scale(self.health_image_surf,(20,20))

        self.mining_image_surf = pygame.image.load('War of stick/Picture/store/pickaxe.png').convert_alpha()
        self.mining_image_surf = pygame.transform.scale(self.mining_image_surf,(30,30))

        self.damage_image_surf = pygame.image.load('WAr of stick/Picture/store/damage.png').convert_alpha()
        self.damage_image_surf = pygame.transform.scale(self.damage_image_surf,(20,20))

        #load the back button image
        self.back_button_surf = pygame.image.load('War of stick/Picture/store/back button.png').convert_alpha()
        self.back_button_surf = pygame.transform.scale(self.back_button_surf, (50,50))
        self.back_button_rect = self.back_button_surf.get_rect(bottomright=(900,100))

        self.troop_equipment_box_surf = pygame.image.load('War of stick/Picture/store/equipment box.png').convert_alpha()
        self.troop_equipment_box_surf = pygame.transform.scale(self.troop_equipment_box_surf,(500,100))
        self.troop_equipment_box_rect = self.troop_equipment_box_surf.get_rect(center=(500,158))

        self.spell_equipment_box_surf = self.troop_equipment_box_surf.copy()
        self.spell_equipment_box_rect = self.spell_equipment_box_surf.get_rect(center=(500,87))
 
        # word
        self.unlock_text_surf = self.font.render('Unlock', True, 'Black')
        self.unlock_text_rect = self.unlock_text_surf.get_rect()

        self.backpack_word_surf = pygame.font.Font(None, 60)
        self.backpack_word_surf = self.backpack_word_surf.render('Backpack', True, 'White')
        self.backpack_word_rect = self.backpack_word_surf.get_rect(center=(480,27))
        
        #words for the topic
        self.topic_word_surf = pygame.font.Font(None, 60)
        self.topic_word_surf = self.topic_word_surf.render('War of stick store', True, 'Black')
        self.topic_word_rect = self.topic_word_surf.get_rect(center=(462,60))

        #money word
        self.num_money_surf = self.font.render(str(self.num_money), True, 'White')
        self.num_money_rect = self.num_money_surf.get_rect(topright=(900,5))

        self.castle_word_surf = self.font.render('Castle', True, 'White')
        self.castle_word_rect = self.castle_word_surf.get_rect(center=(545,220))

        self.troop_word_surf = self.font.render('Troop', True, 'White')
        self.troop_word_rect = self.troop_word_surf.get_rect(center=(645,220))

        self.spell_word_surf = self.font.render('Spell', True, 'White')
        self.spell_word_rect = self.spell_word_surf.get_rect(center=(745,220))

        self.others_word_surf = self.font.render('Others', True, 'White')
        self.others_word_rect = self.others_word_surf.get_rect(center=(845,220))

        self.store_list = [
            {'image' : self.cards.archer_card_surf_small, 'name' : 'archer','button': self.button_background_surf, 'locked' : True, 'money' : self.money_image_surf, 'price' : 200},
            {'image' : self.cards.sparta_card_surf_small, 'name' : 'sparta','button': self.button_background_surf, 'locked' : True, 'money' : self.money_image_surf, 'price' : 350},
            {'image' : self.cards.wizard_card_surf_small, 'name' : 'wizard','button': self.button_background_surf, 'locked' : True, 'money' : self.money_image_surf, 'price' : 450},
            {'image' : self.cards.giant_card_surf_small, 'name' : 'giant','button': self.button_background_surf, 'locked' : True,  'money' : self.money_image_surf, 'price' : 550},
            {'image' : self.blank_card_surf, 'name' : 'Blank 2', 'button' : self.button_background_surf,'locked' : True, 'money' : self.money_image_surf, 'price' : 300},
            {'image' : self.blank_card_surf, 'name' : 'Blank 3', 'button' : self.button_background_surf,'locked' : True, 'money' : self.money_image_surf, 'price' : 100},
            {'image' : self.blank_card_surf, 'name' : 'Blank 4', 'button' : self.button_background_surf,'locked' : True, 'money' : self.money_image_surf, 'price' : 378},
            {'image' : self.blank_card_surf, 'name' : 'Blank 5', 'button' : self.button_background_surf,'locked' : True, 'money' : self.money_image_surf, 'price' : 320},
            {'image' : self.blank_card_surf, 'name' : 'Blank 6', 'button' : self.button_background_surf,'locked' : True, 'money' : self.money_image_surf, 'price' : 330},
            {'image' : self.blank_card_surf, 'name' : 'Blank 7', 'button' : self.button_background_surf,'locked' : True, 'money' : self.money_image_surf, 'price' : 870},
            {'image' : self.blank_card_surf, 'name' : 'Blank 8', 'button' : self.button_background_surf,'locked' : True, 'money' : self.money_image_surf, 'price' : 500},
        ]
        self.store_list = self.store_list[:len(self.x_coords)]

        self.backpack_troop_list = [
            {'image' : self.cards.warrior_card_surf_small, 'name' : 'warrior','button' : self.button_background_surf, 'locked' : False, 'money' : self.money_image_surf, 'price' : '200', 'level': 'lv 1'}
        ]
        
        random.shuffle(self.store_list)
        self.upgrades_button_surf = self.button()
        self.castle_detail = [{
            'image': self.castle_image_surf,
            'name': 'Castle',
            'health icon' : self.health_image_surf,
            'health': 1000,
            'health level' : 1,
            'health price': 150,
            'mining icon' : self.mining_image_surf,
            'mining speed': 100,
            'mining speed level' : 1,
            'mining speed price' : 150,
            'upgrades button': self.upgrades_button_surf,
            'money image' : self.money_image_surf,
            }]

    def button(self):
        self.title_background_surf = pygame.image.load('War of stick/Picture/store/coklat background.jpg').convert_alpha()
        self.title_background_surf = pygame.transform.scale(self.title_background_surf,(90,40))
        self.title_background_dark_surf = pygame.image.load('War of stick/Picture/store/choc_bg_dark.png').convert_alpha()
        self.title_background_dark_surf = pygame.transform.scale(self.title_background_dark_surf,(90,40))
        self.button_surf = [
            self.title_background_surf.copy(),
            self.title_background_surf.copy(),
            self.title_background_surf.copy(),
            self.title_background_surf.copy()
        ]
        self.castle_background_surf = self.button_surf[0]
        self.troop_background_surf = self.button_surf[1]
        self.spell_background_surf = self.button_surf[2]
        self.others_background_surf = self.button_surf[3]

        #upgrade button 
        self.upgrades_button_size = (145,65)
        self.upgrades_button_surf= pygame.Surface(self.upgrades_button_size)
        self.upgrades_button_surf.fill((253,238,176))
        self.upgrades_button_surf =pygame.transform.scale(self.upgrades_button_surf,self.upgrades_button_size)

        return self.upgrades_button_surf
    
    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                #check if the refreash button is clicked
                if self.refresh_button_rect.collidepoint(mouse_pos):
                    if self.num_money >= 100:
                        self.num_money -= 100
                        random.shuffle(self.store_list)

                if self.backpack_image_rect.collidepoint(mouse_pos):
                    self.store = False
                    self.backpack = True
                    self.selected_category = 'Castle'

                if self.store:
                        for index, item in enumerate(self.store_list):
                            if item['locked']:
                                button_background_rect = item['button'].get_rect(center=(self.x_coords[index], self.y_coords[index] + 45))
                                if button_background_rect.collidepoint(mouse_pos):
                                    if self.num_money >= item['price']:
                                        self.num_money -= item['price']
                                        item_copy = item.copy()
                                        item_copy['level'] = 'lv 1'
                                        self.backpack_troop_list.append(item_copy)
                                        item['locked'] = False
                                        del self.store_list[index]

                if self.backpack:
                    if self.back_button_rect.collidepoint(mouse_pos):
                        self.store = True
                        self.backpack = False

                for index, surface in enumerate(self.button_surf):
                    x_coord = self.x_button_coordinate[index]
                    y_coord = self.y_button_coordinate[index]
                    surface_rect = surface.get_rect(center=(x_coord, y_coord))
                    if surface_rect.collidepoint(mouse_pos):
                        if index == 1 :
                            self.screen.blit(self.title_background_dark_surf, surface_rect)
                            self.selected_category = "Troop"
                        elif index == 2 :
                            self.screen.blit(self.title_background_dark_surf, surface_rect)
                            self.selected_category = 'Spell'
                        elif index == 3 :
                            self.screen.blit(self.title_background_dark_surf, surface_rect)
                            self.selected_category = 'Others'

                if self.backpack and self.selected_category == 'Castle':
                    for item in self.castle_detail:
                        health_button_rect = item['upgrades button'].get_rect(bottomleft=(118,520))
                        mining_button_rect = item['upgrades button'].get_rect(bottomleft=(338,520))
                        if health_button_rect.collidepoint(mouse_pos):
                            if self.num_money >= item['health price']:
                                self.num_money -= item['health price']
                                item['health level'] += 1
                                item['health price'] +=100
                        elif mining_button_rect.collidepoint(mouse_pos):
                            if self.num_money >= item['mining speed price']:
                                self.num_money -= item['mining speed price']
                                item['mining speed level'] += 1
                                item['mining speed price'] +=100

    def backpack_screen(self):
        self.display_detail_info()

    def display_detail_info(self):
        self.button() 
        if self.backpack and self.selected_category == 'Castle':
                    self.screen.fill((50,49,47))
                    self.screen.blit(self.backpack_background_surf, (100, 195))
                    self.screen.blit(self.backpack_word_surf,self.backpack_word_rect)
                    self.screen.blit(self.back_button_surf, self.back_button_rect)
                    self.screen.blit(self.money_image_surf,(465,213))
                    self.num_money_surf = self.font.render(str(self.num_money), True, 'Black')
                    self.screen.blit(self.num_money_surf,(400,210))
                    self.screen.blit(self.troop_equipment_box_surf,self.troop_equipment_box_rect)
                    self.screen.blit(self.spell_equipment_box_surf,self.spell_equipment_box_rect)

                    for index, surface in enumerate(self.button_surf):
                        x_coord = self.x_button_coordinate[index]
                        y_coord = self.y_button_coordinate[index]
                        surface_rect = surface.get_rect(center=(x_coord, y_coord))
                        self.screen.blit(surface, surface_rect) 


                    for item in self.castle_detail:
                        #display castle image
                        self.screen.blit(item['image'],(80,180))
                        #Display the health icon
                        health_icon_surf = item['health icon']
                        health_icon_rect = health_icon_surf.get_rect(midleft=(375,293))
                        self.screen.blit(health_icon_surf,health_icon_rect)

                        #display the health msg
                        health_text = self.font.render(f"{str(item['health'])}", True, 'Black')    
                        health_text_rect = health_text.get_rect(midleft=(400,295))    
                        self.screen.blit(health_text,health_text_rect)        

                        #display mining icon
                        mining_icon_surf = item['mining icon']
                        mining_icon_rect = mining_icon_surf.get_rect(midleft=(366,335))
                        self.screen.blit(mining_icon_surf,mining_icon_rect)

                        #display mining speed msg
                        mining_speed_text = self.font.render(f"{str(item['mining speed'])}", True, 'Black')
                        mining_speed_text_rect = mining_speed_text.get_rect(midleft=(402,337))
                        self.screen.blit(mining_speed_text,mining_speed_text_rect)

                        #display health upgrades button
                        health_button_surf = item['upgrades button']
                        health_button_rect = health_button_surf.get_rect(bottomleft=(118,565))
                        self.screen.blit(health_button_surf,health_button_rect)

                        mining_button_surf = item['upgrades button']
                        mining_button_rect = mining_button_surf.get_rect(bottomleft=(338,565))
                        self.screen.blit(mining_button_surf,mining_button_rect)

                        #health upgrades detail
                        health_upgrades_msg_surf = self.font.render(f"Health: Lv{str(item['health level'])}", True , 'Black')
                        health_upgrades_msg_rect = health_upgrades_msg_surf.get_rect(bottomleft=(132,530))
                        self.screen.blit(health_upgrades_msg_surf,health_upgrades_msg_rect)

                        health_upgrades_surf = self.price_font.render(f"Upgrade {str(item['health price'])}",True, 'Black')
                        health_upgrades_rect = health_upgrades_surf.get_rect(bottomleft=(130,555))
                        self.screen.blit(health_upgrades_surf,health_upgrades_rect)

                        health_money_icon_surf = item['money image']
                        health_money_icon_rect = health_money_icon_surf.get_rect(bottomleft=(237,549))
                        self.screen.blit(health_money_icon_surf,health_money_icon_rect)

                        mining_upgrades_msg_surf = self.font.render(f"Mining: Lv{str(item['mining speed level'])}", True, 'Black')
                        mining_upgrades_msg_rect = mining_upgrades_msg_surf.get_rect(bottomleft=(352,530))
                        self.screen.blit(mining_upgrades_msg_surf,mining_upgrades_msg_rect)

                        mining_upgrades_surf = self.price_font.render(f"Upgrade {str(item['mining speed price'])}", True, 'Black')
                        mining_upgrades_rect = mining_upgrades_surf.get_rect(bottomleft=(350,555))
                        self.screen.blit(mining_upgrades_surf,mining_upgrades_rect)

                        mining_money_icon_surf = item['money image']
                        mining_money_icon_rect = mining_money_icon_surf.get_rect(bottomleft=(457,549))
                        self.screen.blit(mining_money_icon_surf,mining_money_icon_rect)

                        right_part_castle_surf = item['image']
                        right_part_castle_surf = pygame.transform.scale(right_part_castle_surf,(120,120))
                        right_part_castle_rect = right_part_castle_surf.get_rect(center=(565,295))
                        self.screen.blit(right_part_castle_surf,right_part_castle_rect)

                    self.screen.blit(self.castle_word_surf,self.castle_word_rect)
                    self.screen.blit(self.troop_word_surf,self.troop_word_rect)
                    self.screen.blit(self.spell_word_surf,self.spell_word_rect)
                    self.screen.blit(self.others_word_surf,self.others_word_rect)

        elif self.selected_category == 'Troop':
            pass

        elif self.selected_category == 'Spell':
            pass
        elif self.selected_category == 'Others':
            pass

    def game_start(self):
        if self.store:
            self.screen.blit(self.background_surf, (0, 0))
            self.screen.blit(self.topic_word_surf, self.topic_word_rect) 

            self.screen.blit(self.refresh_button_surf, self.refresh_button_rect)
            self.screen.blit(self.backpack_image_surf,self.backpack_image_rect)
            self.screen.blit(self.money_image_surf,self.money_image_rect)
            self.num_money_surf = self.font.render(str(self.num_money), True, 'Black')
            self.screen.blit(self.num_money_surf,self.num_money_rect)

            coord_index = 0
            for index, item in enumerate(self.store_list):
                if item['locked'] and index <len(self.x_coords):
                    card_image = item['image']
                    card_rect = card_image.get_rect(center=(self.x_coords[coord_index], self.y_coords[coord_index]))
                    self.screen.blit(card_image, card_rect)

                    text=self.font.render(f"{item['name'].capitalize()}", True, 'Red')
                    text_rect = text.get_rect(center=(self.x_coords[coord_index], self.y_coords[coord_index] -50))
                    self.screen.blit(text,text_rect)

                    button_background_surf = item['button']
                    button_background_rect = button_background_surf.get_rect(center=(self.x_coords[coord_index], self.y_coords[coord_index]+45))
                    self.screen.blit(button_background_surf,button_background_rect)

                    money_image_surf = item['money']
                    money_image_rect = money_image_surf.get_rect(center=(self.x_coords[coord_index] +20, self.y_coords[coord_index] +45))
                    self.screen.blit(money_image_surf,money_image_rect)

                    price_text_surf = self.price_font.render(str(item['price']), True, 'Black')
                    price_text_rect = price_text_surf.get_rect(center=(self.x_coords[coord_index] -7, self.y_coords[coord_index] +46))
                    self.screen.blit(price_text_surf,price_text_rect)

                    coord_index +=1

        elif self.backpack:
            self.backpack_screen()

    def run(self):
        while True:
            self.screen.fill((255, 255, 255))

            self.event_handling()
            self.game_start()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    Game().run()