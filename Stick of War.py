# coding : utf-8

import pygame
from sys import exit

pygame.init()

class TroopButton:
    def __init__(self, image,image_dim, size, position, name, cooldown_time = 3000):
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
    def __init__(self, frame_storage):
        self.coordinate_x = 0
        self.animation_index = 0
        self.frame_storage = frame_storage
        self.image = self.frame_storage[self.animation_index]
        

    def spawn_troop(self, screen, bg_x):
        self.rect = self.image.get_rect(bottomright=(self.coordinate_x + bg_x, 500))
        screen.blit(self.image, self.rect)

    def update(self):
        self.coordinate_x += 2
        self.animation_index += 0.2
        if self.animation_index >= len(self.frame_storage):
            self.animation_index = 0
        self.image = self.frame_storage[int(self.animation_index)]


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

        self.set_up()

    def set_up(self):
        # Scrolling Background
        self.background_image = pygame.image.load('War of stick/Picture/utlis/map.jpg')

        # spell equipment
        self.box = pygame.image.load('War of stick/Picture/utlis/box.png')
        self.box_surf = pygame.transform.scale(self.box, (600, 80))
        self.box_rect = self.box_surf.get_rect(center=(300,550))

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
        self.warrior_all_image = [
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 1.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 2.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 3.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 4.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman sword/stickman sword run/stickman sword run 5.png').convert_alpha()]
        self.warrior_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.warrior_all_image]

        self.warrior_button_image = pygame.image.load('War of stick/Picture/button/sword_button.png')
        self.wizard_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/wizard_dim.png')
        self.warrior_button = TroopButton(self.warrior_button_image, self.wizard_button_dim_image, (100, 100), (100, 70), '10\n20')

        # Troop Two
        self.archer_all_image = [pygame.image.load('War of stick/Picture/stickman archer/stickman archer 1.png').convert_alpha(),
                                 pygame.image.load('War of stick/Picture/stickman archer/stickman archer 2.png').convert_alpha()]
        self.archer_frame_storage = [pygame.transform.scale(frame, (75, 100)) for frame in self.archer_all_image]

        self.archer_button_image = pygame.image.load('War of stick/Picture/button/archer_button.png')
        self.wizard_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/wizard_dim.png')
        self.archer_button = TroopButton(self.archer_button_image, self.wizard_button_dim_image, (100, 100), (200, 70), '30\n20')

        # Troop Three
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

        self.wizard_button_image = pygame.image.load('War of stick/Picture/button/wizard_button.png')
        self.wizard_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/wizard_dim.png')
        self.wizard_button = TroopButton(self.wizard_button_image,self.wizard_button_dim_image, (100, 100), (300, 70), '50\n50')


        # Troop Four
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

        self.sparta_button_image = pygame.image.load('War of stick/Picture/button/sparta_button.png')
        self.wizard_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/wizard_dim.png')
        self.sparta_button = TroopButton(self.sparta_button_image, self.wizard_button_dim_image, (100, 100), (400, 70), '70\n20')

        # Troop Five
        self.giant_all_image = [
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 1.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 2.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 3.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 4.png').convert_alpha(),
            pygame.image.load('War of stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 5.png').convert_alpha()]
        self.giant_frame_storage = [pygame.transform.scale(frame, (150, 200)) for frame in self.giant_all_image]
        self.giant_button_image = pygame.image.load('War of stick/Picture/button/giant_button.png').convert_alpha()
        self.wizard_button_dim_image = pygame.image.load('War of stick/Picture/button_dim/wizard_dim.png')
        self.giant_button = TroopButton(self.giant_button_image, self.wizard_button_dim_image, (100, 100), (500, 70), '70\n20')

    def event_handling(self):
        def clicked_troop(gold_cost, diamond_cost, button_name, frame_storage):
            mouse_pos = pygame.mouse.get_pos()  # Check if the left mouse button was clicked and handle accordingly

            if button_name.is_clicked(mouse_pos):
                if self.num_gold >= gold_cost and self.num_diamond >= diamond_cost:
                    self.num_gold -= gold_cost
                    self.num_diamond -= diamond_cost
                    new_troop = Troop(frame_storage)
                    self.troop_on_court.append(new_troop)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check if left mouse button is pressed
                    clicked_troop(10, 20, self.warrior_button, self.warrior_frame_storage)
                    clicked_troop(30, 20, self.archer_button, self.archer_frame_storage)
                    clicked_troop(50, 50, self.wizard_button, self.wizard_frame_storage)
                    clicked_troop(70, 20, self.sparta_button, self.sparta_frame_storage)
                    clicked_troop(70, 20, self.giant_button, self.giant_frame_storage)

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
        self.screen.blit(self.box_surf, self.box_rect)

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