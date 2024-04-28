# coding : utf-8
import pygame
from sys import exit

pygame.init()

class TroopButton:
    def __init__(self, image, image_dim, size, position, name, cooldown_time):
        self.size = size
        self.position = position
        self.image = image
        self.image_dim = image_dim
        self.image = pygame.transform.scale(self.image, self.size)
        self.image_dim = pygame.transform.scale(self.image_dim, self.size)
        self.name = name
        self.cooldown_time = cooldown_time
        self.rect = self.image.get_rect(center=self.position)
        self.clicked = False
        self.coordinate_x = 0
        self.last_clicked_time = 0
        self.remaining_cooldown = 0

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
        if self.clicked:
            # Display cooldown time if the button is on cooldown
            current_time = pygame.time.get_ticks()
            self.remaining_cooldown = max(0, self.cooldown_time - (current_time - self.last_clicked_time)) // 1000
            cooldown_font = pygame.font.Font(None, 70)
            cooldown_text = cooldown_font.render(f"{self.remaining_cooldown}", True, (255, 255, 255))
            cooldown_text_rect = cooldown_text.get_rect(center=(self.position[0], self.position[1]))
            screen.blit(self.image_dim, self.rect)
            screen.blit(cooldown_text, cooldown_text_rect)

        if self.remaining_cooldown == 0:
            screen.blit(self.image, self.rect)
            self.clicked = False
        self.render_name(screen)

    def is_clicked(self, mouse_pos):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_clicked_time >= self.cooldown_time:
            if self.rect.collidepoint(mouse_pos):
                self.clicked = True
                self.last_clicked_time = current_time
                return True
        return False

class Troop:
    def __init__(self,frame_storage, attack_frame_storage, health, damage, speed):
        self.coordinate_x = 0
        self.animation_index = 0
        self.frame_storage = frame_storage
        self.image = self.frame_storage[self.animation_index]
        self.attacking = False  
        self.attack_frame_index = 0  
        self.attack_frame_storage = attack_frame_storage
        self.image = self.attack_frame_storage[self.attack_frame_index]
        self.health = health
        self.damage = damage
        self.speed = speed

    def spawn_troop(self, screen, bg_x):
        self.rect = self.image.get_rect(bottomright=(self.coordinate_x + bg_x, 500))
        screen.blit(self.image, self.rect)
        # communication between the Troop instance and the Game instance
        self.communication = self

    def update(self):
        self.coordinate_x += 2
        self.animation_index += 0.2
        if self.animation_index >= len(self.frame_storage):
            self.animation_index = 0

    def attack(self):
        self.attacking = True
        if self.attacking:
            self.coordinate_x -= 2
            self.attack_frame_index += 0.1
            if self.attack_frame_index >= len(self.attack_frame_storage):
                self.attack_frame_index = 0
                self.attacking = False
            self.image = self.attack_frame_storage[int(self.attack_frame_index)]

    def take_damage(self, damage):
        self.health -= damage
        if self.health == 0:
            if self in self.communication.troop_on_court:
                self.communication.troop_on_court.remove(self)

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
        self.gold_interval = 100
        self.diamond_interval = 100
        self.troop_on_court = []
        self.bullet_on_court = []
        self.max_health_user = 10000
        self.max_health_enemy = 10000
        self.current_health_user = self.max_health_user
        self.current_health_enemy = self.max_health_enemy
        self.health_bar_width = 200
        self.health_bar_height = 20
        self.health_bar_user_border_pos = (620, 530)
        self.health_bar_enemy_border_pos = (620, 560)
        self.health_bar_user_pos = (620, 530)
        self.health_bar_enemy_pos = (620, 560)
        self.game_over = False
        self.winner = None
        self.set_up()

    def set_up(self):
        # Scrolling Background
        self.background_image = pygame.image.load('War of stick/Picture/utlis/map.jpg')
        self.left_rect_castle = pygame.Rect(self.bg_x, 90, 170, 390)
        self.right_rect_castle = pygame.Rect(self.bg_x + self.background_image.get_width() - 100, 90, 170, 390) # distance between troop and castle during time

        # spell equipment
        self.box = pygame.image.load('War of stick/Picture/utlis/box.png')
        self.box_surf = pygame.transform.scale(self.box, (600, 80))
        self.box_rect = self.box_surf.get_rect(center=(300, 550))

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
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 1.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 2.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 3.png').convert_alpha()]
        self.warrior_attack_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.warrior_attack_image]

        self.warrior_button_image = pygame.image.load('War of stick/Picture/button/sword_button.png')
        self.warrior_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/sword_dim.png')
        self.warrior_button = TroopButton(self.warrior_button_image, self.warrior_button_dim_image, (100, 100), (100, 70), '100\n200', 3000)

        # Troop Two
        # Archer walk
        self.archer_all_image = [pygame.image.load('War of stick/Picture/stickman archer/stickman archer 1.png').convert_alpha(),
                                pygame.image.load('War of stick/Picture/stickman archer/stickman archer 2.png').convert_alpha()]
        self.archer_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.archer_all_image]

        # archer attack
        self.archer_attack_image = [
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 1.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 2.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword attack/stickman sword attack 3.png').convert_alpha()]
        self.archer_attack_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.archer_attack_image]

        self.archer_button_image = pygame.image.load('War of stick/Picture/button/archer_button.png')
        self.archer_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/archer_dim.png')
        self.archer_button = TroopButton(self.archer_button_image, self.archer_button_dim_image, (100, 100), (200, 70), '300\n200', 3000)

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
        self.wizard_button = TroopButton(self.wizard_button_image, self.wizard_button_dim_image, (100, 100), (300, 70), '500\n500', 3000)
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
        self.sparta_button = TroopButton(self.sparta_button_image, self.sparta_button_dim_image, (100, 100), (400, 70), '700\n200', 3000)

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
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant attack/stickman Giant attack 1.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant attack/stickman Giant attack 2.png').convert_alpha()]
        self.giant_attack_frame_storage = [pygame.transform.scale(frame, (150, 200)) for frame in self.giant_attack_image]

        self.giant_button_image = pygame.image.load('War of stick/Picture/button/giant_button.png').convert_alpha()
        self.giant_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/giant_dim.png')
        self.giant_button = TroopButton(self.giant_button_image, self.giant_button_dim_image, (100, 100), (500, 70), '700\n200', 3000)

    def event_handling(self):
        def clicked_troop(gold_cost, diamond_cost, button_name, frame_storage, attack_frame_storage, health, damage, speed):
            mouse_pos = pygame.mouse.get_pos()  # Check if the left mouse button was clicked and handle accordingly

            if button_name.is_clicked(mouse_pos):
                if self.num_gold >= gold_cost and self.num_diamond >= diamond_cost:
                    self.num_gold -= gold_cost
                    self.num_diamond -= diamond_cost
                    new_troop = Troop(frame_storage, attack_frame_storage, health, damage, speed)
                    self.troop_on_court.append(new_troop)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check if left mouse button is pressed
                    clicked_troop(100, 200, self.warrior_button,self.warrior_frame_storage, self.warrior_attack_frame_storage, 100, 20, 1)
                    clicked_troop(300, 200, self.archer_button,self.archer_frame_storage, self.archer_attack_frame_storage, 100, 20, 1)
                    clicked_troop(500, 500, self.wizard_button,self.wizard_frame_storage, self.wizard_attack_frame_storage, 100, 20, 1)
                    clicked_troop(700, 200, self.sparta_button,self.sparta_frame_storage, self.sparta_attack_frame_storage, 100, 20, 1)
                    clicked_troop(700, 200, self.giant_button,self.giant_frame_storage, self.giant_attack_frame_storage, 100, 20, 1)

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

        # Check collision with right castle rectangle and trigger attack
        for troop in self.troop_on_court:
            if self.check_collision(troop, self.right_rect_castle): 
                damage = troop.damage
                self.update_health("enemy", damage)  # Update castle health
                troop.attack()                

    def check_collision(self, troop, rect):
        # collision detection method
        troop_rect = pygame.Rect(troop.coordinate_x, 0, troop.image.get_width(), troop.image.get_height())
        return troop_rect.colliderect(rect)
    
    def draw_health_bar(self):
        # # Draw health bars
        # pygame.draw.rect(self.screen, (0, 255, 0), (self.health_bar_user_pos[0], self.health_bar_user_pos[1], self.current_health_user / self.max_health_user * self.health_bar_width, self.health_bar_height))
        # pygame.draw.rect(self.screen, (255, 0, 0), (self.health_bar_enemy_pos[0] + (1 - self.current_health_enemy / self.max_health_enemy) * self.health_bar_width, self.health_bar_enemy_pos[1], self.current_health_enemy / self.max_health_enemy * self.health_bar_width, self.health_bar_height))
        # or this not sure which one okay in the future, dont delete, later code finish i will test both
        # Draw health bars for the user's castle (left)
        user_health_width = self.current_health_user / self.max_health_user * self.health_bar_width
        user_health_x = self.health_bar_user_pos[0]
        pygame.draw.rect(self.screen, (0, 255, 0), (user_health_x, self.health_bar_user_pos[1], user_health_width, self.health_bar_height))

        # Draw health bars for the enemy's castle (right)
        enemy_health_width = self.current_health_enemy / self.max_health_enemy * self.health_bar_width
        enemy_health_x = self.health_bar_enemy_pos[0] + (1 - self.current_health_enemy / self.max_health_enemy) * self.health_bar_width
        pygame.draw.rect(self.screen, (255, 0, 0), (enemy_health_x, self.health_bar_enemy_pos[1], enemy_health_width, self.health_bar_height))

    def update_health(self, side, damage):
        if side == "user":
            self.current_health_user -= damage
        elif side == "enemy":
            self.current_health_enemy -= damage

        # Ensure health doesn't go below 0
        self.current_health_user = max(0, self.current_health_user)
        self.current_health_enemy = max(0, self.current_health_enemy)

    def check_game_over(self):
        if self.current_health_user <= 0:
            self.game_over = True
            self.winner = "Enemy"
        elif self.current_health_enemy <= 0:
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

        # Draw border for health bars
        health_bar_border_user = pygame.Rect(self.health_bar_user_pos[0] - 2, self.health_bar_user_pos[1] - 2, self.health_bar_width + 4, self.health_bar_height + 4)
        health_bar_border_enemy = pygame.Rect(self.health_bar_enemy_pos[0] - 2, self.health_bar_enemy_pos[1] - 2, self.health_bar_width + 4, self.health_bar_height + 4)
        pygame.draw.rect(self.screen, (0, 0, 0), health_bar_border_user, 2)  # Border for left health bar
        pygame.draw.rect(self.screen, (0, 0, 0), health_bar_border_enemy, 2)  # Border for right health bar
        self.draw_health_bar()

        # box for spell
        self.screen.blit(self.box_surf, self.box_rect)

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
            text_rect = text.get_rect(center=(500,300))
            self.screen.blit(text, text_rect)
            return  # End the game

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