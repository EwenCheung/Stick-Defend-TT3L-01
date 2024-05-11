# coding : utf-8
import pygame
from sys import exit
from random import choice

pygame.init()

class TroopButton:
    def __init__(self, image, image_dim, flash, size, position, name, cooldown_time):
        self.size = size
        self.position = position
        self.image = image
        self.image_dim = image_dim
        self.flash = flash
        self.image = pygame.transform.scale(self.image, self.size)
        self.image_dim = pygame.transform.scale(self.image_dim, self.size)
        self.flash = pygame.transform.scale(self.flash, self.size)
        self.name = name
        self.cooldown_time = cooldown_time
        self.rect = self.image.get_rect(center=self.position)
        self.clicked = False
        self.cooldown_flag = False
        self.coordinate_x = 0
        self.last_clicked_time = 0
        self.remaining_cooldown = 0
        self.insufficient_currency = False
        # self.flash_timer = 0
        # self.flash_duration = 500
        # self.flash_toggle = False

    def render_name(self, screen):
        font = pygame.font.Font(None, 15)
        lines = self.name.split('\n')
        total_height = len(lines) * 15
        y_offset = -total_height / 2

        colors = [(255, 215, 0), (56, 182, 255)]  # gold, blue
        for line, color in zip(lines, colors):
            text = font.render(line, True, color)
            text_rect = text.get_rect(center=(self.position[0], self.position[1] + y_offset))
            text_rect.y += 46
            screen.blit(text, text_rect)
            y_offset += 8

    def draw(self, screen):
        if self.clicked and not self.insufficient_currency:
            self.cooldown_flag = True
            current_time = pygame.time.get_ticks()
            self.remaining_cooldown = max(0, self.cooldown_time - (current_time - self.last_clicked_time)) // 1000
            cooldown_font = pygame.font.Font(None, 70)
            cooldown_text = cooldown_font.render(f"{self.remaining_cooldown}", True, (255, 255, 255))
            cooldown_text_rect = cooldown_text.get_rect(center=(self.position[0], self.position[1]))
            screen.blit(self.image_dim, self.rect)
            screen.blit(cooldown_text, cooldown_text_rect)

        # if self.insufficient_currency and self.flash_toggle:
        #     if self.flash_timer <= self.flash_duration:
        #         screen.blit(self.flash, self.rect)
        #         self.flash_timer += 1
        #     else:
        #         self.flash_timer = 0
        #         self.insufficient_currency = False
        #         self.clicked = False
        #         self.cooldown_flag = False

        if self.remaining_cooldown == 0 and not self.insufficient_currency:
            screen.blit(self.image, self.rect)
            self.clicked = False
        self.render_name(screen)
            
    def is_clicked(self, mouse_pos):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_clicked_time >= self.cooldown_time:
            if self.rect.collidepoint(mouse_pos):
                self.clicked = True
                self.last_clicked_time = current_time
                # if self.insufficient_currency:
                #     self.flash_visible = not self.flash_visible
                #     self.insufficient_currency = False
                #     self.flash_visible = False
                return True
        return False
    
    def lack_currency(self, screen):
        if self.insufficient_currency:
            # self.draw(screen)
            screen.blit(self.flash, self.rect)
            self.insufficient_currency = False
            self.clicked = False
            self.cooldown_flag = False

class Troop:
    def __init__(self, frame_storage, attack_frame_storage, health, attack_damage, speed, troop_width, troop_height, troop_name):
        self.previous_coor = 0
        self.coordinate_x = 0
        self.animation_index = 0
        self.frame_storage = frame_storage
        self.troop_name = troop_name
        self.image = self.frame_storage[self.animation_index]
        self.attacking = False
        self.attack_frame_index = 0
        self.attack_frame_storage = attack_frame_storage
        self.image = self.attack_frame_storage[self.attack_frame_index]
        self.health = health
        self.attack_damage = attack_damage
        self.speed = speed
        self.troop_width = troop_width
        self.troop_height = troop_height
        # self.health_duration = 5000
        # self.health_start_time = 0
        # self.health_active = False
        # self.rage_duration = 5000
        # self.rage_start_time = 0
        # self.rage_active = False
        # communication between the Troop instance and the Game instance
        self.communication = self
        self.rect = (0, 0, 0, 0)
        self.bullet_on_court = []

    def spawn_troop(self, screen, bg_x):
        self.rect = self.image.get_rect(bottomright=(self.coordinate_x + bg_x, 500))
        screen.blit(self.image, self.rect)

    def update(self):
        self.previous_coor = self.coordinate_x
        self.coordinate_x += self.speed
        self.animation_index += self.speed / 5
        if self.animation_index >= len(self.frame_storage):
            self.animation_index = 0
        self.image = self.frame_storage[int(self.animation_index)]

    def troop_attack(self):
        if self.troop_name == 'Archer' or self.troop_name == 'Wizard':
            self.create_bullet(0)
            self.coordinate_x = self.previous_coor
            self.attack_frame_index += 0.2
        else:
            self.coordinate_x = self.previous_coor
            self.attack_frame_index += 0.2

    def attack(self):
        self.attacking = True
        if self.attacking:
            self.troop_attack()
            if self.attack_frame_index >= len(self.attack_frame_storage):
                self.attack_frame_index = 0
                self.attacking = False
            self.image = self.attack_frame_storage[int(self.attack_frame_index)]

    def create_bullet(self, bg_x):
        self.rect = self.image.get_rect(bottomright=(self.coordinate_x + bg_x, 500))
        if self.troop_name == 'Archer':
            self.bullet = pygame.image.load('War of stick/Picture/utils/archer_bullet.png')
            self.bullet_surf = pygame.transform.scale(self.bullet, (50,50))
            self.bullet_surf = self.bullet_surf.get_rect(center=self.rect.center)     
            new_bullet = self.bullet_surf
        elif self.troop_name == 'Wizard':
            self.bullet = pygame.image.load('War of stick/Picture/utils/wizard_bullet.png')
            self.bullet_surf = pygame.transform.scale(self.bullet, (50,50))
            self.bullet_surf = self.bullet_surf.get_rect(center=self.rect.center)     
            new_bullet = self.bullet_surf
        self.bullet_on_court.append(new_bullet)

    def move_bullet(self):
        for bullet_rect in self.bullet_on_court:
            bullet_rect.x += 5  # Move the bullet to the right of troop
            if bullet_rect.x > 1030:
                # Remove bullets that have moved off-screen
                self.bullet_on_court.remove(bullet_rect)

    # def cast_health(self):
    #     self.health_active = True
    #     self.health_start_time = pygame.time.get_ticks()

    # def health_increase(self):
    #     if self.health_active:
    #         self.health *= 1.1
    #         if self.health_start_time >= self.health_duration:
    #             self.health /= 1.1
    #         self.health_active = False

    # def cast_rage(self):
    #     self.rage_active = True
    #     self.rage_start_time = pygame.time.get_ticks()

    # def speed_increase(self):
    #     if self.rage_active:
    #         self.speed *= 2
    #         if self.rage_start_time >= self.rage_duration:
    #             self.speed *= 0.5
    #         self.rage_active = False
        
    def take_damage(self, damage):
        self.health -= damage

class Ninja:
    def __init__(self, ninja_type, frame_storage, ninja_attack_frame_storage, ninja_health, ninja_speed, attack, ninja_coordinate_x):
        self.ninja_type = ninja_type
        self.frame_storage = frame_storage
        self.ninja_attack_frame_storage = ninja_attack_frame_storage
        self.ninja_health = ninja_health
        self.ninja_speed = ninja_speed
        self.attack = attack
        self.animation_index = 0
        self.image = self.frame_storage[self.animation_index]
        self.animation_attack_index = 0
        self.image = self.ninja_attack_frame_storage[self.animation_attack_index]
        self.communication = self
        self.ninja_coordinate_x = ninja_coordinate_x
        self.ninja_prev_coor = self.ninja_coordinate_x
        self.ninja_attacking = False
        self.rect = (0, 0, 0, 0)
        # self.freeze_duration = 5000
        # self.freeze_start_time = 0
        # self.freeze_active = False

    def spawn_ninja(self, screen, bg_x):
        self.rect = self.image.get_rect(bottomright=(self.ninja_coordinate_x + bg_x, 500))
        screen.blit(self.image, self.rect)

    def update_ninja(self):
        self.ninja_prev_coor = self.ninja_coordinate_x
        self.ninja_coordinate_x -= self.ninja_speed
        self.animation_index += self.ninja_speed / 10
        if self.animation_index >= len(self.ninja_attack_frame_storage):
            self.animation_index = 0
        self.image = self.frame_storage[int(self.animation_index)]

    def ninja_attack(self):
        self.ninja_attacking = True
        if self.ninja_attacking:
            self.ninja_coordinate_x = self.ninja_prev_coor
            self.animation_attack_index += 0.2
            if self.animation_attack_index >= len(self.ninja_attack_frame_storage):
                self.animation_attack_index = 0
                self.ninja_attacking = False
            self.image = self.ninja_attack_frame_storage[int(self.animation_attack_index)]

    # def cast_freeze(self):
    #     self.freeze_active = True
    #     self.freeze_start_time = pygame.time.get_ticks()

    # def ninja_speed_decrease(self):
    #     if Game().spell_active:
    #         self.ninja_speed *= 0.5
    #         self.freeze_over()

    # def freeze_over(self):
    #     current_time = pygame.time.get_ticks()
    #     if current_time - Game().start_time >= Game().spell_duration:
    #             self.ninja_speed *= 2
    #             return Game().spell_active == False

    def ninja_take_damage(self, taken_damage):
        self.ninja_health -= taken_damage               

class HealthBar:
    def __init__(self, max_health, initial_health, position, width, height, color):
        self.max_health = max_health
        self.current_health = initial_health
        self.position = position
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        # Draw inside the border box
        health_width = self.current_health / self.max_health * self.width
        health_bar_rect = pygame.Rect(self.position[0], self.position[1], health_width, self.height)
        pygame.draw.rect(screen, self.color, health_bar_rect)

        # Draw borderline
        health_bar_border_rect = pygame.Rect(self.position[0] - 2, self.position[1] - 2, self.width + 4, self.height + 4)
        pygame.draw.rect(screen, (0, 0, 0), health_bar_border_rect, 2)

    def update_health(self, get_damage):
        self.current_health -= get_damage
        self.current_health = max(0, self.current_health)

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tower Defend')  # title name
        self.screen = pygame.display.set_mode((1000, 600))
        self.bg_x = 0
        self.scroll_speed = 10
        self.num_gold = 1000000
        self.num_diamond = 100000
        self.gold_time = pygame.time.get_ticks()
        self.diamond_time = pygame.time.get_ticks()
        self.gold_interval = 100
        self.diamond_interval = 100
        self.troop_on_court = []
        self.enemy_on_court = []
        self.bullet_on_court = []
        self.health_bar_user = HealthBar(10000, 10000, (620, 530), 200, 20, (0, 255, 0))  # health bar
        self.health_bar_enemy = HealthBar(10000, 10000, (620, 560), 200, 20, (255, 0, 0))
        self.healing_initial_position = (35, 550)
        self.freeze_initial_position = (105, 550)
        self.rage_initial_position = (175, 550)
        self.game_over = False
        self.winner = None
        self.chosen_spell = None

        # set up Ninja timer
        self.ninja_timer = pygame.USEREVENT + 1
        self.spawn_time = 3000
        pygame.time.set_timer(self.ninja_timer, self.spawn_time)
        self.ninja_choice = ["naruto", "kakashi", "sasuke"]
        # Scrolling Background
        self.background_image = pygame.image.load('War of stick/Picture/utils/map.jpg')
        self.left_rect_castle = pygame.Rect(self.bg_x, 90, 170, 390)
        self.right_rect_castle = pygame.Rect(self.bg_x + self.background_image.get_width() - 100, 90, 170,
                                             390)  # distance between troop and castle during time

        # spell equipment
        self.box = pygame.image.load('War of stick/Picture/utils/box.png')
        self.box_surf = pygame.transform.scale(self.box, (600, 80))
        self.box_rect = self.box_surf.get_rect(center=(300, 550))

        self.healing_spell = pygame.image.load('War of stick/Picture/spell/healing_spell.png')
        self.healing_spell_surf = pygame.transform.scale(self.healing_spell, (70, 70))
        self.healing_spell_rect = self.healing_spell_surf.get_rect(center=self.healing_initial_position)
        self.freeze_spell = pygame.image.load('War of stick/Picture/spell/freeze_spell.png')
        self.freeze_spell_surf = pygame.transform.scale(self.freeze_spell, (70, 70))
        self.freeze_spell_rect = self.freeze_spell_surf.get_rect(center=self.freeze_initial_position)
        self.rage_spell = pygame.image.load('War of stick/Picture/spell/rage_spell.png')
        self.rage_spell_surf = pygame.transform.scale(self.rage_spell, (70, 70))
        self.rage_spell_rect = self.rage_spell_surf.get_rect(center=self.rage_initial_position)

        # Gold assets
        self.pic_gold = pygame.image.load('War of stick/Picture/utils/gold.png').convert_alpha()
        self.pic_gold_surf = pygame.transform.scale(self.pic_gold, (25, 25))
        self.pic_gold_rect = self.pic_gold_surf.get_rect(center=(760, 50))
        self.num_gold_font = pygame.font.Font(None, 30)
        self.num_gold_surf = self.num_gold_font.render(str(self.num_gold), True, 'Black')
        self.num_gold_rect = self.num_gold_surf.get_rect(center=(800, 50))

        # Diamond assets
        self.pic_diamond = pygame.image.load('War of stick/Picture/utils/diamond.png').convert_alpha()
        self.pic_diamond_surf = pygame.transform.scale(self.pic_diamond, (50, 25))
        self.pic_diamond_rect = self.pic_diamond_surf.get_rect(center=(760, 80))
        self.num_diamond_font = pygame.font.Font(None, 30)
        self.num_diamond_surf = self.num_diamond_font.render(str(self.num_diamond), True, 'Black')
        self.num_diamond_rect = self.num_diamond_surf.get_rect(center=(800, 80))

        # Troop One
        # Warrior run
        self.warrior_all_image = [
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 1.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 2.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 3.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 4.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 5.png').convert_alpha()]
        self.warrior_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.warrior_all_image]

        # Warrior attack
        self.warrior_attack_image = [
            pygame.image.load(
                'War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 1.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 2.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 3.png').convert_alpha()]
        self.warrior_attack_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.warrior_attack_image]

        self.warrior_button_image = pygame.image.load('War of stick/Picture/button/sword_button.png')
        self.warrior_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/sword_dim.png')
        self.warrior_button_flash = pygame.image.load('War of stick/Picture/button_flash/warrior_flash.png')
        self.warrior_button = TroopButton(self.warrior_button_image, self.warrior_button_dim_image, self.warrior_button_flash,
                                          (100, 100), (100, 70), '100\n200', 3000)

        # Troop Two
        # Archer walk
        self.archer_all_image = [pygame.image.load('War of stick/Picture/stickman archer/stickman archer 1.png').convert_alpha(),
                                 pygame.image.load('War of stick/Picture/stickman archer/stickman archer 2.png').convert_alpha()]
        self.archer_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.archer_all_image]

        # archer attack
        self.archer_attack_image = [
            pygame.image.load('War of stick/Picture/stickman archer/stickman archer 1.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman archer/stickman archer 1.png').convert_alpha()]
        self.archer_attack_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.archer_attack_image]

        self.archer_button_image = pygame.image.load('War of stick/Picture/button/archer_button.png')
        self.archer_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/archer_dim.png')
        self.archer_button_flash = pygame.image.load('War of stick/Picture/button_flash/archer_flash.png')
        self.archer_button = TroopButton(self.archer_button_image, self.archer_button_dim_image, self.archer_button_flash,
                                         (100, 100), (200, 70), '300\n200', 3000)

        # Troop Three
        # Wizard walk
        self.wizard_all_image = [
            pygame.image.load(
                'War of stick/Picture/stickman wizard/stickman wizard walk/stickman wizard walk 1.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman wizard/stickman wizard walk/stickman wizard walk 2.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman wizard/stickman wizard walk/stickman wizard walk 3.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman wizard/stickman wizard walk/stickman wizard walk 4.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman wizard/stickman wizard walk/stickman wizard walk 5.png').convert_alpha()
        ]
        self.wizard_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.wizard_all_image]

        # Wizard run
        self.wizard_attack_image = [
            pygame.image.load(
                'War of stick/Picture/stickman wizard/stickman wizard attack/stickman wizard attack 1.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman wizard/stickman wizard attack/stickman wizard attack 2.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman wizard/stickman wizard attack/stickman wizard attack 3.png').convert_alpha()
        ]
        self.wizard_attack_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.wizard_attack_image]

        self.wizard_button_image = pygame.image.load('War of stick/Picture/button/wizard_button.png')
        self.wizard_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/wizard_dim.png')
        self.wizard_button_flash = pygame.image.load('War of stick/Picture/button_flash/wizard_flash.png')
        self.wizard_button = TroopButton(self.wizard_button_image, self.wizard_button_dim_image, self.wizard_button_flash,
                                         (100, 100), (300, 70), '500\n500', 3000)
        # Troop Four
        # Sparta run
        self.sparta_all_image = [
            pygame.image.load(
                'War of stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 1.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 2.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 3.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 4.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 5.png').convert_alpha()
        ]
        self.sparta_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.sparta_all_image]

        # Sparta attack
        self.sparta_attack_image = [
            pygame.image.load(
                'War of stick/Picture/stickman sparta/stickman sparta attack/stickman sparta attack 1.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman sparta/stickman sparta attack/stickman sparta attack 2.png').convert_alpha()
        ]
        self.sparta_attack_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.sparta_attack_image]

        self.sparta_button_image = pygame.image.load('War of stick/Picture/button/sparta_button.png')
        self.sparta_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/sparta_dim.png')
        self.sparta_button_flash = pygame.image.load('War of stick/Picture/button_flash/sparta_flash.png')
        self.sparta_button = TroopButton(self.sparta_button_image, self.sparta_button_dim_image, self.sparta_button_flash,
                                         (100, 100), (400, 70), '700\n200', 3000)

        # Troop Five
        # Giant Walk
        self.giant_all_image = [
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 1.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 2.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 3.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 4.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 5.png').convert_alpha()]
        self.giant_frame_storage = [pygame.transform.scale(frame, (150, 200)) for frame in self.giant_all_image]

        # Giant Attack
        self.giant_attack_image = [
            pygame.image.load(
                'War of stick/Picture/stickman giant/stickman giant attack/stickman Giant attack 1.png').convert_alpha(),
            pygame.image.load(
                'War of stick/Picture/stickman giant/stickman giant attack/stickman Giant attack 2.png').convert_alpha()]
        self.giant_attack_frame_storage = [pygame.transform.scale(frame, (150, 200)) for frame in self.giant_attack_image]

        self.giant_button_image = pygame.image.load('War of stick/Picture/button/giant_button.png').convert_alpha()
        self.giant_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/giant_dim.png')
        self.giant_button_flash = pygame.image.load('War of stick/Picture/button_flash/giant_flash.png')
        self.giant_button = TroopButton(self.giant_button_image, self.giant_button_dim_image, self.giant_button_flash, (100, 100),
                                        (500, 70), '700\n200', 3000)

        self.naruto_normal = [pygame.image.load('Plant vs Stick/Picture/naruto/naruto_walk_1.png').convert_alpha(),
                              pygame.image.load('Plant vs Stick/Picture/naruto/naruto_walk_2.png').convert_alpha(),
                              pygame.image.load('Plant vs Stick/Picture/naruto/naruto_walk_3.png').convert_alpha()]
        self.naruto_attack = [pygame.image.load('Plant vs Stick/Picture/naruto/naruto_attack_1.png').convert_alpha(),
                              pygame.image.load('Plant vs Stick/Picture/naruto/naruto_attack_2.png').convert_alpha()]
        self.naruto_frame_storage = [pygame.transform.scale(frame, (84, 45)) for frame in self.naruto_normal]
        self.naruto_attack_frame_storage = [pygame.transform.scale(frame, (84, 45)) for frame in self.naruto_attack]

        self.sasuke_normal = [pygame.image.load('Plant vs Stick/Picture/sasuke/sasuke_walk_1.png').convert_alpha(),
                              pygame.image.load('Plant vs Stick/Picture/sasuke/sasuke_walk_2.png').convert_alpha(),
                              pygame.image.load('Plant vs Stick/Picture/sasuke/sasuke_walk_3.png').convert_alpha()]
        self.sasuke_attack = [pygame.image.load('Plant vs Stick/Picture/sasuke/sasuke_attack_1.png').convert_alpha(),
                              pygame.image.load('Plant vs Stick/Picture/sasuke/sasuke_attack_2.png').convert_alpha()]
        self.sasuke_frame_storage = [pygame.transform.scale(frame, (75, 55)) for frame in self.sasuke_normal]
        self.sasuke_attack_frame_storage = [pygame.transform.scale(frame, (75, 55)) for frame in self.sasuke_attack]

        self.kakashi_normal = [pygame.image.load('Plant vs Stick/Picture/kakashi/kakashi_run_1.png').convert_alpha(),
                               pygame.image.load('Plant vs Stick/Picture/kakashi/kakashi_run_2.png').convert_alpha(),
                               pygame.image.load('Plant vs Stick/Picture/kakashi/kakashi_run_3.png').convert_alpha()]
        self.kakashi_attack = [pygame.image.load('Plant vs Stick/Picture/kakashi/kakashi_attack_1.png').convert_alpha(),
                               pygame.image.load('Plant vs Stick/Picture/kakashi/kakashi_attack_2.png').convert_alpha()]
        self.kakashi_frame_storage = [pygame.transform.scale(frame, (110, 85)) for frame in self.kakashi_normal]
        self.kakashi_attack_frame_storage = [pygame.transform.scale(frame, (110, 85)) for frame in self.kakashi_attack]

    def event_handling(self):
        def clicked_troop(gold_cost, diamond_cost, button_name, frame_storage, attack_frame_storage, health, attack_damage, speed,
                          troop_width, troop_height, troop_name):
            mouse_pos = pygame.mouse.get_pos()  # Check if the left mouse button was clicked and handle accordingly

            if button_name.is_clicked(mouse_pos):
                if len(self.troop_on_court) <= 20:
                    if self.num_gold >= gold_cost and self.num_diamond >= diamond_cost:
                        self.num_gold -= gold_cost
                        self.num_diamond -= diamond_cost
                        new_troop = Troop(frame_storage, attack_frame_storage, health, attack_damage, speed, troop_width, troop_height, troop_name)
                        self.troop_on_court.append(new_troop)
                    else:
                        button_name.insufficient_currency = True
                        # button_name.false_toggle = True
                        button_name.lack_currency(self.screen)
                else:
                    self.max_troop(button_name)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check if left mouse button is pressed
                    clicked_troop(100, 200, self.warrior_button, self.warrior_frame_storage, self.warrior_attack_frame_storage, 100,
                                  1, 1, 75, 100, 'Warrior')
                    clicked_troop(300, 200, self.archer_button, self.archer_frame_storage, self.archer_attack_frame_storage, 200, 2,
                                  1, 200, 100, 'Archer')
                    clicked_troop(500, 500, self.wizard_button, self.wizard_frame_storage, self.wizard_attack_frame_storage, 250, 2,
                                  2, 200, 100, 'Wizard')
                    clicked_troop(700, 200, self.sparta_button, self.sparta_frame_storage, self.sparta_attack_frame_storage, 300, 3,
                                  2, 75, 100, 'Sparta')
                    clicked_troop(700, 200, self.giant_button, self.giant_frame_storage, self.giant_attack_frame_storage, 350, 4, 1,
                                  30, 200, 'Giant')

            if event.type == self.ninja_timer:
                if len(self.enemy_on_court) <= 20:
                    new_ninja = None
                    ninja_chosen = choice(self.ninja_choice)
                    if ninja_chosen == "naruto":
                        new_ninja = Ninja(ninja_chosen, self.naruto_frame_storage, self.naruto_attack_frame_storage, 100, 1, 2,
                                        self.background_image.get_width())
                    elif ninja_chosen == "sasuke":
                        new_ninja = Ninja(ninja_chosen, self.sasuke_frame_storage, self.sasuke_attack_frame_storage, 50, 1, 3,
                                        self.background_image.get_width())
                    elif ninja_chosen == "kakashi":
                        new_ninja = Ninja(ninja_chosen, self.kakashi_frame_storage, self.kakashi_attack_frame_storage, 75, 2, 2,
                                        self.background_image.get_width())
                    self.enemy_on_court.append(new_ninja)
                else:
                    print('wont be more than 20')

            if self.chosen_spell is None and event.type == pygame.MOUSEBUTTONDOWN:
                if self.healing_spell_rect.collidepoint(event.pos):
                    self.chosen_spell = 'healing'
                elif self.rage_spell_rect.collidepoint(event.pos):
                    self.chosen_spell = 'rage'
                elif self.freeze_spell_rect.collidepoint(event.pos):
                    self.chosen_spell = 'freeze'

            if self.chosen_spell is not None and event.type == pygame.MOUSEMOTION:
                # card follow the mouse poss
                if self.chosen_spell == 'healing':
                    self.healing_spell_rect.move_ip(event.rel)
                elif self.chosen_spell == 'rage':
                    self.rage_spell_rect.move_ip(event.rel)
                elif self.chosen_spell == 'freeze':
                    self.freeze_spell_rect.move_ip(event.rel)

            if event.type == pygame.MOUSEBUTTONUP and self.chosen_spell is not None:
                # can add check condition can release spell or not
                if self.chosen_spell == 'healing':
                    # for troop in self.troop_on_court:
                    #     troop.health_increase()
                    if not self.healing_spell_rect.center == self.healing_initial_position:
                        self.healing_spell_rect.center = self.healing_initial_position  # Snap back to initial position
                if self.chosen_spell == 'rage':
                    # for troop in self.troop_on_court:
                    #     troop.speed_increase()
                    if not self.rage_spell_rect.center == self.rage_initial_position:
                        self.rage_spell_rect.center = self.rage_initial_position  # Snap back to initial position
                if self.chosen_spell == 'freeze':
                    # for ninja in self.enemy_on_court:
                    #     ninja.ninja_speed_decrease()
                    if not self.freeze_spell_rect.center == self.freeze_initial_position:
                        self.freeze_spell_rect.center = self.freeze_initial_position  # Snap back to initial position
                self.chosen_spell = None

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

        for troop in self.troop_on_court:
            if self.check_collision(troop, self.right_rect_castle):
                get_damage = troop.attack_damage
                self.health_bar_enemy.update_health(get_damage)  # Update castle health
                troop.attack()

        for ninja in self.enemy_on_court:
            if self.ninja_collision(ninja, self.left_rect_castle):
                get_the_damage = ninja.attack
                self.health_bar_user.update_health(get_the_damage)  # Update castle health
                ninja.ninja_attack()

        for ninja in self.enemy_on_court:
            for troop in self.troop_on_court:
                if self.both_collide(troop, ninja):
                    troop.attack()   
                    troop.take_damage(ninja.attack)  
                    if troop.health <= 0:
                        self.troop_on_court.remove(troop)
                if self.both_collide(troop, ninja):
                    ninja.ninja_attack()
                    ninja.ninja_take_damage(troop.attack_damage)
                    if ninja.ninja_health <= 0:
                        self.enemy_on_court.remove(ninja)

    def max_troop(self, button_name):
        if button_name == self.warrior_button:
            button_name.insufficient_currency = True
            button_name.lack_currency(self.screen)
        elif button_name == self.archer_button:
            button_name.insufficient_currency = True
            button_name.lack_currency(self.screen)
        elif button_name == self.wizard_button:
            button_name.insufficient_currency = True
            button_name.lack_currency(self.screen)
        elif button_name == self.sparta_button:
            button_name.insufficient_currency = True
            button_name.lack_currency(self.screen)
        elif button_name == self.giant_button:
            button_name.insufficient_currency = True
            button_name.lack_currency(self.screen)

    @staticmethod
    def check_collision(troop, rect):
        troop_rect = pygame.Rect(troop.coordinate_x, 0, troop.troop_width, troop.troop_height)  # for right castle
        return troop_rect.colliderect(rect)
    
    @staticmethod
    def both_collide(troop, ninja):
        troop_rect = pygame.Rect(troop.coordinate_x, 0, troop.troop_width, troop.troop_height)
        ninja_rect = pygame.Rect(ninja.ninja_coordinate_x, 0, 75, 100)                            # for attack each other
        return troop_rect.colliderect(ninja_rect)

    @staticmethod
    def ninja_collision(ninja, rect):
        ninja_rect = pygame.Rect(ninja.ninja_coordinate_x, 0, 75, 100)   # for left castle
        return ninja_rect.colliderect(rect)

    def check_game_over(self):
        if self.health_bar_user.current_health <= 0:
            self.game_over = True
            self.winner = "Enemy"
        elif self.health_bar_enemy.current_health <= 0:
            self.game_over = True
            self.winner = "User"

    def game_start(self):
        # Clear screen
        self.screen.fill((255, 255, 255))

        # Draw rectangles on both sides of the scrolling background
        left_rect_castle = pygame.Rect(self.bg_x, 90, 170, 390)
        right_rect_castle = pygame.Rect(self.bg_x + self.background_image.get_width() - 170, 90, 170, 390)
        pygame.draw.rect(self.screen, (0, 255, 0), left_rect_castle)
        pygame.draw.rect(self.screen, (255, 0, 0), right_rect_castle)

        # background
        self.screen.blit(self.background_image, (self.bg_x, 0))

        self.health_bar_user.draw(self.screen)
        self.health_bar_enemy.draw(self.screen)

        # box for spell
        self.screen.blit(self.box_surf, self.box_rect)
        self.screen.blit(self.healing_spell_surf, self.healing_spell_rect)
        self.screen.blit(self.freeze_spell_surf, self.freeze_spell_rect)
        self.screen.blit(self.rage_spell_surf, self.rage_spell_rect)

        # gold icon
        self.screen.blit(self.pic_gold_surf, self.pic_gold_rect)
        self.num_gold_surf = self.num_gold_font.render(str(self.num_gold), True, 'Black')
        self.screen.blit(self.num_gold_surf, self.num_gold_rect)

        # diamond icon
        self.screen.blit(self.pic_diamond_surf, self.pic_diamond_rect)
        self.num_diamond_surf = self.num_diamond_font.render(str(self.num_diamond), True, 'Black')
        self.screen.blit(self.num_diamond_surf, self.num_diamond_rect)

        # button draw
        self.warrior_button.draw(self.screen)
        self.archer_button.draw(self.screen)
        self.wizard_button.draw(self.screen)
        self.sparta_button.draw(self.screen)
        self.giant_button.draw(self.screen)

        self.check_game_over()
        if self.game_over:
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 68)
            if self.winner == "User":
                text = font.render("You've won!", True, (255, 255, 255))
            else:
                text = font.render("You've lost!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(500, 300))
            self.screen.blit(text, text_rect)
            return  # End the game

        for troop in self.troop_on_court:
            troop.spawn_troop(self.screen, self.bg_x)
            troop.update()

        for enemy in self.enemy_on_court:
            enemy.spawn_ninja(self.screen, self.bg_x)
            enemy.update_ninja()

    def run(self):
        while True:
            self.game_start()
            self.event_handling()

            pygame.display.update()  # Update the display
            self.clock.tick(60)  # Limit frame rate to 60 FPS

if __name__ == "__main__":
    Game().run()
