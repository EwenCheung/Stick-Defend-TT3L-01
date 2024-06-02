import pygame
from sys import exit
import random
import importlib
from Firebase import firebase

pygame.init()
pygame.font.init()
#others troop * 10
#archer wiazrd(attack damage) after use the formula *5//1
#spell blit percentage
#backpack 人一开始就Blit

class Item_card():
    def __init__(self):
        # load store card image
        self.warrior_card_image = pygame.image.load('War of stick/Picture/stickman sword/stickman warrior card.png').convert_alpha()
        self.warrior_card_surf = pygame.transform.scale(self.warrior_card_image, (50, 75))

        self.archer_card_image = pygame.image.load('War of stick/Picture/stickman archer/stickman archer card.png').convert_alpha()
        self.archer_card_surf = pygame.transform.scale(self.archer_card_image, (50, 75))

        self.sparta_card_image = pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta card.png').convert_alpha()
        self.sparta_card_surf = pygame.transform.scale(self.sparta_card_image, (50, 75))

        self.wizard_card_image = pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard card.png').convert_alpha()
        self.wizard_card_surf = pygame.transform.scale(self.wizard_card_image, (50, 75))
        self.wizard_card_rect = self.wizard_card_surf.get_rect(center=(700, 100))

        self.giant_card_image = pygame.image.load('War of stick/Picture/stickman giant/stickman giant card.png').convert_alpha()
        self.giant_card_surf = pygame.transform.scale(self.giant_card_image, (50, 75))

        # load backpack stcik image
        self.warrior_image_surf = pygame.image.load(
            'War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 1.png').convert_alpha()
        self.warrior_image_surf = pygame.transform.scale(self.warrior_image_surf, (100, 120))

        self.archer_image_surf = pygame.image.load('War of stick/Picture/stickman archer/stickman archer 1.png').convert_alpha()
        self.archer_image_surf = pygame.transform.scale(self.archer_image_surf, (65, 65))

        self.sparta_image_surf = pygame.image.load(
            'War of stick/Picture/stickman sparta/stickman sparta attack/stickman sparta attack 1.png').convert_alpha()
        self.sparta_image_surf = pygame.transform.scale(self.sparta_image_surf, (80, 105))

        self.wizard_image_surf = pygame.image.load(
            'War of stick/Picture/stickman wizard/stickman wizard attack/stickman wizard attack 1.png').convert_alpha()
        self.wizard_image_surf = pygame.transform.scale(self.wizard_image_surf, (85, 100))

        self.giant_image_surf = pygame.image.load(
            'War of stick/Picture/stickman giant/stickman giant walk/stickman giant walk 1.png').convert_alpha()
        self.giant_image_surf = pygame.transform.scale(self.giant_image_surf, (75, 80))

        #spell card
        self.freeze_card_image_surf = pygame.image.load('War of stick/Picture/spell/freeze_spell.png').convert_alpha()
        self.freeze_card_image_surf = pygame.transform.scale(self.freeze_card_image_surf,(70,70))

        self.healing_card_image_surf = pygame.image.load('War of stick/Picture/spell/healing_spell.png').convert_alpha()
        self.healing_card_image_surf = pygame.transform.scale(self.healing_card_image_surf,(70,70))

        self.rage_card_image_surf = pygame.image.load('War of stick/Picture/spell/rage_spell.png').convert_alpha()
        self.rage_card_image_surf = pygame.transform.scale(self.rage_card_image_surf,(70,70))

class Game_Store:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Store')
        self.cards = Item_card()
        self.store = True
        self.backpack = False
        self.font = pygame.font.Font(None, 30)
        self.price_font = pygame.font.Font(None, 25)
        self.title_font = pygame.font.Font(None, 70)
        # self.selected_card = None
        self.num_money = 50000
        # define the x,y coordiante for the card
        self.x_coords = ([325, 470, 610, 325, 470, 610, 325, 470, 610])
        self.y_coords = ([200, 200, 200, 336, 336, 336, 477, 477, 477])
        self.x_button_coordinate = ([547, 647, 747, 847])
        self.y_button_coordinate = ([218, 218, 218, 218])
        self.selected_category = 'Castle'
        self.clicked_image_surf = 'warrior'
        self.clicked_spell_surf = 'freeze'
        self.equipped_box = []
        self.equipped_word_storage = []
        print(firebase.troop_storage)
        self.set_up()

    def set_up(self):
        self.upgrades_button_surf = self.button()
        # store
        # load background
        self.background_image = pygame.image.load('War of stick/Picture/store/store background.png').convert_alpha()
        self.background_surf = pygame.transform.scale(self.background_image, (1000, 600))

        self.button_background_surf = pygame.image.load('War of stick/Picture/store/button_for_store.png')
        self.button_background_surf = pygame.transform.scale(self.button_background_surf, (150, 75))

        # load the backpack image
        self.backpack_image_surf = pygame.image.load('War of stick/Picture/store/backpack.png').convert_alpha()
        self.backpack_image_surf = pygame.transform.scale(self.backpack_image_surf, (90, 90))
        self.backpack_image_rect = self.backpack_image_surf.get_rect(bottomright=(870, 570))

        # money for purchase
        self.money_image_surf = pygame.image.load('War of stick/Picture/store/money.png').convert_alpha()
        self.money_image_surf = pygame.transform.scale(self.money_image_surf, (15, 10))
        self.money_image_rect = self.money_image_surf.get_rect(topright=(920, 10))

        # load blank card image
        self.blank_card_surf = pygame.image.load('War of stick/Picture/store/blank card image.png').convert_alpha()
        self.blank_card_surf = pygame.transform.scale(self.blank_card_surf, (50, 75))

        # backpack
        # load backpack image
        self.backpack_background_surf = pygame.image.load('War of stick/Picture/store/backpack background.png').convert_alpha()
        self.backpack_background_surf = pygame.transform.scale(self.backpack_background_surf, (800, 400))

        self.castle_image_surf = pygame.image.load('War of stick/Picture/store/castle.png').convert_alpha()
        self.castle_image_surf = pygame.transform.scale(self.castle_image_surf, (300, 300))
        self.store_castle_image_surf = pygame.transform.scale(self.castle_image_surf, (120,120))

        self.health_image_surf = pygame.image.load('War of stick/Picture/store/health.png').convert_alpha()
        self.health_image_surf = pygame.transform.scale(self.health_image_surf, (20, 20))

        self.mining_image_surf = pygame.image.load('War of stick/Picture/store/pickaxe.png').convert_alpha()
        self.mining_image_surf = pygame.transform.scale(self.mining_image_surf, (30, 30))

        self.damage_image_surf = pygame.image.load('WAr of stick/Picture/store/damage.png').convert_alpha()
        self.damage_image_surf = pygame.transform.scale(self.damage_image_surf, (25, 25))

        self.timer_image_surf = pygame.image.load('War of stick/Picture/store/timer.png').convert_alpha()
        self.timer_image_surf = pygame.transform.scale(self.timer_image_surf,(30,30))

        # load the back button image
        self.back_button_surf = pygame.image.load('War of stick/Picture/store/back button.png').convert_alpha()
        self.back_button_surf = pygame.transform.scale(self.back_button_surf, (50, 50))
        self.back_button_rect = self.back_button_surf.get_rect(bottomright=(900, 100))

        self.troop_equipment_box_surf = pygame.image.load('War of stick/Picture/store/equipment box.png').convert_alpha()
        self.troop_equipment_box_surf = pygame.transform.scale(self.troop_equipment_box_surf, (500, 100))
        self.troop_equipment_box_rect = self.troop_equipment_box_surf.get_rect(center=(500, 158))

        self.spell_equipment_box_surf = self.troop_equipment_box_surf.copy()
        self.spell_equipment_box_rect = self.spell_equipment_box_surf.get_rect(center=(500, 87))

        self.gold_image_surf = pygame.image.load('War of stick/Picture/utils/gold.png').convert_alpha()
        self.gold_image_surf_surf = pygame.transform.scale(self.gold_image_surf, (25, 25))

        self.diamond_image_surf = pygame.image.load('War of stick/Picture/utils/diamond.png').convert_alpha()
        self.diamond_image_surf_surf = pygame.transform.scale(self.diamond_image_surf, (40, 25))

        self.equip_button_size = (120, 65)
        self.equip_button_surf = pygame.Surface(self.equip_button_size)
        self.equip_button_surf.fill((1, 50, 32))

        self.unequip_button_surf = pygame.Surface(self.equip_button_size)
        self.unequip_button_surf.fill((144, 238, 144))

        self.back_level_button_surf = pygame.image.load('War of stick/Picture/Store/back_to_level.png').convert_alpha()
        self.back_level_button_surf = pygame.transform.scale(self.back_level_button_surf,(75,75))
        self.back_level_button_rect = self.back_level_button_surf.get_rect(topleft=(25,15))

        self.back_level_background_surf = pygame.image.load('War of stick/Picture/Store/back_to_level_background.png').convert_alpha()
        self.back_level_background_surf = pygame.transform.scale(self.back_level_background_surf, (150, 100))
        self.back_level_background_rect = self.back_level_background_surf.get_rect(topleft=(40, 2))

        # word
        self.unlock_text_surf = self.font.render('Unlock', True, 'Black')
        self.unlock_text_rect = self.unlock_text_surf.get_rect()

        self.backpack_word_surf = pygame.font.Font(None, 60)
        self.backpack_word_surf = self.backpack_word_surf.render('Backpack', True, 'White')
        self.backpack_word_rect = self.backpack_word_surf.get_rect(center=(480, 27))

        # words for the topic
        self.topic_word_surf = pygame.font.Font(None, 60)
        self.topic_word_surf = self.topic_word_surf.render('War of stick store', True, 'Black')
        self.topic_word_rect = self.topic_word_surf.get_rect(center=(462, 60))

        self.level_word_surf = pygame.font.Font(None, 50)
        self.level_word_surf = self.level_word_surf.render('Level', True, 'Black')
        self.level_word_rect = self.level_word_surf.get_rect(topleft=(85,35))

        # money word
        self.num_money_surf = self.font.render(str(self.num_money), True, 'White')
        self.num_money_rect = self.num_money_surf.get_rect(topright=(900, 5))

        self.castle_word_surf = self.font.render('Castle', True, 'White')
        self.castle_word_rect = self.castle_word_surf.get_rect(center=(545, 220))

        self.troop_word_surf = self.font.render('Troop', True, 'White')
        self.troop_word_rect = self.troop_word_surf.get_rect(center=(645, 220))

        self.spell_word_surf = self.font.render('Spell', True, 'White')
        self.spell_word_rect = self.spell_word_surf.get_rect(center=(745, 220))

        self.others_word_surf = self.font.render('Others', True, 'White')
        self.others_word_rect = self.others_word_surf.get_rect(center=(845, 220))

        self.store_list = [
            {'image': self.store_castle_image_surf, 'name': 'castle', 'button': self.button_background_surf, 'locked': False, 
             'money': self.money_image_surf, 'price': 200},
            {'image': self.cards.warrior_card_surf, 'name': 'warrior', 'button': self.button_background_surf, 'locked': False,
              'money': self.money_image_surf, 'price': 250},
            {'image': self.cards.archer_card_surf, 'name': 'archer', 'button': self.button_background_surf, 'locked': True,
             'money': self.money_image_surf, 'price': 200},
            {'image': self.cards.sparta_card_surf, 'name': 'sparta', 'button': self.button_background_surf, 'locked': True,
             'money': self.money_image_surf, 'price': 350},
            {'image': self.cards.wizard_card_surf, 'name': 'wizard', 'button': self.button_background_surf, 'locked': True,
             'money': self.money_image_surf, 'price': 450},
            {'image': self.cards.giant_card_surf, 'name': 'giant', 'button': self.button_background_surf, 'locked': True,
             'money': self.money_image_surf, 'price': 550},
            {'image': self.cards.freeze_card_image_surf, 'name': 'freeze', 'button': self.button_background_surf, 'locked': True,
             'money': self.money_image_surf, 'price':200},
            {'image': self.cards.healing_card_image_surf, 'name': 'healing', 'button': self.button_background_surf, 'locked': True,
             'money': self.money_image_surf, 'price':200},
            {'image': self.cards.rage_card_image_surf, 'name': 'rage', 'button': self.button_background_surf, 'locked': True,
             'money': self.money_image_surf, 'price':200},
        ]

        self.backpack_troop_list = [
            {'image': self.cards.warrior_image_surf,
             'name': 'warrior',
             'button': self.button_background_surf,
             'locked': False,
             'equip': False,
             'money': self.money_image_surf,
             'upgrades price': 100,
             'level': 1,
             'health icon': self.health_image_surf,
             'damage icon': self.damage_image_surf,
             'gold icon': self.gold_image_surf_surf,
             'diamond icon': self.diamond_image_surf_surf,
             'upgrades button': self.upgrades_button_surf,
             'health': 1000,
             'attack damage': 10,
             'equip button': self.equip_button_surf,
             'unequip button': self.unequip_button_surf
             }
        ]

        self.spell_list = []
        self.troop_position = [
            {
                'warrior': (558, 290),
                'archer': (695, 278),
                'sparta': (830, 287),
                'wizard': (558, 410),
                'giant': (695, 400)
            }
        ]

        self.troop_msg_position = [
            {
                'warrior': (558, 320),
                'archer': (695, 320),
                'sparta': (830, 320),
                'wizard': (558, 438),
                'giant': (695, 438)
            }
        ]

        self.spell_position = [
            {
                'freeze': (558,290),
                'healing': (695,290),
                'rage': (830,290)
            }
        ]
        self.castle_detail = [{
            'image': self.castle_image_surf,
            'name': 'Castle',
            'health icon': self.health_image_surf,
            'health': 1000,
            'health level': 1,
            'health price': 150,
            'mining icon': self.mining_image_surf,
            'mining speed': 100,
            'mining speed level': 1,
            'mining speed price': 150,
            'upgrades button': self.upgrades_button_surf,
            'money image': self.money_image_surf,
        }]

    def button(self):
        self.title_background_surf = pygame.image.load('War of stick/Picture/store/coklat background.jpg').convert_alpha()
        self.title_background_surf = pygame.transform.scale(self.title_background_surf, (90, 40))
        self.title_background_dark_surf = pygame.image.load('War of stick/Picture/store/choc_bg_dark.png').convert_alpha()
        self.title_background_dark_surf = pygame.transform.scale(self.title_background_dark_surf, (90, 40))
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

        # upgrade button
        self.upgrades_button_size = (145, 65)
        self.upgrades_button_surf = pygame.Surface(self.upgrades_button_size)
        self.upgrades_button_surf.fill((253, 238, 176))

        return self.upgrades_button_surf

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.backpack_image_rect.collidepoint(mouse_pos):
                    self.store = False
                    self.backpack = True
                    self.selected_category = 'Castle'

                if self.store:
                    for index, item in enumerate(self.store_list):
                        if item['locked'] == True:
                            button_background_rect = item['button'].get_rect(
                                center=(self.x_coords[index], self.y_coords[index] + 45))
                            if button_background_rect.collidepoint(mouse_pos):
                                if self.num_money >= item['price']:
                                    self.num_money -= item['price']
                                    item_copy = item.copy()
                                    item_copy['level'] = 1
                                    item_copy['health icon'] = self.health_image_surf
                                    item_copy['damage icon'] = self.damage_image_surf
                                    item_copy['gold icon'] = self.gold_image_surf_surf
                                    item_copy['diamond icon'] = self.diamond_image_surf_surf
                                    item_copy['upgrades button'] = self.upgrades_button_surf
                                    item_copy['equip'] = False
                                    item_copy['equip button'] = self.equip_button_surf
                                    item_copy['unequip button'] = self.unequip_button_surf

                                    if item['name'] == 'archer':
                                        troop_image = self.cards.archer_image_surf
                                        item_copy['health'] = 2000
                                        item_copy['upgrades price'] = 200
                                        item_copy['attack damage'] = 25
                                    elif item['name'] == 'sparta':
                                        troop_image = self.cards.sparta_image_surf
                                        item_copy['health'] = 3000
                                        item_copy['upgrades price'] = 400
                                        item_copy['attack damage'] = 30
                                    elif item['name'] == 'wizard':
                                        troop_image = self.cards.wizard_image_surf
                                        item_copy['health'] = 2500
                                        item_copy['upgrades price'] = 300
                                        item_copy['attack damage'] = 25
                                    elif item['name'] == 'giant':
                                        troop_image = self.cards.giant_image_surf
                                        item_copy['health'] = 3500
                                        item_copy['upgrades price'] = 500
                                        item_copy['attack damage'] = 40
                                    elif item['name'] in ['freeze', 'healing', 'rage']:
                                        if item['name'] == 'freeze':
                                            item_copy['upgrades price'] = 300
                                            item_copy['spell function'] = 50
                                        elif item['name'] == 'healing':
                                            item_copy['upgrades price'] = 200
                                            item_copy['healing function'] = 300
                                        elif item['name'] == 'rage':
                                            item_copy['upgrades price'] = 100
                                            item_copy['spell function'] = 50
                                        item_copy['timer icon'] = self.timer_image_surf
                                        self.spell_list.append(item_copy)
                                        item['locked'] = False
                                    else:
                                        break
                                    if item['name'] not in ['freeze', 'healing', 'rage']:
                                        item_copy['image'] = troop_image
                                        self.backpack_troop_list.append(item_copy)
                                    item['locked'] = False

                if self.backpack:
                    if self.back_button_rect.collidepoint(mouse_pos):
                        self.store = True
                        self.backpack = False

                for index, surface in enumerate(self.button_surf):
                    x_coord = self.x_button_coordinate[index]
                    y_coord = self.y_button_coordinate[index]
                    surface_rect = surface.get_rect(center=(x_coord, y_coord))
                    if surface_rect.collidepoint(mouse_pos):
                        if index == 0:
                            self.selected_category = 'Castle'
                        if index == 1:
                            self.screen.blit(self.title_background_dark_surf, surface_rect)
                            self.selected_category = "Troop"
                        elif index == 2:
                            self.screen.blit(self.title_background_dark_surf, surface_rect)
                            self.selected_category = 'Spell'
                        elif index == 3:
                            self.screen.blit(self.title_background_dark_surf, surface_rect)
                            self.selected_category = 'Others'

                if self.backpack and self.selected_category == 'Castle':
                    for item in self.castle_detail:
                        health_button_rect = item['upgrades button'].get_rect(bottomleft=(120, 550))
                        mining_button_rect = item['upgrades button'].get_rect(bottomleft=(340, 550))
                        if health_button_rect.collidepoint(mouse_pos):
                            if self.num_money >= item['health price']:
                                self.num_money -= item['health price']
                                item['health level'] += 1
                                item['health price'] += 100
                                item['health'] += 200
                        elif mining_button_rect.collidepoint(mouse_pos):
                            if self.num_money >= item['mining speed price']:
                                self.num_money -= item['mining speed price']
                                item['mining speed level'] += 1
                                item['mining speed price'] += 100
                                item['mining speed'] += 20

                if self.backpack and self.selected_category == 'Troop':
                    for item in self.backpack_troop_list:
                        troop_type = item['name']
                        troop_image = item['image']
                        position = self.troop_position[0].get(troop_type, (0, 0))
                        troop_rect = troop_image.get_rect(center=(position))
                        if troop_rect.collidepoint(mouse_pos):
                            if troop_type == 'warrior':
                                self.clicked_image_surf = 'warrior'
                            elif troop_type == 'archer':
                                self.clicked_image_surf = 'archer'
                            elif troop_type == 'sparta':
                                self.clicked_image_surf = 'sparta'
                            elif troop_type == 'wizard':
                                self.clicked_image_surf = 'wizard'
                            elif troop_type == 'giant':
                                self.clicked_image_surf = 'giant'

                if self.backpack and self.selected_category == 'Troop':
                    for item in self.backpack_troop_list:
                        if item['name'] == self.clicked_image_surf:
                            upgrades_button_rect = item['upgrades button'].get_rect(midbottom=(220, 565))
                            if upgrades_button_rect.collidepoint(mouse_pos):
                                if self.num_money >= item['upgrades price']:
                                    self.num_money -= item['upgrades price']

                                    troop_data = firebase.troop_storage.get(item['name'])
                                    if troop_data:
                                        item['upgrades price'] = max(item['upgrades price'] * (troop_data[1] / 2), item['upgrades price'] + 50)
                                        item['health'] += max(item['health'] * (troop_data[1] / 2), item['health'] + 50)
                                        item['attack damage'] += max(item['attack damage'] * (troop_data[1] / 2), item['attack damage'] + 50)
                                        item['level'] +=1
                                        troop_data[1] +=1

                            equip_button_rect = item['equip button'].get_rect(midbottom=(383, 565))
                            if equip_button_rect.collidepoint(mouse_pos):
                                if item['equip']:
                                    item['equip'] = False
                                else:
                                    item['equip'] = True
                
                if self.backpack and self.selected_category == 'Spell':
                    for item in self.spell_list:
                        spell_type = item['name']
                        spell_image = item['image']
                        position = self.spell_position[0].get(spell_type, (0,0))
                        spell_rect = spell_image.get_rect(center=(position))
                        if spell_rect.collidepoint(mouse_pos):
                            if spell_type == 'freeze':
                                self.clicked_spell_surf = 'freeze'
                            elif spell_type == 'healing':
                                self.clicked_spell_surf = 'healing'
                            elif spell_type == 'rage':
                                self.clicked_spell_surf = 'rage'

                if self.backpack and self.selected_category == 'Spell':
                     for item in self.spell_list:
                        if item['name'] == self.clicked_spell_surf:
                            upgrades_button_rect = item['upgrades button'].get_rect(midbottom=(220, 565))
                            if upgrades_button_rect.collidepoint(mouse_pos):
                                if self.num_money>= item['upgrades price']:
                                    self.num_money -= item['upgrades price']

                                    spell_data = firebase.spell_storage.get(item['name'])
                                    if spell_data:
                                        item['upgrades price'] +=  max(item['upgrades price'] * (spell_data[1] / 2), item['upgrades price'] + 50)
                                        item['spell function'] += 5
                                        item['level'] += 1

                            equip_button_rect = item['equip button'].get_rect(midbottom=(383, 565))
                            if equip_button_rect.collidepoint(mouse_pos):
                                if item['equip']:
                                    item['equip'] = False
                                else:
                                    item['equip'] = True
                if self.store:
                    if self.back_level_background_rect.collidepoint(mouse_pos):
                        self.go_level_py()
                
    def go_level_py(self):
        level_module = importlib.import_module("Level")
        level_select = level_module.GameLevel()
        level_select.run()
        exit()

    def backpack_screen(self):
        self.display_detail_info()
        for item in self.backpack_troop_list:
            if item['equip'] == True:
                if item['name'] == 'warrior':
                    warrior_equipped_surf = pygame.image.load('War of stick/Picture/stickman sword/stickman warrior card.png')
                    warrior_equipped_surf = pygame.transform.scale(warrior_equipped_surf, (50, 55))
                    warrior_equipped_rect = warrior_equipped_surf.get_rect(topleft=(290, 58))
                    self.screen.blit(warrior_equipped_surf, warrior_equipped_rect)
                    equipped = [warrior_equipped_surf, warrior_equipped_rect]
                if item['name'] == 'archer':
                    archer_equipped_surf = pygame.image.load('War of stick/Picture/stickman archer/stickman archer card.png')
                    archer_equipped_surf = pygame.transform.scale(archer_equipped_surf, (50, 55))
                    archer_equipped_rect = archer_equipped_surf.get_rect(topleft=(375, 58))
                    self.screen.blit(archer_equipped_surf, archer_equipped_rect)
                    equipped = [archer_equipped_surf, archer_equipped_rect]
                elif item['name'] == 'sparta':
                    sparta_equipped_surf = pygame.image.load('War of stick/Picture/stickman sparta/stickman sparta card.png')
                    sparta_equipped_surf = pygame.transform.scale(sparta_equipped_surf, (50, 55))
                    sparta_equipped_rect = sparta_equipped_surf.get_rect(topleft=(569, 58))
                    self.screen.blit(sparta_equipped_surf, sparta_equipped_rect)
                    equipped = [sparta_equipped_surf, sparta_equipped_rect]
                elif item['name'] == 'wizard':
                    wizard_equipped_surf = pygame.image.load('War of stick/Picture/stickman wizard/stickman wizard card.png')
                    wizard_equipped_surf = pygame.transform.scale(wizard_equipped_surf, (50, 55))
                    wizard_equipped_rect = wizard_equipped_surf.get_rect(topleft=(473, 58))
                    self.screen.blit(wizard_equipped_surf, wizard_equipped_rect)
                    equipped = [wizard_equipped_surf, wizard_equipped_rect]
                elif item['name'] == 'giant':
                    giant_equipped_surf = pygame.image.load('War of stick/Picture/stickman giant/stickman giant card.png')
                    giant_equipped_surf = pygame.transform.scale(giant_equipped_surf, (50, 55))
                    giant_equipped_rect = giant_equipped_surf.get_rect(topleft=(668, 58))
                    self.screen.blit(giant_equipped_surf, giant_equipped_rect)
                    equipped = [giant_equipped_surf, giant_equipped_rect]
                self.equipped_box.append(equipped)
        
        for item in self.spell_list :
            if item['equip'] == True:
                if item['name'] == 'freeze':
                    freeze_equipped_surf = self.cards.freeze_card_image_surf
                    freeze_equipped_surf = pygame.transform.scale(freeze_equipped_surf,(55,55))
                    freeze_equipped_rect = freeze_equipped_surf.get_rect(topleft=(290, 130))
                    self.screen.blit(freeze_equipped_surf, freeze_equipped_rect)
                    equipped = [freeze_equipped_surf, freeze_equipped_rect]
                    
                if item['name'] == 'healing':
                    healing_equipped_surf = self.cards.healing_card_image_surf
                    healing_equipped_surf = pygame.transform.scale(healing_equipped_surf,(55,55))
                    healing_equipped_rect = healing_equipped_surf.get_rect(topleft=(375, 130))
                    self.screen.blit(healing_equipped_surf, healing_equipped_rect)
                    equipped = [healing_equipped_surf, healing_equipped_rect]

                elif item['name'] == 'rage':
                    rage_equipped_surf = self.cards.rage_card_image_surf
                    rage_equipped_surf = pygame.transform.scale(rage_equipped_surf,(55,55))
                    rage_equipped_rect = rage_equipped_surf.get_rect(topleft=(473, 130))
                    self.screen.blit(rage_equipped_surf, rage_equipped_rect)
                    equipped = [rage_equipped_surf, rage_equipped_rect]

        self.troop_screen_blit()
        self.spell_screen_blit()

    def display_detail_info(self):
        self.button()
        self.screen.fill((50, 49, 47))
        self.screen.blit(self.backpack_background_surf, (100, 195))
        self.screen.blit(self.backpack_word_surf, self.backpack_word_rect)
        self.screen.blit(self.back_button_surf, self.back_button_rect)
        self.money_icon_rect = self.money_image_surf.get_rect(topright=(480, 214))
        self.screen.blit(self.money_image_surf, self.money_icon_rect)

        self.num_money_surf = self.font.render(str(self.num_money), True, 'Black')
        self.money_num_rect = self.num_money_surf.get_rect(topright=(460, 210))
        self.screen.blit(self.num_money_surf, self.money_num_rect)
        # equipment box
        self.screen.blit(self.troop_equipment_box_surf, self.troop_equipment_box_rect)
        self.screen.blit(self.spell_equipment_box_surf, self.spell_equipment_box_rect)

        # button
        for index, surface in enumerate(self.button_surf):
            button_x_coords = self.x_button_coordinate[index]
            button_y_coords = self.y_button_coordinate[index]
            surface_rect = surface.get_rect(center=(button_x_coords, button_y_coords))
            self.screen.blit(surface, surface_rect)

            # title word
        self.screen.blit(self.castle_word_surf, self.castle_word_rect)
        self.screen.blit(self.troop_word_surf, self.troop_word_rect)
        self.screen.blit(self.spell_word_surf, self.spell_word_rect)
        self.screen.blit(self.others_word_surf, self.others_word_rect)

        if self.backpack and self.selected_category == 'Castle':
            self.screen.fill((50, 49, 47))
            self.screen.blit(self.backpack_background_surf, (100, 195))
            self.screen.blit(self.backpack_word_surf, self.backpack_word_rect)
            self.screen.blit(self.back_button_surf, self.back_button_rect)

            self.money_icon_rect = self.money_image_surf.get_rect(topright=(480, 214))
            self.screen.blit(self.money_image_surf, self.money_icon_rect)

            self.num_money_surf = self.font.render(str(self.num_money), True, 'Black')
            self.money_num_rect = self.num_money_surf.get_rect(topright=(460, 210))
            self.screen.blit(self.num_money_surf, self.money_num_rect)

            self.screen.blit(self.troop_equipment_box_surf, self.troop_equipment_box_rect)
            self.screen.blit(self.spell_equipment_box_surf, self.spell_equipment_box_rect)

            for index, surface in enumerate(self.button_surf):
                button_x_coords = self.x_button_coordinate[index]
                button_y_coords = self.y_button_coordinate[index]
                surface_rect = surface.get_rect(center=(button_x_coords, button_y_coords))
                self.screen.blit(surface, surface_rect)

            for item in self.castle_detail:
                # display castle image
                self.screen.blit(item['image'], (80, 180))
                # Display the health icon
                health_icon_surf = item['health icon']
                health_icon_rect = health_icon_surf.get_rect(midleft=(375, 293))
                self.screen.blit(health_icon_surf, health_icon_rect)

                # display the health msg
                health_text = self.font.render(f"{str(item['health'])}", True, 'Black')
                health_text_rect = health_text.get_rect(midleft=(400, 295))
                self.screen.blit(health_text, health_text_rect)

                # display mining icon
                mining_icon_surf = item['mining icon']
                mining_icon_rect = mining_icon_surf.get_rect(midleft=(366, 335))
                self.screen.blit(mining_icon_surf, mining_icon_rect)

                # display mining speed msg
                mining_speed_text = self.font.render(f"{str(item['mining speed'])}", True, 'Black')
                mining_speed_text_rect = mining_speed_text.get_rect(midleft=(402, 337))
                self.screen.blit(mining_speed_text, mining_speed_text_rect)

                # display health upgrades button
                health_button_surf = item['upgrades button']
                health_button_rect = health_button_surf.get_rect(bottomleft=(118, 565))
                self.screen.blit(health_button_surf, health_button_rect)

                mining_button_surf = item['upgrades button']
                mining_button_rect = mining_button_surf.get_rect(bottomleft=(338, 565))
                self.screen.blit(mining_button_surf, mining_button_rect)

                # health upgrades detail
                health_upgrades_msg_surf = self.font.render(f"Health: Lv{str(item['health level'])}", True, 'Black')
                health_upgrades_msg_rect = health_upgrades_msg_surf.get_rect(bottomleft=(132, 530))
                self.screen.blit(health_upgrades_msg_surf, health_upgrades_msg_rect)

                health_upgrades_surf = self.price_font.render(f"Upgrade {str(item['health price'])}", True, 'Black')
                health_upgrades_rect = health_upgrades_surf.get_rect(bottomleft=(130, 555))
                self.screen.blit(health_upgrades_surf, health_upgrades_rect)

                health_money_icon_surf = item['money image']
                health_money_icon_rect = health_money_icon_surf.get_rect(bottomleft=(237, 549))
                self.screen.blit(health_money_icon_surf, health_money_icon_rect)

                mining_upgrades_msg_surf = self.font.render(f"Mining: Lv{str(item['mining speed level'])}", True, 'Black')
                mining_upgrades_msg_rect = mining_upgrades_msg_surf.get_rect(bottomleft=(352, 530))
                self.screen.blit(mining_upgrades_msg_surf, mining_upgrades_msg_rect)

                mining_upgrades_surf = self.price_font.render(f"Upgrade {str(item['mining speed price'])}", True, 'Black')
                mining_upgrades_rect = mining_upgrades_surf.get_rect(bottomleft=(350, 555))
                self.screen.blit(mining_upgrades_surf, mining_upgrades_rect)

                mining_money_icon_surf = item['money image']
                mining_money_icon_rect = mining_money_icon_surf.get_rect(bottomleft=(457, 549))
                self.screen.blit(mining_money_icon_surf, mining_money_icon_rect)

                right_part_castle_surf = item['image']
                right_part_castle_surf = pygame.transform.scale(right_part_castle_surf, (120, 120))
                right_part_castle_rect = right_part_castle_surf.get_rect(center=(565, 295))
                self.screen.blit(right_part_castle_surf, right_part_castle_rect)

                self.screen.blit(self.castle_word_surf, self.castle_word_rect)
                self.screen.blit(self.troop_word_surf, self.troop_word_rect)
                self.screen.blit(self.spell_word_surf, self.spell_word_rect)
                self.screen.blit(self.others_word_surf, self.others_word_rect)

        elif self.selected_category == 'Troop':
            for index, item in enumerate(self.backpack_troop_list):
                troop_type = item['name']
                troop_image = item['image']
                position = self.troop_position[0].get(troop_type, (0, 0))
                troop_rect = troop_image.get_rect(center=(position))
                self.screen.blit(troop_image, troop_rect)

                msg_position = self.troop_msg_position[0].get(troop_type, (0, 0))

                level_msg_surf = self.price_font.render(f"Level: {str(item['level'])}", True, 'White')
                level_msg_rect = level_msg_surf.get_rect(center=(msg_position))
                self.screen.blit(level_msg_surf, level_msg_rect)

        elif self.selected_category == 'Spell':
            for index, item in enumerate(self.spell_list):
                spell_type = item['name']
                spell_image = item['image']
                position = self.spell_position[0].get(spell_type, (0,0))
                spell_rect = spell_image.get_rect(center=(position))
                self.screen.blit(spell_image,spell_rect)

        elif self.selected_category == 'Others':
            pass

    def troop_screen_blit(self):
        if self.backpack and self.selected_category == 'Troop':
            for item in self.backpack_troop_list:
                if item['equip'] == True:
                    if item['name'] == 'warrior':
                        equipped_text = self.price_font.render("Equipped", True, (255, 255, 255))
                        equipped_text_rect = equipped_text.get_rect(midtop=(557, 330))
                        self.screen.blit(equipped_text, equipped_text_rect)
                    elif item['name'] == 'archer':
                        equipped_text = self.price_font.render("Equipped", True, (255, 255, 255))
                        equipped_text_rect = equipped_text.get_rect(midtop=(695, 330))
                        self.screen.blit(equipped_text, equipped_text_rect)
                    elif item['name'] == 'sparta':
                        equipped_text = self.price_font.render("Equipped", True, (255, 255, 255))
                        equipped_text_rect = equipped_text.get_rect(midtop=(829, 330))
                        self.screen.blit(equipped_text, equipped_text_rect)
                    elif item['name'] == 'wizard':
                        equipped_text = self.price_font.render("Equipped", True, (255, 255, 255))
                        equipped_text_rect = equipped_text.get_rect(midtop=(560, 445))
                        self.screen.blit(equipped_text, equipped_text_rect)
                    elif item['name'] == 'giant':
                        equipped_text = self.price_font.render("Equipped", True, (255, 255, 255))
                        equipped_text_rect = equipped_text.get_rect(midtop=(695, 445))
                        self.screen.blit(equipped_text, equipped_text_rect)

                if self.clicked_image_surf == 'warrior':
                    if item['name'] == 'warrior':
                        warrior_troop_image_surf = item['image']
                        warrior_troop_image_surf = pygame.transform.scale(warrior_troop_image_surf, (350, 350))
                        warrior_troop_image_rect = warrior_troop_image_surf.get_rect(midleft=(48, 380))
                        self.screen.blit(warrior_troop_image_surf, warrior_troop_image_rect)

                        troop_name_surf = self.title_font.render(f"{str(item['name'])}", True, 'White')
                        troop_name_rect = troop_name_surf.get_rect(midtop=(246, 198))
                        self.screen.blit(troop_name_surf, troop_name_rect)

                        gold_icon_surf = item['gold icon']
                        gold_icon_rect = gold_icon_surf.get_rect(midleft=(375, 293))
                        self.screen.blit(gold_icon_surf, gold_icon_rect)

                        gold_text_surf = self.font.render(str(300), True, 'White')
                        gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                        self.screen.blit(gold_text_surf, gold_text_rect)

                        diamond_icon_surf = item['diamond icon']
                        diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                        self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                        diamond_text_surf = self.font.render(str(400), True, "White")
                        diamond_text_rect = diamond_text_surf.get_rect(midleft=(406, 332))
                        self.screen.blit(diamond_text_surf, diamond_text_rect)

                        health_icon_surf = item['health icon']
                        health_icon_rect = health_icon_surf.get_rect(midleft=(376, 370))
                        self.screen.blit(health_icon_surf, health_icon_rect)

                        health_text_surf = self.font.render(f"{str(item['health'])}", True, 'White')
                        health_text_rect = health_text_surf.get_rect(midleft=(403, 371))
                        self.screen.blit(health_text_surf, health_text_rect)

                        damage_icon_surf = item['damage icon']
                        damage_icon_rect = damage_icon_surf.get_rect(midleft=(375, 407))
                        self.screen.blit(damage_icon_surf, damage_icon_rect)

                        damage_text_surf = self.font.render(f"{str(item['attack damage'])}", True, 'White')
                        damage_text_rect = damage_text_surf.get_rect(midleft=(405, 408))
                        self.screen.blit(damage_text_surf, damage_text_rect)

                        upgrades_button_surf = item['upgrades button']
                        upgrades_button_rect = upgrades_button_surf.get_rect(midbottom=(220, 565))
                        self.screen.blit(upgrades_button_surf, upgrades_button_rect)

                        level_msg_surf = self.font.render(f"Level: {str(item['level'])}", True, 'Black')
                        level_msg_rect = level_msg_surf.get_rect(bottomleft=(180, 530))
                        self.screen.blit(level_msg_surf, level_msg_rect)

                        level_upgrades_surf = self.price_font.render(f"Upgrade {str(item['upgrades price'])}", True, 'Black')
                        level_upgrades_rect = level_upgrades_surf.get_rect(topright=(265, 535))
                        self.screen.blit(level_upgrades_surf, level_upgrades_rect)

                        money_icon_surf = item['money']
                        money_icon_rect = money_icon_surf.get_rect(midleft=(270, 543))
                        self.screen.blit(money_icon_surf, money_icon_rect)

                        if item['equip'] == False:
                            equip_button_surf = item['equip button']
                            equip_button_rect = equip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(equip_button_surf, equip_button_rect)

                            equip_text = self.font.render("Equip", True, (255, 255, 255))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)
                        elif item['equip'] == True:
                            unequip_button_surf = item['unequip button']
                            unequip_button_rect = unequip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(unequip_button_surf, unequip_button_rect)

                            equip_text = self.font.render("Unequip", True, (0, 0, 0))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)

                elif self.clicked_image_surf == 'archer':
                    if item['name'] == 'archer':
                        archer_troop_image_surf = item['image']
                        archer_troop_image_surf = pygame.transform.scale(archer_troop_image_surf, (200, 200))
                        archer_troop_image_rect = archer_troop_image_surf.get_rect(midleft=(148, 355))
                        self.screen.blit(archer_troop_image_surf, archer_troop_image_rect)

                        troop_name_surf = self.title_font.render(f"{str(item['name'])}", True, 'White')
                        troop_name_rect = troop_name_surf.get_rect(midtop=(246, 198))
                        self.screen.blit(troop_name_surf, troop_name_rect)

                        gold_icon_surf = item['gold icon']
                        gold_icon_rect = gold_icon_surf.get_rect(midleft=(375, 293))
                        self.screen.blit(gold_icon_surf, gold_icon_rect)

                        gold_text_surf = self.font.render(str(300), True, 'White')
                        gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                        self.screen.blit(gold_text_surf, gold_text_rect)

                        diamond_icon_surf = item['diamond icon']
                        diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                        self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                        diamond_text_surf = self.font.render(str(400), True, "White")
                        diamond_text_rect = diamond_text_surf.get_rect(midleft=(406, 332))
                        self.screen.blit(diamond_text_surf, diamond_text_rect)

                        health_icon_surf = item['health icon']
                        health_icon_rect = health_icon_surf.get_rect(midleft=(376, 370))
                        self.screen.blit(health_icon_surf, health_icon_rect)

                        health_text_surf = self.font.render(f"{str(item['health'])}", True, 'White')
                        health_text_rect = health_text_surf.get_rect(midleft=(403, 371))
                        self.screen.blit(health_text_surf, health_text_rect)

                        damage_icon_surf = item['damage icon']
                        damage_icon_rect = damage_icon_surf.get_rect(midleft=(375, 407))
                        self.screen.blit(damage_icon_surf, damage_icon_rect)

                        damage_text_surf = self.font.render(f"{str(item['attack damage'])}", True, 'White')
                        damage_text_rect = damage_text_surf.get_rect(midleft=(405, 408))
                        self.screen.blit(damage_text_surf, damage_text_rect)

                        upgrades_button_surf = item['upgrades button']
                        upgrades_button_rect = upgrades_button_surf.get_rect(midbottom=(220, 565))
                        self.screen.blit(upgrades_button_surf, upgrades_button_rect)

                        level_msg_surf = self.font.render(f"Level: {str(item['level'])}", True, 'Black')
                        level_msg_rect = level_msg_surf.get_rect(bottomleft=(180, 530))
                        self.screen.blit(level_msg_surf, level_msg_rect)

                        level_upgrades_surf = self.price_font.render(f"Upgrade {str(item['upgrades price'])}", True, 'Black')
                        level_upgrades_rect = level_upgrades_surf.get_rect(topright=(265, 535))
                        self.screen.blit(level_upgrades_surf, level_upgrades_rect)

                        money_icon_surf = item['money']
                        money_icon_rect = money_icon_surf.get_rect(midleft=(270, 543))
                        self.screen.blit(money_icon_surf, money_icon_rect)

                        if item['equip'] == False:
                            equip_button_surf = item['equip button']
                            equip_button_rect = equip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(equip_button_surf, equip_button_rect)

                            equip_text = self.font.render("Equip", True, (255, 255, 255))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)
                        elif item['equip'] == True:
                            unequip_button_surf = item['unequip button']
                            unequip_button_rect = unequip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(unequip_button_surf, unequip_button_rect)

                            equip_text = self.font.render("Unequip", True, (0, 0, 0))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)

                elif self.clicked_image_surf == 'sparta':
                    if item['name'] == 'sparta':
                        sparta_troop_image_surf = item['image']
                        sparta_troop_image_surf = pygame.transform.scale(sparta_troop_image_surf, (280, 320))
                        sparta_troop_image_rect = sparta_troop_image_surf.get_rect(midleft=(80, 390))
                        self.screen.blit(sparta_troop_image_surf, sparta_troop_image_rect)

                        troop_name_surf = self.title_font.render(f"{str(item['name'])}", True, 'White')
                        troop_name_rect = troop_name_surf.get_rect(midtop=(246, 198))
                        self.screen.blit(troop_name_surf, troop_name_rect)

                        gold_icon_surf = item['gold icon']
                        gold_icon_rect = gold_icon_surf.get_rect(midleft=(375, 293))
                        self.screen.blit(gold_icon_surf, gold_icon_rect)

                        gold_text_surf = self.font.render(str(300), True, 'White')
                        gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                        self.screen.blit(gold_text_surf, gold_text_rect)

                        diamond_icon_surf = item['diamond icon']
                        diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                        self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                        diamond_text_surf = self.font.render(str(400), True, "White")
                        diamond_text_rect = diamond_text_surf.get_rect(midleft=(406, 332))
                        self.screen.blit(diamond_text_surf, diamond_text_rect)

                        health_icon_surf = item['health icon']
                        health_icon_rect = health_icon_surf.get_rect(midleft=(376, 370))
                        self.screen.blit(health_icon_surf, health_icon_rect)

                        health_text_surf = self.font.render(f"{str(item['health'])}", True, 'White')
                        health_text_rect = health_text_surf.get_rect(midleft=(403, 371))
                        self.screen.blit(health_text_surf, health_text_rect)

                        damage_icon_surf = item['damage icon']
                        damage_icon_rect = damage_icon_surf.get_rect(midleft=(375, 407))
                        self.screen.blit(damage_icon_surf, damage_icon_rect)

                        damage_text_surf = self.font.render(f"{str(item['attack damage'])}", True, 'White')
                        damage_text_rect = damage_text_surf.get_rect(midleft=(405, 408))
                        self.screen.blit(damage_text_surf, damage_text_rect)

                        upgrades_button_surf = item['upgrades button']
                        upgrades_button_rect = upgrades_button_surf.get_rect(midbottom=(220, 565))
                        self.screen.blit(upgrades_button_surf, upgrades_button_rect)

                        level_msg_surf = self.font.render(f"Level: {str(item['level'])}", True, 'Black')
                        level_msg_rect = level_msg_surf.get_rect(bottomleft=(180, 530))
                        self.screen.blit(level_msg_surf, level_msg_rect)

                        level_upgrades_surf = self.price_font.render(f"Upgrade {str(item['upgrades price'])}", True, 'Black')
                        level_upgrades_rect = level_upgrades_surf.get_rect(topright=(265, 535))
                        self.screen.blit(level_upgrades_surf, level_upgrades_rect)

                        money_icon_surf = item['money']
                        money_icon_rect = money_icon_surf.get_rect(midleft=(270, 543))
                        self.screen.blit(money_icon_surf, money_icon_rect)

                        if item['equip'] == False:
                            equip_button_surf = item['equip button']
                            equip_button_rect = equip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(equip_button_surf, equip_button_rect)

                            equip_text = self.font.render("Equip", True, (255, 255, 255))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)
                        elif item['equip'] == True:
                            unequip_button_surf = item['unequip button']
                            unequip_button_rect = unequip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(unequip_button_surf, unequip_button_rect)

                            equip_text = self.font.render("Unequip", True, (0, 0, 0))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)

                elif self.clicked_image_surf == 'wizard':
                    if item['name'] == 'wizard':
                        wizard_troop_image_surf = item['image']
                        wizard_troop_image_surf = pygame.transform.scale(wizard_troop_image_surf, (300, 350))
                        wizard_troop_image_rect = wizard_troop_image_surf.get_rect(midleft=(100, 408))
                        self.screen.blit(wizard_troop_image_surf, wizard_troop_image_rect)

                        troop_name_surf = self.title_font.render(f"{str(item['name'])}", True, 'White')
                        troop_name_rect = troop_name_surf.get_rect(midtop=(246, 198))
                        self.screen.blit(troop_name_surf, troop_name_rect)

                        gold_icon_surf = item['gold icon']
                        gold_icon_rect = gold_icon_surf.get_rect(midleft=(375, 293))
                        self.screen.blit(gold_icon_surf, gold_icon_rect)

                        gold_text_surf = self.font.render(str(300), True, 'White')
                        gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                        self.screen.blit(gold_text_surf, gold_text_rect)

                        diamond_icon_surf = item['diamond icon']
                        diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                        self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                        diamond_text_surf = self.font.render(str(400), True, "White")
                        diamond_text_rect = diamond_text_surf.get_rect(midleft=(406, 332))
                        self.screen.blit(diamond_text_surf, diamond_text_rect)

                        health_icon_surf = item['health icon']
                        health_icon_rect = health_icon_surf.get_rect(midleft=(376, 370))
                        self.screen.blit(health_icon_surf, health_icon_rect)

                        health_text_surf = self.font.render(f"{str(item['health'])}", True, 'White')
                        health_text_rect = health_text_surf.get_rect(midleft=(403, 371))
                        self.screen.blit(health_text_surf, health_text_rect)

                        damage_icon_surf = item['damage icon']
                        damage_icon_rect = damage_icon_surf.get_rect(midleft=(375, 407))
                        self.screen.blit(damage_icon_surf, damage_icon_rect)

                        damage_text_surf = self.font.render(f"{str(item['attack damage'])}", True, 'White')
                        damage_text_rect = damage_text_surf.get_rect(midleft=(405, 408))
                        self.screen.blit(damage_text_surf, damage_text_rect)

                        upgrades_button_surf = item['upgrades button']
                        upgrades_button_rect = upgrades_button_surf.get_rect(midbottom=(220, 565))
                        self.screen.blit(upgrades_button_surf, upgrades_button_rect)

                        level_msg_surf = self.font.render(f"Level: {str(item['level'])}", True, 'Black')
                        level_msg_rect = level_msg_surf.get_rect(bottomleft=(180, 530))
                        self.screen.blit(level_msg_surf, level_msg_rect)

                        level_upgrades_surf = self.price_font.render(f"Upgrade {str(item['upgrades price'])}", True, 'Black')
                        level_upgrades_rect = level_upgrades_surf.get_rect(topright=(265, 535))
                        self.screen.blit(level_upgrades_surf, level_upgrades_rect)

                        money_icon_surf = item['money']
                        money_icon_rect = money_icon_surf.get_rect(midleft=(270, 543))
                        self.screen.blit(money_icon_surf, money_icon_rect)

                        if item['equip'] == False:
                            equip_button_surf = item['equip button']
                            equip_button_rect = equip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(equip_button_surf, equip_button_rect)

                            equip_text = self.font.render("Equip", True, (255, 255, 255))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)
                        elif item['equip'] == True:
                            unequip_button_surf = item['unequip button']
                            unequip_button_rect = unequip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(unequip_button_surf, unequip_button_rect)

                            equip_text = self.font.render("Unequip", True, (0, 0, 0))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)

                elif self.clicked_image_surf == 'giant':
                    if item['name'] == 'giant':
                        giant_troop_image_surf = item['image']
                        giant_troop_image_surf = pygame.transform.scale(giant_troop_image_surf, (250, 300))
                        giant_troop_image_rect = giant_troop_image_surf.get_rect(midleft=(115, 380))
                        self.screen.blit(giant_troop_image_surf, giant_troop_image_rect)

                        troop_name_surf = self.title_font.render(f"{str(item['name'])}", True, 'White')
                        troop_name_rect = troop_name_surf.get_rect(midtop=(246, 198))
                        self.screen.blit(troop_name_surf, troop_name_rect)

                        gold_icon_surf = item['gold icon']
                        gold_icon_rect = gold_icon_surf.get_rect(midleft=(375, 293))
                        self.screen.blit(gold_icon_surf, gold_icon_rect)

                        gold_text_surf = self.font.render(str(300), True, 'White')
                        gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                        self.screen.blit(gold_text_surf, gold_text_rect)

                        diamond_icon_surf = item['diamond icon']
                        diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                        self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                        diamond_text_surf = self.font.render(str(400), True, "White")
                        diamond_text_rect = diamond_text_surf.get_rect(midleft=(406, 332))
                        self.screen.blit(diamond_text_surf, diamond_text_rect)

                        health_icon_surf = item['health icon']
                        health_icon_rect = health_icon_surf.get_rect(midleft=(376, 370))
                        self.screen.blit(health_icon_surf, health_icon_rect)

                        health_text_surf = self.font.render(f"{str(item['health'])}", True, 'White')
                        health_text_rect = health_text_surf.get_rect(midleft=(403, 371))
                        self.screen.blit(health_text_surf, health_text_rect)

                        damage_icon_surf = item['damage icon']
                        damage_icon_rect = damage_icon_surf.get_rect(midleft=(375, 407))
                        self.screen.blit(damage_icon_surf, damage_icon_rect)

                        damage_text_surf = self.font.render(f"{str(item['attack damage'])}", True, 'White')
                        damage_text_rect = damage_text_surf.get_rect(midleft=(405, 408))
                        self.screen.blit(damage_text_surf, damage_text_rect)

                        upgrades_button_surf = item['upgrades button']
                        upgrades_button_rect = upgrades_button_surf.get_rect(midbottom=(220, 565))
                        self.screen.blit(upgrades_button_surf, upgrades_button_rect)

                        level_msg_surf = self.font.render(f"Level: {str(item['level'])}", True, 'Black')
                        level_msg_rect = level_msg_surf.get_rect(bottomleft=(180, 530))
                        self.screen.blit(level_msg_surf, level_msg_rect)

                        level_upgrades_surf = self.price_font.render(f"Upgrade {str(item['upgrades price'])}", True, 'Black')
                        level_upgrades_rect = level_upgrades_surf.get_rect(topright=(265, 535))
                        self.screen.blit(level_upgrades_surf, level_upgrades_rect)

                        money_icon_surf = item['money']
                        money_icon_rect = money_icon_surf.get_rect(midleft=(270, 543))
                        self.screen.blit(money_icon_surf, money_icon_rect)

                        if item['equip'] == False:
                            equip_button_surf = item['equip button']
                            equip_button_rect = equip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(equip_button_surf, equip_button_rect)

                            equip_text = self.font.render("Equip", True, (255, 255, 255))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)
                        elif item['equip'] == True:
                            unequip_button_surf = item['unequip button']
                            unequip_button_rect = unequip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(unequip_button_surf, unequip_button_rect)

                            equip_text = self.font.render("Unequip", True, (0, 0, 0))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)

    def spell_screen_blit(self):
        if self.backpack and self.selected_category == 'Spell':
            for item in self.spell_list:
                if item['equip'] == True:
                    if item['name'] == 'freeze':
                        equipped_text = self.price_font.render("Equipped", True, (255, 255, 255))
                        equipped_text_rect = equipped_text.get_rect(midtop=(557, 330))
                        self.screen.blit(equipped_text, equipped_text_rect)
                    elif item['name'] == 'healing':
                        equipped_text = self.price_font.render("Equipped", True, (255, 255, 255))
                        equipped_text_rect = equipped_text.get_rect(midtop=(695, 330))
                        self.screen.blit(equipped_text, equipped_text_rect)
                    elif item['name'] == 'rage':
                        equipped_text = self.price_font.render("Equipped", True, (255, 255, 255))
                        equipped_text_rect = equipped_text.get_rect(midtop=(829, 330))
                        self.screen.blit(equipped_text, equipped_text_rect)

                if self.clicked_spell_surf =='freeze':
                    if item['name'] == 'freeze':
                        freeze_spell_image_surf = item['image']
                        freeze_spell_image_surf = pygame.transform.scale(freeze_spell_image_surf, (220, 220))
                        freeze_spell_image_rect = freeze_spell_image_surf.get_rect(midleft=(142, 375))
                        self.screen.blit(freeze_spell_image_surf, freeze_spell_image_rect)
                    
                        spell_name_surf = self.title_font.render(f"{str(item['name'])}", True, 'White')
                        spell_name_rect = spell_name_surf.get_rect(midtop=(246, 205))
                        self.screen.blit(spell_name_surf, spell_name_rect)

                        # gold_icon_surf = item['gold icon']
                        # gold_icon_rect = gold_icon_surf.get_rect(midleft=(375, 293))
                        # self.screen.blit(gold_icon_surf, gold_icon_rect)

                        # gold_text_surf = self.font.render(str(300), True, 'White')
                        # gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                        # self.screen.blit(gold_text_surf, gold_text_rect)

                        diamond_icon_surf = item['diamond icon']
                        diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                        self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                        diamond_text_surf = self.font.render(str(500), True, "White")
                        diamond_text_rect = diamond_text_surf.get_rect(midleft=(406, 332))
                        self.screen.blit(diamond_text_surf, diamond_text_rect)

                        timer_icon_surf = item['timer icon']
                        timer_icon_rect = timer_icon_surf.get_rect(midleft=(370, 370))
                        self.screen.blit(timer_icon_surf,timer_icon_rect)

                        timer_text_surf = self.font.render(f"{str(item['timer duration'])}s", True, "White")
                        timer_text_rect = timer_text_surf.get_rect(midleft=(410, 371))
                        self.screen.blit(timer_text_surf,timer_text_rect)

                        upgrades_button_surf = item['upgrades button']
                        upgrades_button_rect = upgrades_button_surf.get_rect(midbottom=(220, 565))
                        self.screen.blit(upgrades_button_surf, upgrades_button_rect)

                        level_msg_surf = self.font.render(f"Duration: Lv{str(item['level'])}", True, 'Black')
                        level_msg_rect = level_msg_surf.get_rect(bottomleft=(155, 530))
                        self.screen.blit(level_msg_surf, level_msg_rect)

                        level_upgrades_surf = self.price_font.render(f"Upgrade {str(item['upgrades price'])}", True, 'Black')
                        level_upgrades_rect = level_upgrades_surf.get_rect(topright=(265, 535))
                        self.screen.blit(level_upgrades_surf, level_upgrades_rect)

                        money_icon_surf = item['money']
                        money_icon_rect = money_icon_surf.get_rect(midleft=(270, 543))
                        self.screen.blit(money_icon_surf, money_icon_rect)

                        if item['equip'] == False:
                            equip_button_surf = item['equip button']
                            equip_button_rect = equip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(equip_button_surf, equip_button_rect)

                            equip_text = self.font.render("Equip", True, (255, 255, 255))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)
                        elif item['equip'] == True:
                            unequip_button_surf = item['unequip button']
                            unequip_button_rect = unequip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(unequip_button_surf, unequip_button_rect)

                            equip_text = self.font.render("Unequip", True, (0, 0, 0))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)

                elif self.clicked_spell_surf == 'healing':
                    if item['name'] == 'healing':
                        healing_spell_image_surf = item['image']
                        healing_spell_image_surf = pygame.transform.scale(healing_spell_image_surf, (220, 220))
                        healing_spell_image_rect = healing_spell_image_surf.get_rect(midleft=(142, 375))
                        self.screen.blit(healing_spell_image_surf, healing_spell_image_rect)
                    
                        spell_name_surf = self.title_font.render(f"{str(item['name'])}", True, 'White')
                        spell_name_rect = spell_name_surf.get_rect(midtop=(246, 205))
                        self.screen.blit(spell_name_surf, spell_name_rect)

                        # gold_icon_surf = item['gold icon']
                        # gold_icon_rect = gold_icon_surf.get_rect(midleft=(375, 293))
                        # self.screen.blit(gold_icon_surf, gold_icon_rect)

                        # gold_text_surf = self.font.render(str(300), True, 'White')
                        # gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                        # self.screen.blit(gold_text_surf, gold_text_rect)

                        diamond_icon_surf = item['diamond icon']
                        diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                        self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                        diamond_text_surf = self.font.render(str(500), True, "White")
                        diamond_text_rect = diamond_text_surf.get_rect(midleft=(406, 332))
                        self.screen.blit(diamond_text_surf, diamond_text_rect)

                        timer_icon_surf = item['timer icon']
                        timer_icon_rect = timer_icon_surf.get_rect(midleft=(370, 370))
                        self.screen.blit(timer_icon_surf,timer_icon_rect)

                        timer_text_surf = self.font.render(f"{str(item['timer duration'])}s", True, "White")
                        timer_text_rect = timer_text_surf.get_rect(midleft=(410, 371))
                        self.screen.blit(timer_text_surf,timer_text_rect)

                        upgrades_button_surf = item['upgrades button']
                        upgrades_button_rect = upgrades_button_surf.get_rect(midbottom=(220, 565))
                        self.screen.blit(upgrades_button_surf, upgrades_button_rect)

                        level_msg_surf = self.font.render(f"Duration: Lv{str(item['level'])}", True, 'Black')
                        level_msg_rect = level_msg_surf.get_rect(bottomleft=(155, 530))
                        self.screen.blit(level_msg_surf, level_msg_rect)

                        level_upgrades_surf = self.price_font.render(f"Upgrade {str(item['upgrades price'])}", True, 'Black')
                        level_upgrades_rect = level_upgrades_surf.get_rect(topright=(265, 535))
                        self.screen.blit(level_upgrades_surf, level_upgrades_rect)

                        money_icon_surf = item['money']
                        money_icon_rect = money_icon_surf.get_rect(midleft=(270, 543))
                        self.screen.blit(money_icon_surf, money_icon_rect)

                        if item['equip'] == False:
                            equip_button_surf = item['equip button']
                            equip_button_rect = equip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(equip_button_surf, equip_button_rect)

                            equip_text = self.font.render("Equip", True, (255, 255, 255))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)
                        elif item['equip'] == True:
                            unequip_button_surf = item['unequip button']
                            unequip_button_rect = unequip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(unequip_button_surf, unequip_button_rect)

                            equip_text = self.font.render("Unequip", True, (0, 0, 0))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)

                elif self.clicked_spell_surf == 'rage':
                    if item['name'] == 'rage':
                        rage_spell_image_surf = item['image']
                        rage_spell_image_surf = pygame.transform.scale(rage_spell_image_surf, (220, 220))
                        rage_spell_image_rect = rage_spell_image_surf.get_rect(midleft=(142, 375))
                        self.screen.blit(rage_spell_image_surf, rage_spell_image_rect)
                    
                        spell_name_surf = self.title_font.render(f"{str(item['name'])}", True, 'White')
                        spell_name_rect = spell_name_surf.get_rect(midtop=(246, 205))
                        self.screen.blit(spell_name_surf, spell_name_rect)

                        # gold_icon_surf = item['gold icon']
                        # gold_icon_rect = gold_icon_surf.get_rect(midleft=(375, 293))
                        # self.screen.blit(gold_icon_surf, gold_icon_rect)

                        # gold_text_surf = self.font.render(str(500), True, 'White')
                        # gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                        # self.screen.blit(gold_text_surf, gold_text_rect)

                        diamond_icon_surf = item['diamond icon']
                        diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                        self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                        diamond_text_surf = self.font.render(str(400), True, "White")
                        diamond_text_rect = diamond_text_surf.get_rect(midleft=(406, 332))
                        self.screen.blit(diamond_text_surf, diamond_text_rect)

                        timer_icon_surf = item['timer icon']
                        timer_icon_rect = timer_icon_surf.get_rect(midleft=(370, 370))
                        self.screen.blit(timer_icon_surf,timer_icon_rect)

                        timer_text_surf = self.font.render(f"{str(item['timer duration'])}s", True, "White")
                        timer_text_rect = timer_text_surf.get_rect(midleft=(410, 371))
                        self.screen.blit(timer_text_surf,timer_text_rect)

                        upgrades_button_surf = item['upgrades button']
                        upgrades_button_rect = upgrades_button_surf.get_rect(midbottom=(220, 565))
                        self.screen.blit(upgrades_button_surf, upgrades_button_rect)

                        level_msg_surf = self.font.render(f"Duration: Lv{str(item['level'])}", True, 'Black')
                        level_msg_rect = level_msg_surf.get_rect(bottomleft=(155, 530))
                        self.screen.blit(level_msg_surf, level_msg_rect)

                        level_upgrades_surf = self.price_font.render(f"Upgrade {str(item['upgrades price'])}", True, 'Black')
                        level_upgrades_rect = level_upgrades_surf.get_rect(topright=(265, 535))
                        self.screen.blit(level_upgrades_surf, level_upgrades_rect)

                        money_icon_surf = item['money']
                        money_icon_rect = money_icon_surf.get_rect(midleft=(270, 543))
                        self.screen.blit(money_icon_surf, money_icon_rect)

                        if item['equip'] == False:
                            equip_button_surf = item['equip button']
                            equip_button_rect = equip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(equip_button_surf, equip_button_rect)

                            equip_text = self.font.render("Equip", True, (255, 255, 255))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)
                        elif item['equip'] == True:
                            unequip_button_surf = item['unequip button']
                            unequip_button_rect = unequip_button_surf.get_rect(midbottom=(383, 565))
                            self.screen.blit(unequip_button_surf, unequip_button_rect)

                            equip_text = self.font.render("Unequip", True, (0, 0, 0))
                            equip_text_rect = equip_text.get_rect(midtop=(380, 520))
                            self.screen.blit(equip_text, equip_text_rect)

    def game_start(self):
        if self.store:
            self.screen.blit(self.background_surf, (0, 0))
            self.screen.blit(self.topic_word_surf, self.topic_word_rect)

            self.screen.blit(self.backpack_image_surf, self.backpack_image_rect)
            self.screen.blit(self.money_image_surf, self.money_image_rect)
            self.num_money_surf = self.font.render(str(self.num_money), True, 'Black')
            self.screen.blit(self.num_money_surf, self.num_money_rect)

            self.screen.blit(self.back_level_background_surf,self.back_level_background_rect)
            self.screen.blit(self.back_level_button_surf,self.back_level_button_rect)
            self.screen.blit(self.level_word_surf,self.level_word_rect)

            for index, item in enumerate(self.store_list):
                if item['locked'] == True and index < len(self.x_coords):
                    card_image = item['image']
                    card_rect = card_image.get_rect(center=(self.x_coords[index], self.y_coords[index]))
                    self.screen.blit(card_image, card_rect)

                    text = self.font.render(f"{item['name'].capitalize()}", True, 'Red')
                    text_rect = text.get_rect(center=(self.x_coords[index], self.y_coords[index] - 50))
                    self.screen.blit(text, text_rect)

                    button_background_surf = item['button']
                    button_background_rect = button_background_surf.get_rect(
                        center=(self.x_coords[index], self.y_coords[index] + 45))
                    self.screen.blit(button_background_surf, button_background_rect)

                    money_image_surf = item['money']
                    money_image_rect = money_image_surf.get_rect(center=(self.x_coords[index] + 20, self.y_coords[index] + 45))
                    self.screen.blit(money_image_surf, money_image_rect)

                    price_text_surf = self.price_font.render(str(item['price']), True, 'Black')
                    price_text_rect = price_text_surf.get_rect(center=(self.x_coords[index] - 7, self.y_coords[index] + 46))
                    self.screen.blit(price_text_surf, price_text_rect)
                
                else:
                    card_image = item['image']
                    card_rect = card_image.get_rect(center=(self.x_coords[index], self.y_coords[index]))
                    self.screen.blit(card_image, card_rect)

                    text = self.font.render(f"{item['name'].capitalize()}", True, 'Red')
                    text_rect = text.get_rect(center=(self.x_coords[index], self.y_coords[index] - 50))
                    self.screen.blit(text, text_rect)

                    button_background_surf = item['button']
                    button_background_surf = pygame.transform.scale(button_background_surf,(225,75))
                    button_background_rect = button_background_surf.get_rect(
                        center=(self.x_coords[index] - 5, self.y_coords[index] + 45))
                    self.screen.blit(button_background_surf, button_background_rect)

                    unlocked_text_surf = self.price_font.render('Uncloked', True, 'Black')
                    unlocked_text_rect = unlocked_text_surf.get_rect(center=(self.x_coords[index] - 7, self.y_coords[index] + 46))
                    self.screen.blit(unlocked_text_surf,unlocked_text_rect)

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
    Game_Store().run()
