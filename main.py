import asyncio
import pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption('Stick_Defend')  # title name
pygame.display.set_mode((1000, 600))
from sys import exit
import time
import ast
from random import randint, choice


class Data:
    def __init__(self):
        self.all_user = []
        self.fetch_data()
        self.login_method = None
        self.username = "Guest"
        self.password = "888888"
        self.stage_level = 4
        self.money = 6000
        # troop : [have or not, level, equipped or not, health, attack damage, speed, upgrades_price]
        # health = (current health * 1.1)//1
        # attack = (current attack* 1.1)
        # upgrades_price = (current price * 1.1)//1
        self.troop_storage = {
            "warrior": [True, 1, True, 1000, 10000, 15, 200],
            "archer": [True, 1, True, 200, 10, 1.1, 150],
            "wizard": [False, 1, False, 250, 10, 0.8, 200],
            "sparta": [False, 1, False, 300, 2.5, 1, 350],
            "giant": [False, 1, False, 350, 3.5, 0.6, 500]
        }

        # spell :[have or not, level, equpped or not, functionality, upgrades price]
        # rage = rage + 0.05
        # healing = healing + 100
        # freeze = freeze + 0.05
        self.spell_storage = {
            "rage": [False, 1, False, 0.1, 150],
            "healing": [False, 1, False, 100, 150],
            "freeze": [False, 1, False, 0.1, 150]
        }
        # first upgrades for health, second is formining speed level
        # middle two coloum 1000 stand for health and 10 stand for mining speed
        # and the last two coloum first stand for the health upgrades price, second stand for mining speed upgrades price
        self.castle_storage = {
            "default_castle": [True, 1, 1, 1000, 1, 150, 150]  # two upgrades
        }

        self.warrior_gold = 200
        self.warrior_diamond = 0
        self.archer_gold = 300
        self.archer_diamond = 200
        self.wizard_gold = 300
        self.wizard_diamond = 500
        self.sparta_gold = 500
        self.sparta_diamond = 350
        self.giant_gold = 1000
        self.giant_diamond = 500

        self.lvl_choose = 100

        self.no_star = pygame.image.load('War of stick/Picture/utils/no_star.png')
        self.no_star_surf = pygame.transform.scale(self.no_star, (90, 40))
        self.star_one_surf = self.no_star_surf
        self.star_two_surf = self.no_star_surf
        self.star_three_surf = self.no_star_surf
        self.star_four_surf = self.no_star_surf
        self.star_five_surf = self.no_star_surf
        self.star_six_surf = self.no_star_surf
        self.star_seven_surf = self.no_star_surf
        self.star_eight_surf = self.no_star_surf
        self.star_nine_surf = self.no_star_surf
        self.star_ten_surf = self.no_star_surf

    # sign in and take the info of the data
    def sign_in(self, username, password):
        for user in self.all_user:
            if user["username"] == username and user["password"] == password:
                self.username = user["username"]
                self.password = user["password"]
                self.stage_level = user["stage_level"]
                self.money = user["money"]
                self.troop_storage = user["troop_storage"]
                self.spell_storage = user["spell_storage"]
                self.castle_storage = user["castle_storage"]
                self.login_method = "sign_in"
                return True
        else:
            return False

    # sign up a new account with default info
    def sign_up(self, username, password):
        data = {'username': username,
                'password': password,
                'stage_level': 1,
                'money': 0,
                'troop_storage': {
                    "warrior": [True, 1, True, 100, 1.5, 1, 200],
                    "archer": [True, 1, True, 200, 10, 1.1, 150],
                    "wizard": [False, 1, False, 250, 10, 0.8, 200],
                    "sparta": [False, 1, False, 300, 2.5, 1, 350],
                    "giant": [False, 1, False, 350, 3.5, 0.6, 500]
                },
                'spell_storage': {
                    "rage": [False, 1, False, 0.1, 150],
                    "healing": [False, 1, False, 100, 150],
                    "freeze": [False, 1, False, 0.1, 150]
                },
                'castle_storage': {
                    "default_castle": [True, 1, 1, 1000, 1, 150, 150]  # two upgrades
                }}
        self.all_user.append(data)

    # read current user data
    def read_data(self):
        all_data = {
            "username": self.username,
            "password": self.password,
            "stage_level": self.stage_level,  # can be list if you want else just integer
            "money": self.money,  # money that the user has
            "troop_storage": self.troop_storage,
            "spell_storage": self.spell_storage,
            "castle_storage": self.castle_storage,
        }
        return all_data

    def print_all_user(self):
        for user in self.all_user:
            print(f"username: {user['username']}")
            print(f"password: {user['password']}")
            print(f"stage_level: {user['stage_level']}")
            print(f"money: {user['money']}")
            print("troop_storage:")
            for troop, details in user["troop_storage"].items():
                print(f"  {troop}: {details}")
            print("spell_storage:")
            for spell, details in user["spell_storage"].items():
                print(f"  {spell}: {details}")
            print("castle_storage:")
            for castle, details in user["castle_storage"].items():
                print(f"  {castle}: {details}")
            print("\n")

    # update user latest info to self.all_user (after update you can push_data)
    def update_user(self):
        all_data = self.read_data()
        for i, user in enumerate(self.all_user):
            if user["username"] == self.username:
                self.all_user[i] = all_data
                break

    # fetch every user from database
    def fetch_data(self):
        with open('database.txt', mode='rt', encoding='utf-8') as f:
            for line in f:
                user_data = ast.literal_eval(line.strip())
                self.all_user.append(user_data)

    def push_data(self):
        with open('database.txt', mode='w', encoding='utf-8') as f:
            for user in self.all_user:
                f.write(f"{user}\n")


database = Data()

class LoadingBar:
    def __init__(self, x, y, height, width, colour, border_colour, border_width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour
        self.border_colour = border_colour
        self.border_width = border_width
        self.progress = 0  # the first progress variable is to calculate how much should it be filled in
        # if remove that the loading bar won't work

    def draw_bar(self, screen):
        pygame.draw.rect(screen, self.border_colour, (
            self.x - self.border_width, self.y - self.border_width, self.width + 2 * self.border_width,
            self.height + 2 * self.border_width))
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width * self.progress, self.height))


class GameHome:
    def __init__(self):
        # pygame.init()
        # pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Home Page')
        self.loading_bar = LoadingBar(400, 500, 30, 200, (255, 255, 224), (0, 0, 0), 2)  # Fixed width initialization
        self.progress = 0  # this one is if I put 0.2 it will start the loading bar from 0.2

        self.image = pygame.image.load(
            "War of stick/Picture/utils/background_photo.jpg")  # Replace "home_image.jpg" with your image path
        self.image = pygame.transform.scale(self.image, (1000, 600))
        self.image_rect = self.image.get_rect(center=(1000 // 2, 600 // 2))

        self.wood_plank_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.wood_plank_surface = pygame.transform.scale(self.wood_plank_surface, (200, 60))
        self.pokemon_vs_naruto_rect = None
        self.stick_of_war_rect = None

        self.text_box_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.text_box_surface = pygame.transform.scale(self.text_box_surface, (400, 60))

        self.loading = True
        self.finish_loading = False

        self.font = pygame.font.Font(None, 35)
        self.choose_game_to_play = False
        self.choosing_login_method = False
        self.signing_in = False
        self.signing_up = False
        self.login_as_guest = False

        self.retry = False
        self.no_account_found = False
        self.signup_time = None
        self.signin_time = None
        self.retry_time = None
        self.acc_found_time = None
        self.go_pokemon_py = False
        self.go_level_py = False

        # sign up
        self.user_text_box_rectangle = self.text_box_surface.get_rect(center=(500, 250))
        self.ask_username = self.font.render('Create your username', True, (255, 255, 255))
        self.ask_username_rect = self.ask_username.get_rect(center=(500, 200))

        self.pass_text_box_rectangle = self.text_box_surface.get_rect(center=(500, 350))
        self.ask_password = self.font.render("Create your password", True, (255, 255, 255))
        self.ask_password_rect = self.ask_password.get_rect(center=(500, 300))

        self.enter_rectangle = self.wood_plank_surface.get_rect(center=(500, 450))
        self.enter_text = self.font.render("Enter", True, (255, 255, 255))
        self.enter_text_rect = self.enter_text.get_rect(center=self.enter_rectangle.center)

        self.back_rectangle = self.wood_plank_surface.get_rect(center=(100, 100))
        self.back_text = self.font.render("Back", True, (255, 255, 255))
        self.back_text_rect = self.back_text.get_rect(center=self.back_rectangle.center)

        self.sign_up_username = ""
        self.sign_up_password = ""
        self.signup_done = False
        self.key_user = False
        self.key_pass = False

        # sign in
        self.sign_in_user_text_box_rectangle = self.text_box_surface.get_rect(center=(500, 250))
        self.sign_in_ask_username = self.font.render('Type your username', True, (255, 255, 255))
        self.sign_in_ask_username_rect = self.sign_in_ask_username.get_rect(center=(500, 200))

        self.sign_in_pass_text_box_rectangle = self.text_box_surface.get_rect(center=(500, 350))
        self.sign_in_ask_password = self.font.render("Type your password", True, (255, 255, 255))
        self.sign_in_ask_password_rect = self.sign_in_ask_password.get_rect(center=(500, 300))

        self.sign_in_login_rectangle = self.wood_plank_surface.get_rect(center=(500, 450))
        self.sign_in_login_text = self.font.render("Login", True, (255, 255, 255))
        self.sign_in_login_text_rect = self.sign_in_login_text.get_rect(center=self.sign_in_login_rectangle.center)

        self.sign_in_back_rectangle = self.wood_plank_surface.get_rect(center=(100, 100))
        self.sign_in_back_text = self.font.render("Back", True, (255, 255, 255))
        self.sign_in_back_text_rect = self.sign_in_back_text.get_rect(center=self.sign_in_back_rectangle.center)

        self.sign_in_username = ""
        self.sign_in_password = ""
        self.sign_in_key_user = False
        self.sign_in_key_pass = False

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.update_user()
                database.push_data()
                pygame.quit()
                exit()
            elif self.choose_game_to_play and event.type == pygame.MOUSEBUTTONDOWN:
                if self.stick_of_war_rect.collidepoint(pygame.mouse.get_pos()):
                    self.choose_game_to_play = False
                    self.home_music.stop()
                    self.go_level_py = True
                elif self.pokemon_vs_naruto_rect.collidepoint(pygame.mouse.get_pos()):
                    self.choose_game_to_play = False
                    self.home_music.stop()
                    self.go_pokemon_py = True
                elif self.back_rectangle.collidepoint(pygame.mouse.get_pos()):
                    self.choosing_login_method = True
                    self.choose_game_to_play = False
                    database.login_method = None
            elif self.choosing_login_method and event.type == pygame.MOUSEBUTTONDOWN:
                if not self.signing_up and not self.login_as_guest and self.sign_in_rect.collidepoint(pygame.mouse.get_pos()):
                    self.signing_in = True
                    self.choosing_login_method = False
                elif not self.signing_in and not self.login_as_guest and self.sign_up_rect.collidepoint(pygame.mouse.get_pos()):
                    self.signing_up = True
                    self.choosing_login_method = False
                elif not self.signing_in and not self.signing_up and self.login_as_guest_rect.collidepoint(pygame.mouse.get_pos()):
                    self.login_as_guest = True
                    self.choosing_login_method = False

            if self.signing_up:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.user_text_box_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.key_user = True
                        self.key_pass = False
                    elif self.pass_text_box_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.key_user = False
                        self.key_pass = True
                    elif self.back_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.key_user = False
                        self.key_pass = False
                        self.signing_up = False
                        self.choosing_login_method = True
                        self.sign_up_username = ""
                        self.sign_up_password = ""
                    elif self.enter_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.key_user = False
                        self.key_pass = False
                        if self.sign_up_username != "" and self.sign_up_password != "":
                            database.sign_up(self.sign_up_username, self.sign_up_password)
                            self.signup_time = time.time()
                            self.signup_done = True
                            self.signing_up = False
                            self.choosing_login_method = True
                            self.sign_up_username = ""
                            self.sign_up_password = ""
                        else:
                            self.sign_up_username = ""
                            self.sign_up_password = ""
                            self.retry = True
                            self.retry_time = time.time()
                            self.signing_up = True
                            self.choosing_login_method = False

                if event.type == pygame.KEYDOWN:
                    if self.key_user:
                        if event.key == pygame.K_BACKSPACE:
                            self.sign_up_username = self.sign_up_username[:-1]
                        else:
                            self.sign_up_username += event.unicode
                    elif self.key_pass:
                        if event.key == pygame.K_BACKSPACE:
                            self.sign_up_password = self.sign_up_password[:-1]
                        else:
                            self.sign_up_password += event.unicode

            if self.signing_in:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.sign_in_user_text_box_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.sign_in_key_user = True
                        self.sign_in_key_pass = False
                    elif self.sign_in_pass_text_box_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.sign_in_key_user = False
                        self.sign_in_key_pass = True
                    elif self.back_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.sign_in_key_user = False
                        self.sign_in_key_pass = False
                        self.signing_in = False
                        self.choosing_login_method = True
                        self.sign_in_username = ""
                        self.sign_in_password = ""
                    elif self.sign_in_login_rectangle.collidepoint(pygame.mouse.get_pos()):
                        self.sign_in_key_user = False
                        self.sign_in_key_pass = False
                        find_user = database.sign_in(self.sign_in_username, self.sign_in_password)
                        if find_user:
                            self.signing_in = False
                            self.choosing_login_method = False
                            self.sign_in_username = ""
                            self.sign_in_password = ""
                            self.choose_game_to_play = True
                        elif self.sign_in_username == "" or self.sign_in_password == "":
                            self.sign_in_username = ""
                            self.sign_in_password = ""
                            self.retry = True
                            self.retry_time = time.time()
                            self.signing_in = True
                            self.choosing_login_method = False
                        else:
                            self.sign_in_password = ""
                            self.no_account_found = True
                            self.acc_found_time = time.time()
                            self.signing_in = True
                            self.choosing_login_method = False

                if event.type == pygame.KEYDOWN:
                    if self.sign_in_key_user:
                        if event.key == pygame.K_BACKSPACE:
                            self.sign_in_username = self.sign_in_username[:-1]
                        else:
                            self.sign_in_username += event.unicode
                    elif self.sign_in_key_pass:
                        if event.key == pygame.K_BACKSPACE:
                            self.sign_in_password = self.sign_in_password[:-1]
                        else:
                            self.sign_in_password += event.unicode

            elif self.login_as_guest:
                self.choosing_login_method = False
                self.choose_game_to_play = True
                database.login_method = "Guest"
                self.login_as_guest = False

    def game_start_bg(self):
        self.screen.blit(self.image, self.image_rect)

    def update_progress(self):
        # Simulating loading progress

        if self.progress <= 1:
            self.progress += 0.03
            self.finish_loading = False

        else:
            self.progress = 1
            self.loading = False
            self.finish_loading = True
            self.choosing_login_method = True

        self.loading_bar.progress = self.progress
        self.loading_bar.draw_bar(self.screen)

    def draw_button_with_text(self, surface, rect, text):
        text_surf = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(surface, rect)
        self.screen.blit(text_surf, text_rect)

    def choose_game(self):
        self.draw_button_with_text(self.wood_plank_surface, self.wood_plank_surface.get_rect(center=(350, 430)), 'Bokomon vs Stick')
        self.pokemon_vs_naruto_rect = self.wood_plank_surface.get_rect(center=(350, 430))

        self.draw_button_with_text(self.wood_plank_surface, self.wood_plank_surface.get_rect(center=(650, 430)), 'Stick of War')
        self.stick_of_war_rect = self.wood_plank_surface.get_rect(center=(650, 430))

        # Draw back button
        self.screen.blit(self.wood_plank_surface, self.back_rectangle)
        self.screen.blit(self.back_text, self.back_text_rect)

    def signing_user(self):
        self.draw_button_with_text(self.wood_plank_surface, self.wood_plank_surface.get_rect(center=(350, 430)), 'Sign Up')
        self.sign_up_rect = self.wood_plank_surface.get_rect(center=(350, 430))

        self.draw_button_with_text(self.wood_plank_surface, self.wood_plank_surface.get_rect(center=(650, 430)), 'Sign In')
        self.sign_in_rect = self.wood_plank_surface.get_rect(center=(650, 430))

        self.draw_button_with_text(self.wood_plank_surface, self.wood_plank_surface.get_rect(center=(500, 300)), 'Login as Guest')
        self.login_as_guest_rect = self.wood_plank_surface.get_rect(center=(500, 300))

    def sign_in(self):
        self.screen.blit(self.sign_in_ask_username, self.sign_in_ask_username_rect)
        self.screen.blit(self.text_box_surface, self.sign_in_user_text_box_rectangle)
        username = self.font.render(self.sign_in_username, True, (255, 255, 255))
        username_rect = username.get_rect(center=self.sign_in_user_text_box_rectangle.center)
        self.screen.blit(username, username_rect.move(0, 0))

        # Draw password elements
        self.screen.blit(self.sign_in_ask_password, self.sign_in_ask_password_rect)
        self.screen.blit(self.text_box_surface, self.sign_in_pass_text_box_rectangle)
        password = self.font.render(self.sign_in_password, True, (255, 255, 255))
        password_rect = password.get_rect(center=self.sign_in_pass_text_box_rectangle.center)
        self.screen.blit(password, password_rect.move(0, 0))

        # Draw login button
        self.screen.blit(self.wood_plank_surface, self.sign_in_login_rectangle)
        self.screen.blit(self.sign_in_login_text, self.sign_in_login_text_rect)

        # Draw back button
        self.screen.blit(self.wood_plank_surface, self.sign_in_back_rectangle)
        self.screen.blit(self.sign_in_back_text, self.sign_in_back_text_rect)

    def sign_up(self):
        # Draw username elements
        self.screen.blit(self.ask_username, self.ask_username_rect)
        self.screen.blit(self.text_box_surface, self.user_text_box_rectangle)
        username = self.font.render(self.sign_up_username, True, (255, 255, 255))
        username_rect = username.get_rect(center=self.user_text_box_rectangle.center)
        self.screen.blit(username, username_rect.move(0, 0))

        # Draw password elements
        self.screen.blit(self.ask_password, self.ask_password_rect)
        self.screen.blit(self.text_box_surface, self.pass_text_box_rectangle)
        password = self.font.render(self.sign_up_password, True, (255, 255, 255))
        password_rect = password.get_rect(center=self.pass_text_box_rectangle.center)
        self.screen.blit(password, password_rect.move(0, 0))

        # Draw enter button
        self.screen.blit(self.wood_plank_surface, self.enter_rectangle)
        self.screen.blit(self.enter_text, self.enter_text_rect)

        # Draw back button
        self.screen.blit(self.wood_plank_surface, self.back_rectangle)
        self.screen.blit(self.back_text, self.back_text_rect)

    def display_message(self):
        if self.signup_done:
            current_time = time.time()
            if current_time - self.signup_time <= 5:  # Show for 5 seconds
                alpha = max(255 - int((current_time - self.signup_time) * 85), 0)  # Gradually decrease alpha
                success_message = self.font.render("Signup Successful! You can signin now", True, (50, 205, 50))
                success_message.set_alpha(alpha)
                success_message_rect = success_message.get_rect(center=(500, 550))
                self.screen.blit(success_message, success_message_rect)
            else:
                self.signup_done = False
        if self.retry:
            current_retry_time = time.time()
            if current_retry_time - self.retry_time <= 3:  # Show for 3 seconds
                alpha = max(255 - int((current_retry_time - self.retry_time) * 85), 0)  # Gradually decrease alpha
                retry_message = self.font.render("Do not leave the field blank", True, (255, 0, 0))
                retry_message.set_alpha(alpha)
                retry_message_rect = retry_message.get_rect(center=(500, 550))
                self.screen.blit(retry_message, retry_message_rect)
            else:
                self.retry = False
        if self.no_account_found:
            current_no_acc_time = time.time()
            if current_no_acc_time - self.acc_found_time <= 3:  # Show for 3 seconds
                alpha = max(255 - int((current_no_acc_time - self.acc_found_time) * 85), 0)  # Gradually decrease alpha
                no_account_message = self.font.render("No such account found, please try again or signup an account", True,
                                                      (255, 0, 0))
                no_account_message.set_alpha(alpha)
                no_account_message_rect = no_account_message.get_rect(center=(500, 550))
                self.screen.blit(no_account_message, no_account_message_rect)
            else:
                self.retry = False

    def run(self):
        self.home_music = pygame.mixer.Sound('War of stick/Music/home_music.wav')
        self.home_music.set_volume(0.2)
        self.home_music.play(loops=-1)
        while True:
            self.screen.fill((255, 255, 255))

            self.event_handling()
            self.game_start_bg()
            if database.login_method is None:
                if self.loading:
                    self.update_progress()
                elif self.finish_loading:
                    if self.choosing_login_method:
                        self.signing_user()
                    elif self.signing_in:
                        self.sign_in()
                    elif self.signing_up:
                        self.sign_up()
                    elif self.choose_game_to_play:
                        self.choose_game()
            else:
                self.choose_game()
            self.display_message()
            pygame.display.update()
            self.clock.tick(60)



"""
"""
"""
"""
"""
"""

# pygame.init()
# pygame.font.init()


class GameLevel:
    def __init__(self):
        # pygame.init()
        # pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Choose Level')

        self.wood_plank_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.wood_plank_surface = pygame.transform.scale(self.wood_plank_surface, (100, 120))
        self.wood_plank_surface_back_and_store = pygame.transform.scale(self.wood_plank_surface, (90, 50))

        self.lock = pygame.image.load('War of stick/Picture/utils/lock.png')
        self.lock_surf = pygame.transform.scale(self.lock, (100, 100))

        self.one_star = pygame.image.load('War of stick/Picture/utils/one_star.png')
        self.one_star_surf = pygame.transform.scale(self.one_star, (90, 40))

        self.two_star = pygame.image.load('War of stick/Picture/utils/two_star.png')
        self.two_star_surf = pygame.transform.scale(self.two_star, (90, 40))

        self.three_star = pygame.image.load('War of stick/Picture/utils/three_star.png')
        self.three_star_surf = pygame.transform.scale(self.three_star, (90, 40))

        self.level_bg = pygame.image.load('War of stick/Picture/utils/choose level.png')

        self.level_select_music = pygame.mixer.Sound('War of stick/Music/level.mp3')
        self.level_select_music.set_volume(0.2)
        self.level_select_music.play(loops=-1)

        self.go_home_py = False
        self.go_store_py = False
        self.go_stick_of_war = False

        # star rect for all level
        # level one
        self.star_one_rect = self.one_star_surf.get_rect(center=(180, 290))

        # level two
        self.star_two_rect = self.one_star_surf.get_rect(center=(335, 290))

        # level three
        self.star_three_rect = self.one_star_surf.get_rect(center=(495, 290))

        # level four
        self.star_four_rect = self.one_star_surf.get_rect(center=(650, 290))

        # level five
        self.star_five_rect = self.one_star_surf.get_rect(center=(805, 290))

        # level six
        self.star_six_rect = self.one_star_surf.get_rect(center=(180, 470))

        # level seven
        self.star_seven_rect = self.one_star_surf.get_rect(center=(335, 470))

        # level eight
        self.star_eight_rect = self.one_star_surf.get_rect(center=(495, 470))

        # level nine
        self.star_nine_rect = self.one_star_surf.get_rect(center=(650, 470))

        # level ten
        self.star_ten_rect = self.one_star_surf.get_rect(center=(805, 470))

    def choose_level(self, winner, played_time):
        self.wood_plank_rectangle_back = self.wood_plank_surface.get_rect(center=(115, 100))

        self.wood_plank_rectangle_store = self.wood_plank_surface.get_rect(center=(890, 100))

        self.wood_plank_rectangle_one = self.wood_plank_surface.get_rect(center=(180, 230))

        self.wood_plank_rectangle_two = self.wood_plank_surface.get_rect(center=(335, 230))
        self.lock_two_rect = self.lock_surf.get_rect(center=(335, 230))

        self.wood_plank_rectangle_three = self.wood_plank_surface.get_rect(center=(495, 230))
        self.lock_three_rect = self.lock_surf.get_rect(center=(495, 230))

        self.wood_plank_rectangle_four = self.wood_plank_surface.get_rect(center=(650, 230))
        self.lock_four_rect = self.lock_surf.get_rect(center=(650, 230))

        self.wood_plank_rectangle_five = self.wood_plank_surface.get_rect(center=(805, 230))
        self.lock_five_rect = self.lock_surf.get_rect(center=(805, 230))

        self.wood_plank_rectangle_six = self.wood_plank_surface.get_rect(center=(180, 410))
        self.lock_six_rect = self.lock_surf.get_rect(center=(180, 410))

        self.wood_plank_rectangle_seven = self.wood_plank_surface.get_rect(center=(335, 410))
        self.lock_seven_rect = self.lock_surf.get_rect(center=(335, 410))

        self.wood_plank_rectangle_eight = self.wood_plank_surface.get_rect(center=(495, 410))
        self.lock_eight_rect = self.lock_surf.get_rect(center=(495, 410))

        self.wood_plank_rectangle_nine = self.wood_plank_surface.get_rect(center=(650, 410))
        self.lock_nine_rect = self.lock_surf.get_rect(center=(650, 410))

        self.wood_plank_rectangle_ten = self.wood_plank_surface.get_rect(center=(805, 410))
        self.lock_ten_rect = self.lock_surf.get_rect(center=(805, 410))

        if database.stage_level == 1:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_two_rect)
            self.screen.blit(self.lock_surf, self.lock_three_rect)
            self.screen.blit(self.lock_surf, self.lock_four_rect)
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement(winner, played_time)
            self.blit_star()
        elif database.stage_level == 2:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_three_rect)
            self.screen.blit(self.lock_surf, self.lock_four_rect)
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement(winner, played_time)
            self.blit_star()
        elif database.stage_level == 3:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_four_rect)
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement(winner, played_time)
            self.blit_star()
        elif database.stage_level == 4:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_five_rect)
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement(winner, played_time)
            self.blit_star()
        elif database.stage_level == 5:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_six_rect)
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement(winner, played_time)
            self.blit_star()
        elif database.stage_level == 6:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_seven_rect)
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement(winner, played_time)
            self.blit_star()
        elif database.stage_level == 7:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_eight_rect)
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement(winner, played_time)
            self.blit_star()
        elif database.stage_level == 8:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_nine_rect)
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement(winner, played_time)
            self.blit_star()
        elif database.stage_level == 9:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_nine)
            self.screen.blit(self.level_bg, (0, 0))
            self.screen.blit(self.lock_surf, self.lock_ten_rect)
            self.achievement(winner, played_time)
            self.blit_star()
        elif database.stage_level == 10:
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_back)
            self.screen.blit(self.wood_plank_surface_back_and_store, self.wood_plank_rectangle_store)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_one)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_two)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_three)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_four)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_five)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_six)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_seven)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_eight)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_nine)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle_ten)
            self.screen.blit(self.level_bg, (0, 0))
            self.achievement(winner, played_time)
            self.blit_star()

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.update_user()
                database.push_data()
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.wood_plank_rectangle_store.collidepoint(pygame.mouse.get_pos()):
                    self.level_select_music.stop()
                    self.go_store_py = True

                if self.wood_plank_rectangle_back.collidepoint(pygame.mouse.get_pos()):
                    self.level_select_music.stop()
                    self.go_home_py = True

                if database.stage_level >= 1:
                    if self.wood_plank_rectangle_one.collidepoint(pygame.mouse.get_pos()):
                        database.lvl_choose = 1
                        self.go_stick_of_war = True

                if database.stage_level >= 2:
                    if self.wood_plank_rectangle_two.collidepoint(pygame.mouse.get_pos()):
                        database.lvl_choose = 2
                        self.go_stick_of_war = True

                if database.stage_level >= 3:
                    if self.wood_plank_rectangle_three.collidepoint(pygame.mouse.get_pos()):
                        database.lvl_choose = 3
                        self.go_stick_of_war = True

                if database.stage_level >= 4:
                    if self.wood_plank_rectangle_four.collidepoint(pygame.mouse.get_pos()):
                        database.lvl_choose = 4
                        self.go_stick_of_war = True

                if database.stage_level >= 5:
                    if self.wood_plank_rectangle_five.collidepoint(pygame.mouse.get_pos()):
                        database.lvl_choose = 5
                        self.go_stick_of_war = True

                if database.stage_level >= 6:
                    if self.wood_plank_rectangle_six.collidepoint(pygame.mouse.get_pos()):
                        database.lvl_choose = 6
                        self.go_stick_of_war = True

                if database.stage_level >= 7:
                    if self.wood_plank_rectangle_seven.collidepoint(pygame.mouse.get_pos()):
                        database.lvl_choose = 7
                        self.go_stick_of_war = True

                if database.stage_level >= 8:
                    if self.wood_plank_rectangle_eight.collidepoint(pygame.mouse.get_pos()):
                        database.lvl_choose = 8
                        self.go_stick_of_war = True

                if database.stage_level >= 9:
                    if self.wood_plank_rectangle_nine.collidepoint(pygame.mouse.get_pos()):
                        database.lvl_choose = 9
                        self.go_stick_of_war = True

                if database.stage_level >= 10:
                    if self.wood_plank_rectangle_ten.collidepoint(pygame.mouse.get_pos()):
                        database.lvl_choose = 10
                        self.go_stick_of_war = True

    def blit_star(self):
        if database.stage_level >= 1:
            self.screen.blit(database.star_one_surf, self.star_one_rect)
        if database.stage_level >= 2:
            self.screen.blit(database.star_two_surf, self.star_two_rect)
        if database.stage_level >= 3:
            self.screen.blit(database.star_three_surf, self.star_three_rect)
        if database.stage_level >= 4:
            self.screen.blit(database.star_four_surf, self.star_four_rect)
        if database.stage_level >= 5:
            self.screen.blit(database.star_five_surf, self.star_five_rect)
        if database.stage_level >= 6:
            self.screen.blit(database.star_six_surf, self.star_six_rect)
        if database.stage_level >= 7:
            self.screen.blit(database.star_seven_surf, self.star_seven_rect)
        if database.stage_level >= 8:
            self.screen.blit(database.star_eight_surf, self.star_eight_rect)
        if database.stage_level >= 9:
            self.screen.blit(database.star_nine_surf, self.star_nine_rect)
        if database.stage_level >= 10:
            self.screen.blit(database.star_ten_surf, self.star_ten_rect)

    def achievement(self, winner, played_time):
        if winner == "Enemy":
            if database.lvl_choose != 100:
                database.money += int(10 + database.lvl_choose * 1.3)
                database.lvl_choose = 100
        elif winner == "User":
            if database.lvl_choose == 1:
                if 0 <= played_time <= 120000:
                    database.star_one_surf = self.three_star_surf
                    database.money += (30 + database.lvl_choose * 15)

                elif 120000 < played_time <= 240000:
                    database.star_one_surf = self.two_star_surf
                    database.money += (30 + database.lvl_choose * 5)

                elif played_time > 240000:
                    database.star_one_surf = self.one_star_surf
                    database.money += (20 + database.lvl_choose * 2)

                database.lvl_choose = 100

            if database.lvl_choose == 2:
                if 0 <= played_time <= 120000:
                    database.star_two_surf = self.three_star_surf
                    database.money += (30 + database.lvl_choose * 15)

                elif 120000 < played_time <= 240000:
                    database.star_two_surf = self.two_star_surf
                    database.money += (30 + database.lvl_choose * 5)

                elif played_time > 240000:
                    database.star_two_surf = self.one_star_surf
                    database.money += (20 + database.lvl_choose * 2)

                database.lvl_choose = 100

            if database.lvl_choose == 3:
                if 0 <= played_time <= 120000:
                    database.star_three_surf = self.three_star_surf
                    database.money += (30 + database.lvl_choose * 15)

                elif 120000 < played_time <= 240000:
                    database.star_three_surf = self.two_star_surf
                    database.money += (30 + database.lvl_choose * 5)

                elif played_time > 240000:
                    database.star_three_surf = self.one_star_surf
                    database.money += (20 + database.lvl_choose * 2)

                database.lvl_choose = 100

            if database.lvl_choose == 4:
                if 0 <= played_time <= 120000:
                    database.star_four_surf = self.three_star_surf
                    database.money += (30 + database.lvl_choose * 15)

                elif 120000 < played_time <= 240000:
                    database.star_four_surf = self.two_star_surf
                    database.money += (30 + database.lvl_choose * 5)

                elif played_time > 240000:
                    database.star_four_surf = self.one_star_surf
                    database.money += (20 + database.lvl_choose * 2)

                database.lvl_choose = 100

            if database.lvl_choose == 5:
                if 0 <= played_time <= 120000:
                    database.star_five_surf = self.three_star_surf
                    database.money += (30 + database.lvl_choose * 15)

                elif 120000 < played_time <= 240000:
                    database.star_five_surf = self.two_star_surf
                    database.money += (30 + database.lvl_choose * 5)

                elif played_time > 240000:
                    database.star_five_surf = self.one_star_surf
                    database.money += (20 + database.lvl_choose * 2)

                database.lvl_choose = 100

            if database.lvl_choose == 6:
                if 0 <= played_time <= 120000:
                    database.star_six_surf = self.three_star_surf
                    database.money += (30 + database.lvl_choose * 15)

                elif 120000 < played_time <= 240000:
                    database.star_six_surf = self.two_star_surf
                    database.money += (30 + database.lvl_choose * 5)

                elif played_time >= 240000:
                    database.star_six_surf = self.one_star_surf
                    database.money += (20 + database.lvl_choose * 2)

                database.lvl_choose = 100

            if database.lvl_choose == 7:
                if 0 <= played_time <= 120000:
                    database.star_seven_surf = self.three_star_surf
                    database.money += (30 + database.lvl_choose * 15)

                elif 120000 < played_time <= 240000:
                    database.star_seven_surf = self.two_star_surf
                    database.money += (30 + database.lvl_choose * 5)

                elif played_time >= 240000:
                    database.star_seven_surf = self.one_star_surf
                    database.money += (20 + database.lvl_choose * 2)

                database.lvl_choose = 100

            if database.lvl_choose == 8:
                if 0 <= played_time <= 120000:
                    database.star_eight_surf = self.three_star_surf
                    database.money += (30 + database.lvl_choose * 15)

                elif 120000 < played_time <= 240000:
                    database.star_eight_surf = self.two_star_surf
                    database.money += (30 + database.lvl_choose * 5)

                elif played_time >= 240000:
                    database.star_eight_surf = self.one_star_surf
                    database.money += (20 + database.lvl_choose * 2)

                database.lvl_choose = 100

            if database.lvl_choose == 9:
                if 0 <= played_time <= 120000:
                    database.star_nine_surf = self.three_star_surf
                    database.money += (30 + database.lvl_choose * 15)

                elif 120000 < played_time <= 240000:
                    database.star_nine_surf = self.two_star_surf
                    database.money += (30 + database.lvl_choose * 5)

                elif played_time > 240000:
                    database.star_nine_surf = self.one_star_surf
                    database.money += (20 + database.lvl_choose * 2)

                database.lvl_choose = 100

            if database.lvl_choose == 10:
                if 0 <= played_time <= 120000:
                    database.star_ten_surf = self.three_star_surf
                    database.money += (30 + database.lvl_choose * 15)

                elif 120000 < played_time <= 240000:
                    database.star_ten_surf = self.two_star_surf
                    database.money += (30 + database.lvl_choose * 5)

                elif played_time > 240000:
                    database.star_ten_surf = self.one_star_surf
                    database.money += (20 + database.lvl_choose * 2)

                database.lvl_choose = 100


    def run(self):
        self.level_select_music = pygame.mixer.Sound('War of stick/Music/level.mp3')
        self.level_select_music.set_volume(0.2)
        self.level_select_music.play(loops=-1)

        while True:
            self.screen.fill((255, 255, 255))

            self.choose_level(stick_of_war.winner,stick_of_war.played_time)

            self.event_handling()

            pygame.display.update()
            self.clock.tick(60)



"""
"""
"""
"""
"""
"""

# coding: utf-8



# game start from here
# have to initialise the pygame first
# pygame.init()
# pygame.font.init()
# pygame.display.set_caption('Pokemon vs Naruto')  # title name
# pygame.display.set_mode((1000, 600))


class Tools:
    def find_grid_coor(self, pos, grid_coor, num_ball, hero_type):
        # check whether out of map
        # 312 - 42 = 272 ( least x ) , 927 + 42 = 967 ( max x )
        # 172 - 45 = 127 ( least y ) , 532 + 45 = 577 ( max x )
        if pos[0] < 272 or pos[0] > 967 or pos[1] < 127 or pos[1] > 577:
            return None

        if hero_type == 'machine':
            if num_ball < 50:
                return None
        elif hero_type == 'archer':
            if num_ball < 150:
                return None
        elif hero_type == 'wizard':
            if num_ball < 100:
                return None

        # check at which column (finding coordinate x)
        for i, column in enumerate(grid_coor):
            # cause our grid_coor is center so use + and - to get the max result
            if grid_coor[i][0][0] - 42 <= pos[0] and grid_coor[i][0][0] + 42 >= pos[0]:
                # check at which row (finding coordinate y), will output the coor for x and y
                for coor in column:
                    if coor[1] - 45 <= pos[1] and coor[1] + 45 >= pos[1]:
                        if coor[2] == 1:
                            return None
                        elif coor[2] == 0:
                            coor[2] = 1
                            return (coor[0], coor[1])  # return coordinate where hero have to stay


class Gem_Ball:
    def __init__(self):
        self.gem_ball_surface = pygame.image.load('Plant vs Stick/Picture/utils/diamond_ball.png').convert_alpha()
        self.gem_ball_surface = pygame.transform.scale(self.gem_ball_surface, (50, 50))
        self.gem_ball_rect_storage = []

    def create_gem_ball(self):
        gem_ball_rectangle = self.gem_ball_surface.get_rect(center=(randint(312, 927), randint(-250, -100)))
        self.gem_ball_rect_storage.append(gem_ball_rectangle)

    def drop_gem_ball(self):
        for gem_ball_rect in self.gem_ball_rect_storage:
            # dropping from up and stop at bottom
            if gem_ball_rect.y < 535:
                gem_ball_rect.y += 0.6  # speed cannot below 0.6


# load hero frame
machine_frame = [
                    pygame.image.load('Plant vs Stick/Picture/machine/machine_1.png').convert_alpha() for _ in
                    range(30)] + [pygame.image.load('Plant vs Stick/Picture/machine/machine_2.png').convert_alpha()
                                  ]

wizard_normal = [pygame.image.load('Plant vs Stick/Picture/wizard/wizard_1.png').convert_alpha(),
                   pygame.image.load('Plant vs Stick/Picture/wizard/wizard_2.png').convert_alpha()]

archer_normal = [pygame.image.load('Plant vs Stick/Picture/archer/archer_1.png').convert_alpha(),
                  pygame.image.load('Plant vs Stick/Picture/archer/archer_2.png').convert_alpha()]

wizard_attack = [pygame.image.load('Plant vs Stick/Picture/wizard/wizard_3.png').convert_alpha(),
                   pygame.image.load('Plant vs Stick/Picture/wizard/wizard_4.png').convert_alpha(),
                   pygame.image.load('Plant vs Stick/Picture/wizard/wizard_5.png').convert_alpha()]

archer_attack = [pygame.image.load('Plant vs Stick/Picture/archer/archer_attack_1.png').convert_alpha(),
                  pygame.image.load('Plant vs Stick/Picture/archer/archer_attack_2.png').convert_alpha(),
                  pygame.image.load('Plant vs Stick/Picture/archer/archer_attack_3.png').convert_alpha(),
                  pygame.image.load('Plant vs Stick/Picture/archer/archer_attack_4.png').convert_alpha(),
                  pygame.image.load('Plant vs Stick/Picture/archer/archer_attack_5.png').convert_alpha(),
                  pygame.image.load('Plant vs Stick/Picture/archer/archer_attack_6.png').convert_alpha(),]


class Hero(pygame.sprite.Sprite):
    # hero
    def __init__(self, hero_type, placing_coordinate):
        super().__init__()

        self.hero_type = hero_type
        self.placing_coordinate = placing_coordinate

        if self.hero_type == 'machine':
            self.normal_frames = [pygame.transform.scale(frame, (70, 82)) for frame in machine_frame]
            self.health = 300
        elif self.hero_type == 'archer':
            self.attack_frames = [pygame.transform.scale(frame, (75, 82)) for frame in archer_attack]
            self.normal_frames = [pygame.transform.scale(frame, (75, 82)) for frame in archer_normal]
            self.health = 180
            self.bullet_speed = 5
        elif self.hero_type == 'wizard':
            self.attack_frames = [pygame.transform.scale(frame, (75, 82)) for frame in wizard_attack]
            self.normal_frames = [pygame.transform.scale(frame, (75, 82)) for frame in wizard_normal]
            self.health = 200
            self.bullet_speed = 4
        else:
            print('No hero found')

        self.frames = self.normal_frames
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(center=(self.placing_coordinate))

        self.archer_bullet_surface = pygame.image.load('Plant vs Stick/Picture/archer/archer_bullet.png').convert_alpha()
        self.archer_bullet_surface = pygame.transform.scale(self.archer_bullet_surface, (50, 10))

        self.wizard_bullet_surface = pygame.image.load('Plant vs Stick/Picture/wizard/wizard_bullet.png').convert_alpha()
        self.wizard_bullet_surface = pygame.transform.scale(self.wizard_bullet_surface, (20, 20))

        self.machine_ball_surface = pygame.image.load('Plant vs Stick/Picture/utils/diamond_ball.png').convert_alpha()
        self.machine_ball_surface = pygame.transform.scale(self.machine_ball_surface, (25, 25))

        # this list will store all active bullet
        self.bullet_rect_storage = []

    def change_mode(self, mode):
        if self.hero_type == 'archer' or self.hero_type == 'wizard':
            if mode == 'attacking':
                self.frames = self.attack_frames
            if mode == 'normal':
                self.frames = self.normal_frames

    def update_animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.create_bullet()
            self.animation_index = 0

        self.image = self.frames[int(self.animation_index)]

    def create_bullet(self):
        # bullet created append into the list
        if self.hero_type == 'archer':
            new_bullet = self.archer_bullet_surface.get_rect(center=self.rect.center)
        elif self.hero_type == 'wizard':
            new_bullet = self.wizard_bullet_surface.get_rect(center=self.rect.center)
        elif self.hero_type == 'machine':
            new_bullet = self.machine_ball_surface.get_rect(
                center=((self.rect.bottomright[0] + randint(-15, 15)), ((self.rect.bottomright[1] + randint(-15, 15)))))
        self.bullet_rect_storage.append(new_bullet)

    def move_bullet(self):
        for bullet_rect in self.bullet_rect_storage:
            bullet_rect.x += self.bullet_speed  # Move the bullet to the right of Pikachu
            if bullet_rect.x > 1030:
                # Remove bullets that have moved off-screen
                self.bullet_rect_storage.remove(bullet_rect)

    def update(self):
        self.update_animation_state()


# load stickman image
stickman_warrior_image = [
    pygame.image.load('Plant vs Stick/Picture/stickman sword/stickman sword run/stickman sword run 1.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman sword/stickman sword run/stickman sword run 2.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman sword/stickman sword run/stickman sword run 3.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman sword/stickman sword run/stickman sword run 4.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman sword/stickman sword run/stickman sword run 5.png').convert_alpha()]

stickman_sparta_image = [
    pygame.image.load('Plant vs Stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 1.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 2.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 3.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 4.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman sparta/stickman sparta run/stickman sparta run 5.png').convert_alpha()]

stickman_giant_image = [
    pygame.image.load('Plant vs Stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 1.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 2.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 3.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 4.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman giant/stickman giant walk/stickman Giant walk 5.png').convert_alpha()]

# load stickman attack image
stickman_warrior_attack = [
    pygame.image.load('Plant vs Stick/Picture/stickman sword/stickman sword attack/stickman sword attack 1.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman sword/stickman sword attack/stickman sword attack 2.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman sword/stickman sword attack/stickman sword attack 3.png').convert_alpha()]

stickman_sparta_attack = [
    pygame.image.load('Plant vs Stick/Picture/stickman sparta/stickman sparta attack/stickman sparta attack 1.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman sparta/stickman sparta attack/stickman sparta attack 2.png').convert_alpha()]

stickman_giant_attack = [
    pygame.image.load('Plant vs Stick/Picture/stickman giant/stickman giant attack/stickman giant attack 1.png').convert_alpha(),
    pygame.image.load('Plant vs Stick/Picture/stickman giant/stickman giant attack/stickman giant attack 2.png').convert_alpha()]


class Troop(pygame.sprite.Sprite):
    # load image

    def __init__(self, troop_type, all_grid_coor):
        super().__init__()

        self.troop_type = troop_type
        self.all_grid_coor = all_grid_coor

        if troop_type == 'warrior':
            self.frames = [pygame.transform.scale(frame, (84, 45)) for frame in stickman_warrior_image]
            self.frame = [pygame.transform.scale(frame, (84, 45)) for frame in stickman_warrior_attack]
            self.speed = 1
            self.health = 120
            self.attack = 20
            self.cooldown = 0
        elif troop_type == 'sparta':
            self.frames = [pygame.transform.scale(frame, (110, 85)) for frame in stickman_sparta_image]
            self.frame = [pygame.transform.scale(frame, (110, 85)) for frame in stickman_sparta_attack]
            self.speed = 1
            self.health = 110
            self.attack = 25
            self.cooldown = 0
        elif troop_type == 'giant':
            self.frames = [pygame.transform.scale(frame, (110, 85)) for frame in stickman_giant_image]
            self.frame = [pygame.transform.scale(frame, (110, 85)) for frame in stickman_giant_attack]
            self.speed = 1
            self.health = 110
            self.attack = 25
            self.cooldown = 0
        else:
            print('No ninja found')

        self.original_speed = self.speed

        # spawn at these position
        self.spawn_y = choice([172, 262, 352, 442, 532])
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(center=(randint(1100, 2000), self.spawn_y))

        self.animation_attack_index = 0
        self.image = self.frame[self.animation_attack_index]

    def update_animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def animation_attack_state(self):
        self.animation_attack_index += 0.1
        if self.animation_attack_index >= len(self.frame):
            self.animation_attack_index = 0
        self.image = self.frame[int(self.animation_attack_index)]

    def update(self, hero_groups):
        self.update_animation_state()

        if self.cooldown > 0:
            self.cooldown -= 1

        self.rect.x -= self.speed

        collisions = pygame.sprite.spritecollide(self, hero_groups, False)
        if collisions:
            self.speed = 0
            self.animation_attack_state()
            if self.cooldown == 0:
                for hero in collisions:
                    hero.health -= self.attack

                    self.cooldown = 60
                    if hero.health <= 0:
                        coor_with_1 = []
                        for column in self.all_grid_coor:
                            for coor in column:
                                if coor[2] == 1:
                                    coor_with_1.append(coor)
                                    if [hero.rect.centerx, hero.rect.centery, 1] in coor_with_1:
                                        coor[2] = 0
                        hero.kill()
                        self.speed = self.original_speed
        else:
            self.speed = self.original_speed

    def troop_being_attack(self, damage):
        self.health -= damage

    def check_troop_die(self):
        if self.health <= 0:
            self.kill()
            return True


class GamePokemonVsStick:
    def __init__(self):
        # pygame.init()
        # pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))  # screen size
        self.machine_card_initial_position = (120, 8)
        self.archer_card_initial_position = (191, 8)
        self.wizard_card_initial_position = (262, 8)
        self.reset_func()

    def reset_func(self):
            self.before_press_start = True  # main menu
            self.after_press_start = False  # game start
            self.begin_time = None

            # Groups
            self.troop_groups = pygame.sprite.Group()
            self.hero_groups = pygame.sprite.Group()

            # reset game state for play again
            self.reset_game_state()

            # set up gem_ball_drop_timer
            self.gem_ball_timer = pygame.USEREVENT + 2
            pygame.time.set_timer(self.gem_ball_timer, 16000)

            # choice of ninja
            self.troop_choice = ['warrior', 'sparta', 'giant']

    def reset_game_state(self):

        # set up Ninja timer
        self.troop_timer = pygame.USEREVENT + 1
        self.spawn_time = 8000
        pygame.time.set_timer(self.troop_timer, self.spawn_time)

        self.num_ball = 500
        self.chosen_hero = None
        self.coordinate = None
        self.remaining_time = None
        self.help_menu_page = None
        self.lose = False
        self.wave = 1
        self.row_with_troop = []
        # center coordinate for each box
        # x = [312, 400, 486, 577, 663, 750, 838, 927]
        # y = [172, 262, 352, 442, 532]
        # grid_coor [0] is x_coor , [1] is y_coor , [2] is the grid been taken
        self.grid_coor = [
            [[312, 172, 0], [312, 262, 0], [312, 352, 0], [312, 442, 0], [312, 532, 0]],
            [[400, 172, 0], [400, 262, 0], [400, 352, 0], [400, 442, 0], [400, 532, 0]],
            [[486, 172, 0], [486, 262, 0], [486, 352, 0], [486, 442, 0], [486, 532, 0]],
            [[577, 172, 0], [577, 262, 0], [577, 352, 0], [577, 442, 0], [577, 532, 0]],
            [[663, 172, 0], [663, 262, 0], [663, 352, 0], [663, 442, 0], [663, 532, 0]],
            [[750, 172, 0], [750, 262, 0], [750, 352, 0], [750, 442, 0], [750, 532, 0]],
            [[838, 172, 0], [838, 262, 0], [838, 352, 0], [838, 442, 0], [838, 532, 0]],
            [[927, 172, 0], [927, 262, 0], [927, 352, 0], [927, 442, 0], [927, 532, 0]]
        ]
        self.tools = Tools()
        self.spawned_ball = Gem_Ball()
        self.troop_groups.empty()
        self.hero_groups.empty()

        self.go_home_py = False
        self.set_up()  # set up surface and rectangle etc

    def set_up(self):  # set up surface and rectangle etc
        # main menu surface and rect
        self.welcome_surface = pygame.image.load('Plant vs Stick/Picture/utils/welcome.jpg').convert()
        self.welcome_surface = pygame.transform.scale(self.welcome_surface, (1000, 600))

        self.start_adventure_surface = pygame.image.load('Plant vs Stick/Picture/utils/white_screen.jpeg').convert()
        self.start_adventure_surface = pygame.transform.scale(self.start_adventure_surface, (410, 100))
        self.start_adventure_rect = self.start_adventure_surface.get_rect(topleft=(510, 70))

        username_font = pygame.font.Font(None, 30)
        self.username_surface = username_font.render(database.username, True, 'Green')
        self.username_rectangle = self.username_surface.get_rect(center=(257, 90))

        press_h_font = pygame.font.Font(None, 35)
        self.h_surface = press_h_font.render(("Press 'h' for help menu. You can find guides there"), True, 'White')
        self.h_rectangle = self.h_surface.get_rect(center=(500, 570))

        self.help_menu_font = pygame.font.Font(None, 20)
        # Read the help_menu_file file
        with open("Plant vs Stick/Data/help_menu.txt", "r") as file:
            self.help_menu_content = file.read()
        self.help_menu_page = False

        # game start surface and rect
        self.background_surface = pygame.image.load('Plant vs Stick/Picture/utils/game_background.png').convert()
        self.background_surface = pygame.transform.scale(self.background_surface, (1000, 600))

        self.machine_card_surface = pygame.image.load('Plant vs Stick/Picture/machine/machine_card.png').convert()
        self.machine_card_surface = pygame.transform.scale(self.machine_card_surface, (68, 83))
        self.machine_card_rectangle = self.machine_card_surface.get_rect(topleft=self.machine_card_initial_position)

        self.archer_card_surface = pygame.image.load('Plant vs Stick/Picture/archer/archer_card.png').convert()
        self.archer_card_surface = pygame.transform.scale(self.archer_card_surface, (68, 83))
        self.archer_card_rectangle = self.archer_card_surface.get_rect(topleft=self.archer_card_initial_position)

        self.wizard_card_surface = pygame.image.load('Plant vs Stick/Picture/wizard/wizard_card.png').convert()
        self.wizard_card_surface = pygame.transform.scale(self.wizard_card_surface, (68, 83))
        self.wizard_card_rectangle = self.wizard_card_surface.get_rect(topleft=self.wizard_card_initial_position)

        self.num_ball_font = pygame.font.Font(None, 30)
        self.num_ball_surface = self.num_ball_font.render(str(self.num_ball), True, 'Black')
        self.num_ball_rectangle = self.num_ball_surface.get_rect(center=(65, 85))

        self.wave_font = pygame.font.Font(None, 50)
        self.wave_surface = self.wave_font.render(f'Wave {self.wave}', True, 'White')
        self.wave_rectangle = self.wave_surface.get_rect(center=(80, 580))

        self.wave_background_surf = pygame.image.load('Plant vs Stick/Picture/utils/wave_background.jpeg').convert()
        self.wave_background_surf = pygame.transform.scale(self.wave_background_surf, (140, 50))
        self.wave_background_rect = self.wave_background_surf.get_rect(center=(80, 580))

        self.wood_plank_surface = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.wood_plank_surface = pygame.transform.scale(self.wood_plank_surface, (140, 50))
        self.wood_plank_rectangle = self.wood_plank_surface.get_rect(topleft=(850, 10))
        self.time = None
        self.timer = pygame.font.Font(None, 36).render(None, True, (255, 255, 255))
        self.timer_rectangle = self.timer.get_rect(center=(890, 35))

        self.back_background_size = (250, 55)
        self.back_background_surf = pygame.surface.Surface(self.back_background_size)
        self.back_background_surf.fill((14, 25, 45))
        self.back_background_rect = self.back_background_surf.get_rect(center=(254, 40))

        self.back_button_surf = pygame.image.load('War of stick/Picture/Store/back_to_level.png').convert_alpha()
        self.back_button_surf = pygame.transform.scale(self.back_button_surf, (75, 75))
        self.back_button_rect = self.back_button_surf.get_rect(center=(155, 40))

        self.back_word_surf = pygame.font.Font(None, 42)
        self.back_word_surf = self.back_word_surf.render('Back to Home', True, "Green")
        self.back_word_rect = self.back_word_surf.get_rect(center=(270, 40))

    def event_handling(self):
        # Event handling
        for event in pygame.event.get():
            # press 'x' to quit the game
            if event.type == pygame.QUIT:
                database.update_user()
                database.push_data()
                pygame.quit()
                exit()

            if self.before_press_start and event.type == pygame.KEYDOWN:
                if not self.help_menu_page and event.key == pygame.K_h:  # if press 'h' for Help
                    self.help_menu_page = True
                    self.before_press_start = False

            elif self.help_menu_page and event.type == pygame.KEYDOWN:
                if not self.before_press_start and event.key == pygame.K_h:  # if press 'h' for Help
                    self.before_press_start = True
                    self.help_menu_page = False

            # press 'start adventure' in the home page, then game will start
            if event.type == pygame.MOUSEBUTTONDOWN and self.start_adventure_rect.collidepoint(
                    event.pos) and self.before_press_start:
                self.after_press_start = True
                self.before_press_start = False
                self.begin_time = pygame.time.get_ticks()  # this record the initial countdown and i put here coz to only program the time when user move to next page

            # spawned ninja
            if event.type == self.troop_timer and self.after_press_start:
                spawned_troop = Troop((choice(self.troop_choice)), self.grid_coor)
                self.troop_groups.add(spawned_troop)

            # spawned gem_ball from sky
            if event.type == self.gem_ball_timer and self.after_press_start:
                self.spawned_ball.create_gem_ball()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # press hero card from the top , and chosen hero will be that
                if self.machine_card_rectangle.collidepoint(event.pos):
                    self.chosen_hero = 'machine'
                elif self.archer_card_rectangle.collidepoint(event.pos):
                    self.chosen_hero = 'archer'
                elif self.wizard_card_rectangle.collidepoint(event.pos):
                    self.chosen_hero = 'wizard'

                # if pressed gem_ball from sky , earned 50 num_ball
                for gem_ball_rect in self.spawned_ball.gem_ball_rect_storage:
                    if gem_ball_rect.collidepoint(event.pos):
                        self.spawned_ball.gem_ball_rect_storage.remove(gem_ball_rect)
                        self.num_ball += 50
                        break

                # if pressed gem_ball from machine , earned 25 num_ball
                for machine_hero in self.hero_groups:
                    if machine_hero.hero_type == 'machine':
                        for bullet_rect in machine_hero.bullet_rect_storage:
                            if bullet_rect.collidepoint(event.pos):
                                machine_hero.bullet_rect_storage.remove(bullet_rect)
                                self.num_ball += 25
                                break

            # drag the hero card chosen just now
            if self.chosen_hero and event.type == pygame.MOUSEMOTION:
                # card follow the mouse pos
                if self.chosen_hero == 'machine':
                    self.machine_card_rectangle.move_ip(event.rel)
                elif self.chosen_hero == 'archer':
                    self.archer_card_rectangle.move_ip(event.rel)
                elif self.chosen_hero == 'wizard':
                    self.wizard_card_rectangle.move_ip(event.rel)

            # button_up after dragging hero , hero planted and back to the initial position
            if event.type == pygame.MOUSEBUTTONUP and self.chosen_hero is not None:
                # check hero release at which coordinate and enough num_ball or not
                # return None if the position release hero card is unavailable (out of map / already have hero)
                # return the x and y coordinate of the box for planting if available
                self.coordinate = self.tools.find_grid_coor(event.pos, self.grid_coor, self.num_ball,
                                                            self.chosen_hero)

                if self.coordinate is not None:  # not None which mean by is available for planting
                    if self.chosen_hero == 'machine':
                        self.num_ball -= 50
                        if not self.machine_card_rectangle.topleft == self.machine_card_initial_position:
                            self.machine_card_rectangle.topleft = self.machine_card_initial_position  # Snap back to initial position

                    elif self.chosen_hero == 'archer':
                        self.num_ball -= 150
                        if not self.archer_card_rectangle.topleft == self.archer_card_initial_position:
                            self.archer_card_rectangle.topleft = self.archer_card_initial_position  # Snap back to initial position

                    elif self.chosen_hero == 'wizard':
                        self.num_ball -= 100
                        if not self.wizard_card_rectangle.topleft == self.wizard_card_initial_position:
                            self.wizard_card_rectangle.topleft = self.wizard_card_initial_position  # Snap back to initial position

                    # chosen heri spawned at the box with the coordinate returned above
                    spawned_hero = Hero(self.chosen_hero, self.coordinate)
                    self.hero_groups.add(spawned_hero)

                # if return None which mean by not available for planting
                # card snap back without deducting num_balls
                if self.coordinate is None:
                    if self.chosen_hero == 'machine':
                        if not self.machine_card_rectangle.topleft == self.machine_card_initial_position:
                            self.machine_card_rectangle.topleft = self.machine_card_initial_position

                    elif self.chosen_hero == 'archer':
                        if not self.archer_card_rectangle.topleft == self.archer_card_initial_position:
                            self.archer_card_rectangle.topleft = self.archer_card_initial_position

                    elif self.chosen_hero == 'wizard':
                        if not self.wizard_card_rectangle.topleft == self.wizard_card_initial_position:
                            self.wizard_card_rectangle.topleft = self.wizard_card_initial_position

                # clear
                self.chosen_hero = None
                self.coordinate = None

            # player can choose to turn back to main menu(before press start) or play again(after press start)
            if self.lose and event.type == pygame.MOUSEBUTTONDOWN:
                if self.home_page_rect.collidepoint(event.pos):
                    self.reset_game_state()
                    self.before_press_start = True
                    self.after_press_start = False
                elif self.play_again_rect.collidepoint(event.pos):
                    self.reset_game_state()
                    self.after_press_start = True
                    self.before_press_start = False
                    self.begin_time = pygame.time.get_ticks()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.before_press_start and self.back_background_rect.collidepoint(mouse_pos):
                    self.bg_music.stop()
                    self.go_home_py = True

    def game_start(self):
        if self.before_press_start:  # main menu page
            self.screen.blit(self.start_adventure_surface, self.start_adventure_rect)
            self.screen.blit(self.welcome_surface, (0, 0))
            self.screen.blit(self.username_surface, self.username_rectangle)
            self.screen.blit(self.h_surface, self.h_rectangle)
            self.screen.blit(self.back_background_surf, self.back_background_rect)
            self.screen.blit(self.back_button_surf, self.back_button_rect)
            self.screen.blit(self.back_word_surf, self.back_word_rect)

        if self.help_menu_page:
            self.screen.fill((255, 255, 255))
            text_lines = self.help_menu_content.split('\n')
            y_position = 10

            for line in text_lines:
                text = self.help_menu_font.render(line, True, (0, 0, 0))
                self.screen.blit(text, (10, y_position))
                y_position += 20  # Adjust the line spacing as needed

        if self.after_press_start:  # game start
            self.num_ball_surface = self.num_ball_font.render(str(self.num_ball), None, 'Black')

            # timer
            exact_time = pygame.time.get_ticks()
            time_pass = (exact_time - self.begin_time) // 1000
            minutes = time_pass // 60
            seconds = time_pass % 60
            self.time = f"{minutes:02}:{seconds:02}"
            self.timer = pygame.font.Font(None, 36).render(self.time, True, (255, 255, 255))

            # wave
            if minutes >= self.wave:
                self.spawn_time = self.spawn_time // 3
                pygame.time.set_timer(self.troop_timer, self.spawn_time)
                self.wave = minutes + 1

                self.wave_surface = pygame.font.Font(None, 50).render(f'Wave {self.wave}', True, 'White')

            # blit all background
            self.screen.blit(self.background_surface, (0, 0))
            self.screen.blit(self.machine_card_surface, self.machine_card_rectangle)
            self.screen.blit(self.archer_card_surface, self.archer_card_rectangle)
            self.screen.blit(self.wizard_card_surface, self.wizard_card_rectangle)
            self.screen.blit(self.num_ball_surface, self.num_ball_rectangle)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle)
            self.screen.blit(self.timer, self.timer_rectangle)

            # update the frame of ninja and hero then draw them out
            self.hero_groups.draw(self.screen)
            self.hero_groups.update()
            self.troop_groups.draw(self.screen)
            self.troop_groups.update(self.hero_groups)

            # blit gem ball
            for gem_ball_rect in self.spawned_ball.gem_ball_rect_storage:
                self.spawned_ball.drop_gem_ball()
                self.screen.blit(self.spawned_ball.gem_ball_surface, gem_ball_rect)

            self.screen.blit(self.wave_background_surf, self.wave_background_rect)
            self.screen.blit(self.wave_surface, self.wave_rectangle)

            # three usage for this piece of code
            # 1. check ninja with hero in same row ( have to attack or not )
            # 2. change hero mode(attacking or normal)
            # 3. bullet dissapear when collide with ninja
            for hero in self.hero_groups:
                for troop in self.troop_groups:
                    # if ninja appear on screen and in same row with hero , add ninja to list
                    # y_coor same means same row
                    if troop.rect.centerx < 1025 and troop.rect.centery == hero.rect.centery:
                        if troop.rect.centery not in self.row_with_troop:
                            # append ninja into the list if this ninja is not in the list and change mode
                            self.row_with_troop.append(troop.rect.centery)
                            hero.change_mode('attacking')

                        die = troop.check_troop_die()
                        if die or troop.rect.centerx < (hero.rect.centerx - 30):
                            self.row_with_troop.remove(troop.rect.centery)
                            for hero in self.hero_groups:
                                if hero.hero_type != 'machine':
                                    hero.bullet_rect_storage = []
                            hero.change_mode('normal')

                    # bullet collide then cause damage and dissapear
                    for bullet_rect in hero.bullet_rect_storage:
                        if hero.hero_type != 'machine' and bullet_rect.colliderect(troop.rect):
                            hero.bullet_rect_storage.remove(bullet_rect)
                            if hero.hero_type == 'archer':
                                troop.troop_being_attack(25)
                            elif hero.hero_type == 'wizard':
                                troop.troop_being_attack(18)
                            break

            # move and blit bullet for hero in row_with_ninja
            for hero in self.hero_groups:
                if hero.rect.centery in self.row_with_troop:
                    if hero.hero_type == 'archer':
                        hero.move_bullet()
                        for bullet_rect in hero.bullet_rect_storage:
                            self.screen.blit(hero.archer_bullet_surface, bullet_rect)
                    elif hero.hero_type == 'wizard':
                        hero.move_bullet()
                        for bullet_rect in hero.bullet_rect_storage:
                            self.screen.blit(hero.wizard_bullet_surface, bullet_rect)

                if hero.hero_type == 'machine':
                    for bullet_rect in hero.bullet_rect_storage:
                        self.screen.blit(hero.machine_ball_surface, bullet_rect)  # Draw the gem ball

            # if ninja cross over to the house then lose
            for troop in self.troop_groups:
                if troop.rect.centerx < 250:
                    self.lose = True
                    self.after_press_start = False

        if self.lose:
            self.screen.fill((0, 0, 0))

            loss_message = pygame.font.Font(None, 135).render("K.O.", True, (255, 255, 255))
            loss_message_rect = loss_message.get_rect(center=(500, 145))
            self.screen.blit(loss_message, loss_message_rect)

            used_time = pygame.font.Font(None, 70).render(f'You survived for {self.time}', True, (255, 255, 255))
            used_time_rect = used_time.get_rect(center=(500, 250))
            self.screen.blit(used_time, used_time_rect)

            wave_message = pygame.font.Font(None, 70).render(f'You reached Wave {self.wave}', True, (255, 255, 255))
            wave_message_rect = wave_message.get_rect(center=(500, 335))
            self.screen.blit(wave_message, wave_message_rect)

            self.wood_plank_surface = pygame.transform.scale(self.wood_plank_surface, (200, 70))

            self.wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(350, 430))
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle)
            home_page = pygame.font.Font(None, 40).render('Home Page', True, (255, 255, 255))
            self.home_page_rect = home_page.get_rect(center=(350, 430))
            self.screen.blit(home_page, self.home_page_rect)

            self.wood_plank_rectangle = self.wood_plank_surface.get_rect(center=(650, 430))
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rectangle)
            play_again = pygame.font.Font(None, 40).render("Play Again", True, (255, 255, 255))
            self.play_again_rect = play_again.get_rect(center=(650, 430))
            self.screen.blit(play_again, self.play_again_rect)

    def run(self):
        self.bg_music = pygame.mixer.Sound('Plant vs Stick/audio/bg_music.mp3')
        self.bg_music.set_volume(0.1)
        self.bg_music.play(loops=-1)
        while True:
            # CLear screen
            self.screen.fill((255, 255, 255))

            # event_handling_control_function
            self.event_handling()

            # start function which will blit screen and etc
            self.game_start()

            pygame.display.update()
            pygame.display.flip()  # redraw the screen

            self.clock.tick(60)  # 60 fps



"""
"""
"""
"""

# coding : utf-8


# pygame.init()
# pygame.font.init()


class TroopButton:
    def __init__(self, game_instance, image, image_dim, flash, lock, size, position, price, cooldown_time, gold_cost, diamond_cost):
        self.size = size
        self.position = position
        self.image = image
        self.image_dim = image_dim
        self.flash = flash
        self.lock = lock
        self.image = pygame.transform.scale(self.image, self.size)
        self.image_dim = pygame.transform.scale(self.image_dim, self.size)
        self.flash = pygame.transform.scale(self.flash, self.size)
        self.lock = pygame.transform.scale(self.lock, self.size)
        self.price = price
        self.cooldown_time = cooldown_time
        self.gold_cost = gold_cost
        self.diamond_cost = diamond_cost
        self.rect = self.image.get_rect(center=self.position)
        self.clicked = False
        self.coordinate_x = 0
        self.last_clicked_time = 0
        self.remaining_cooldown = 0
        self.insufficient_currency = True
        self.flash_timer = 0
        self.flash_duration = 3000
        self.game = game_instance
        self.red = True

    def render_name(self, screen):
        font = pygame.font.Font(None, 15)
        lines = self.price.split('n')
        total_height = len(lines) * 15
        y_offset = -total_height / 2

        colors = [(255, 215, 0), (56, 182, 255)]  # gold, blue
        for line, color in zip(lines, colors):
            text = font.render(line, True, color)
            text_rect = text.get_rect(center=(self.position[0], self.position[1] + y_offset))
            text_rect.y += 46
            screen.blit(text, text_rect)
            y_offset += 8

    def draw(self, screen, troop_available):
        if troop_available == True:
            if self.game.num_gold < self.gold_cost or self.game.num_diamond < self.diamond_cost:
                self.insufficient_currency = True
            else:
                self.insufficient_currency = False

            if self.insufficient_currency or self.game.num_troops > 99:
                if self.clicked:
                    screen.blit(self.flash, self.rect)
                    self.testing(screen)
                if self.remaining_cooldown == 0:
                    screen.blit(self.flash, self.rect)
                    self.clicked = False
                self.red = True

            elif not self.insufficient_currency:
                if self.clicked:
                    screen.blit(self.image_dim, self.rect)
                    self.testing(screen)
                if self.remaining_cooldown == 0:
                    screen.blit(self.image, self.rect)
                    self.clicked = False
                self.red = False
        else:
            screen.blit(self.lock, self.rect)

        self.render_name(screen)

    def testing(self, screen):
        current_time = pygame.time.get_ticks()
        self.remaining_cooldown = max(0, self.cooldown_time - (current_time - self.last_clicked_time)) // 1000
        cooldown_font = pygame.font.Font(None, 70)
        cooldown_text = cooldown_font.render(f"{self.remaining_cooldown}", True, (255, 255, 255))
        cooldown_text_rect = cooldown_text.get_rect(center=(self.position[0], self.position[1]))
        screen.blit(cooldown_text, cooldown_text_rect)

    def is_clicked(self, mouse_pos):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_clicked_time >= self.cooldown_time and not self.red:
            if self.rect.collidepoint(mouse_pos):
                self.clicked = True
                self.last_clicked_time = current_time
                return True
        return False


class Troop:
    def __init__(self, game_instance, frame_storage, attack_frame_storage, health, attack_damage, speed, troop_width, troop_height,
                 troop_name, troop_size):
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
        self.normal_attack = attack_damage
        self.speed = speed
        self.normal_speed = speed
        self.troop_width = troop_width
        self.troop_height = troop_height
        self.troop_size = troop_size
        # communication between the Troop instance and the Game instance
        self.game = game_instance
        self.rect = (0, 0, 0, 0)
        self.bullet_on_court = []
        self.bullet_cooldown = 0
        self.raging = False
        self.rage_run = 0

    def spawn_troop(self, screen, bg_x):
        if self.troop_name == 'Giant':
            self.rect = self.image.get_rect(bottomright=(self.coordinate_x + bg_x, 520))
            screen.blit(self.image, self.rect)
        else:
            self.rect = self.image.get_rect(bottomright=(self.coordinate_x + bg_x, 500))
            screen.blit(self.image, self.rect)

    def update(self):
        self.previous_coor = self.coordinate_x
        self.coordinate_x += self.speed
        self.animation_index += self.speed / 5
        if self.animation_index >= len(self.frame_storage):
            self.animation_index = 0
        self.image = self.frame_storage[int(self.animation_index)]
        if self.raging and self.rage_run == 0:
            self.speed *= (1 + database.spell_storage["rage"][3])
            self.attack_damage *= (1 + database.spell_storage["rage"][3])
            self.rage_run += 1
        elif not self.raging and self.rage_run > 0:
            self.speed = self.normal_speed
            self.attack_damage = self.normal_attack
            self.rage_run = 0
            self.raging = False

    def troop_attack(self, bg_x):
        if self.troop_name == 'Archer' or self.troop_name == 'Wizard':
            self.bullet_cooldown += 1
            if self.bullet_cooldown >= 50:
                self.create_bullet(bg_x)
                self.bullet_cooldown = 0
            self.coordinate_x = self.previous_coor
            self.attack_frame_index += 0.2
        else:
            self.coordinate_x = self.previous_coor
            self.attack_frame_index += 0.2

    def attack(self, bg_x):
        self.attacking = True
        if self.attacking:
            self.troop_attack(bg_x)
            if self.attack_frame_index >= len(self.attack_frame_storage):
                self.attack_frame_index = 0
                self.attacking = False
            self.image = self.attack_frame_storage[int(self.attack_frame_index)]

    def create_bullet(self, bg_x):
        if self.troop_name == 'Archer':
            bullet = pygame.image.load('War of stick/Picture/utils/archer_bullet.png')
            bullet_surf = pygame.transform.scale(bullet, (20, 20))
            bullet_rect = bullet_surf.get_rect(center=(self.coordinate_x + bg_x, randint(435, 465)))
            new_bullet = [bullet_surf, bullet_rect]
        elif self.troop_name == 'Wizard':
            bullet = pygame.image.load('War of stick/Picture/utils/wizard_bullet.png')
            bullet_surf = pygame.transform.scale(bullet, (50, 50))
            bullet_rect = bullet_surf.get_rect(center=(self.coordinate_x + bg_x, randint(435, 465)))
            new_bullet = [bullet_surf, bullet_rect]
        self.bullet_on_court.append(new_bullet)

    def move_bullet(self, bg_x):
        for bullet in self.bullet_on_court:
            bullet[1].x += 5  # Move the bullet to the right of troop
            for ninja in self.game.enemy_on_court:
                if bullet[1].x > self.coordinate_x + bg_x + 600:
                    # Remove bullets that a far from stick man
                    self.bullet_on_court.remove(bullet)
                    break
                elif bullet[1].colliderect(ninja):
                    self.bullet_on_court.remove(bullet)
                    ninja.ninja_health -= self.attack_damage
                    break

    def take_damage(self, damage):
        self.health -= damage


class Ninja:
    def __init__(self, ninja_type, frame_storage, ninja_attack_frame_storage, ninja_health, ninja_speed, attack, ninja_coordinate_x):
        self.ninja_type = ninja_type
        self.frame_storage = frame_storage
        self.ninja_attack_frame_storage = ninja_attack_frame_storage
        self.ninja_health = ninja_health
        self.normal_speed = ninja_speed
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
        self.freezing = False
        self.run = 0

    def spawn_ninja(self, screen, bg_x):
        if self.ninja_type == 'naruto' and self.ninja_type == 'sasuke':
            self.rect = self.image.get_rect(bottomright=(self.ninja_coordinate_x + bg_x, 500))
            screen.blit(self.image, self.rect)
        else:
            self.rect = self.image.get_rect(bottomright=(self.ninja_coordinate_x + bg_x, 500))
            screen.blit(self.image, self.rect)

    def update_ninja(self):
        self.ninja_prev_coor = self.ninja_coordinate_x
        self.ninja_coordinate_x -= self.ninja_speed
        self.animation_index += self.ninja_speed / 10
        if self.animation_index >= len(self.ninja_attack_frame_storage):
            self.animation_index = 0
        self.image = self.frame_storage[int(self.animation_index)]
        if self.freezing and self.run == 0:
            self.ninja_speed *= (1 - database.spell_storage["freezing"][3])
            self.run += 1
        elif not self.freezing and self.run > 0:
            self.ninja_speed /= (1 - database.spell_storage["freezing"][3])
            self.run = 0
            self.freezing = False

    def ninja_attack(self):
        self.ninja_attacking = True
        if self.ninja_attacking:
            self.ninja_coordinate_x = self.ninja_prev_coor
            self.animation_attack_index += 0.2
            if self.animation_attack_index >= len(self.ninja_attack_frame_storage):
                self.animation_attack_index = 0
                self.ninja_attacking = False
            self.image = self.ninja_attack_frame_storage[int(self.animation_attack_index)]

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


class GameStickOfWar:
    def __init__(self):
        self.reset_func()

        self.ninja_choice = ["naruto", "naruto", "naruto", "kakashi", "kakashi", "sasuke"]
        # Scrolling Background
        self.background_image = pygame.image.load('War of stick/Picture/utils/map.jpg')
        self.left_rect_castle = pygame.Rect(self.bg_x, 90, 170, 390)
        self.right_rect_castle = pygame.Rect(self.bg_x + self.background_image.get_width() - 100, 90, 170,
                                             390)  # distance between troop and castle during time

        # spell equipment
        self.box = pygame.image.load('War of stick/Picture/utils/box.png')
        self.box_surf = pygame.transform.scale(self.box, (600, 80))
        self.box_rect = self.box_surf.get_rect(center=(300, 550))

        # healing
        self.healing_spell = pygame.image.load('War of stick/Picture/spell/healing_spell.png')
        self.healing_spell_surf = pygame.transform.scale(self.healing_spell, (70, 70))
        self.healing_spell_rect = self.healing_spell_surf.get_rect(center=self.healing_initial_position)
        # healing dim
        self.healing_dim = pygame.image.load('War of stick/Picture/spell/healing_dim_spell.png')
        self.healing_dim_surf = pygame.transform.scale(self.healing_dim, (70, 70))
        self.healing_dim_rect = self.healing_dim_surf.get_rect(center=self.healing_initial_position)
        # healing red
        self.healing_red = pygame.image.load('War of stick/Picture/spell/healing_red.png')
        self.healing_red_surf = pygame.transform.scale(self.healing_red, (70, 70))
        self.healing_red_rect = self.healing_red_surf.get_rect(center=self.healing_initial_position)
        # healing animation
        self.healing_spell_animation = pygame.image.load('War of stick/Picture/spell/healing_animation.png')
        self.healing_spell_animation.set_alpha(128)
        self.healing_spell_animation_surf = pygame.transform.scale(self.healing_spell_animation, (100, 100))

        # freeze
        self.freeze_spell = pygame.image.load('War of stick/Picture/spell/freeze_spell.png')
        self.freeze_spell_surf = pygame.transform.scale(self.freeze_spell, (70, 70))
        self.freeze_spell_rect = self.freeze_spell_surf.get_rect(center=self.freeze_initial_position)
        # freeze dim
        self.freeze_dim = pygame.image.load('War of stick/Picture/spell/freeze_dim_spell.png')
        self.freeze_dim_surf = pygame.transform.scale(self.freeze_dim, (70, 70))
        self.freeze_dim_rect = self.freeze_dim_surf.get_rect(center=self.freeze_initial_position)
        # freeze red
        self.freeze_red = pygame.image.load('War of stick/Picture/spell/freeze_red.png')
        self.freeze_red_surf = pygame.transform.scale(self.freeze_red, (70, 70))
        self.freeze_red_rect = self.freeze_red_surf.get_rect(center=self.freeze_initial_position)
        # rage animation
        self.freeze_spell_animation = pygame.image.load('War of stick/Picture/spell/freeze_animation.png')
        self.freeze_spell_animation.set_alpha(128)
        self.freeze_spell_animation_surf = pygame.transform.scale(self.freeze_spell_animation, (80, 80))

        # rage
        self.rage_spell = pygame.image.load('War of stick/Picture/spell/rage_spell.png')
        self.rage_spell_surf = pygame.transform.scale(self.rage_spell, (70, 70))
        self.rage_spell_rect = self.rage_spell_surf.get_rect(center=self.rage_initial_position)
        # rage dim
        self.rage_dim = pygame.image.load('War of stick/Picture/spell/rage_dim_spell.png')
        self.rage_dim_surf = pygame.transform.scale(self.rage_dim, (70, 70))
        self.rage_dim_rect = self.rage_dim_surf.get_rect(center=self.rage_initial_position)
        # rage red
        self.rage_red = pygame.image.load('War of stick/Picture/spell/rage_red.png')
        self.rage_red_surf = pygame.transform.scale(self.rage_red, (70, 70))
        self.rage_red_rect = self.rage_red_surf.get_rect(center=self.rage_initial_position)
        # rage animation
        self.rage_spell_animation = pygame.image.load('War of stick/Picture/spell/rage_animation.png')
        self.rage_spell_animation.set_alpha(128)
        self.rage_spell_animation_surf = pygame.transform.scale(self.rage_spell_animation, (90, 100))
        # rage special for giant
        self.rage_spell_animation_giant_surf = pygame.transform.scale(self.rage_spell_animation, (90, 150))

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

        # Troop Assets
        self.pic_troop = pygame.image.load('War of stick/Picture/utils/troop_pic.png').convert_alpha()
        self.pic_troop_surf = pygame.transform.scale(self.pic_troop, (80, 80))
        self.pic_troop_rect = self.pic_troop_surf.get_rect(center=(866, 100))
        self.num_troop_font = pygame.font.Font(None, 30)
        self.num_troop_surf = self.num_troop_font.render(str(self.num_troops), True, 'Black')
        self.num_troop_rect = self.num_troop_surf.get_rect(center=(905, 80))

        # timer asset
        self.timer = pygame.image.load('War of stick/Picture/store/timer.png')
        self.timer_surf = pygame.transform.scale(self.timer, (30, 30))
        self.timer_rect = self.timer_surf.get_rect(center=(863, 50))

        # spell price
        self.price_box = pygame.image.load('War of stick/Picture/utils/price_box.png')
        self.price_box_surf = pygame.transform.scale(self.price_box, (50, 20))
        self.price_box_heal_rect = self.price_box_surf.get_rect(center=(35, 510))
        self.price_box_freeze_rect = self.price_box_surf.get_rect(center=(105, 510))
        self.price_box_rage_rect = self.price_box_surf.get_rect(center=(175, 510))

        self.healing_price_font = pygame.font.Font(None, 20)
        self.healing_price_surf = self.healing_price_font.render(str(self.healing_price), True, 'Black')
        self.healing_price_rect = self.healing_price_surf.get_rect(center=(35, 510))

        self.freeze_price_font = pygame.font.Font(None, 20)
        self.freeze_price_surf = self.freeze_price_font.render(str(self.freeze_price), True, 'Black')
        self.freeze_price_rect = self.freeze_price_surf.get_rect(center=(105, 510))

        self.rage_price_font = pygame.font.Font(None, 20)
        self.rage_price_surf = self.rage_price_font.render(str(self.rage_price), True, 'Black')
        self.rage_price_rect = self.rage_price_surf.get_rect(center=(175, 510))

        self.lock = pygame.image.load('War of stick/Picture/utils/lock.png')
        self.lock_surf = pygame.transform.scale(self.lock, (50, 50))

        self.wood_plank = pygame.image.load('Plant vs Stick/Picture/utils/wood.png').convert()
        self.wood_plank_surface = pygame.transform.scale(self.wood_plank, (100, 50))
        self.wood_plank_rect = self.wood_plank_surface.get_rect(center=(500, 500))

        self.level_text = pygame.font.Font(None, 50)
        self.level_text_surf = self.level_text.render("Level", True, (255, 255, 255))
        self.level_text_rect = self.level_text_surf.get_rect(center=(500, 500))

        self.one_star = pygame.image.load('War of stick/Picture/utils/one_star.png')
        self.one_star_surf = pygame.transform.scale(self.one_star, (180, 80))

        self.two_star = pygame.image.load('War of stick/Picture/utils/two_star.png')
        self.two_star_surf = pygame.transform.scale(self.two_star, (180, 80))

        self.three_star = pygame.image.load('War of stick/Picture/utils/three_star.png')
        self.three_star_surf = pygame.transform.scale(self.three_star, (180, 80))

        self.no_star = pygame.image.load('War of stick/Picture/utils/no_star.png')
        self.no_star_surf = pygame.transform.scale(self.no_star, (180, 80))

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
        self.warrior_lock = pygame.image.load('War of stick/Picture/button_lock/warrior_lock.png')
        self.warrior_button = TroopButton(self, self.warrior_button_image, self.warrior_button_dim_image, self.warrior_button_flash,
                                          self.warrior_lock,
                                          (100, 100), (100, 70), f'{database.warrior_gold}n{database.warrior_diamond}', 3000,
                                          database.warrior_gold, database.warrior_diamond)

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
        self.archer_lock = pygame.image.load('War of stick/Picture/button_lock/archer_lock.png')
        self.archer_button = TroopButton(self, self.archer_button_image, self.archer_button_dim_image, self.archer_button_flash,
                                         self.archer_lock,
                                         (100, 100), (200, 70), f'{database.archer_gold}n{database.archer_diamond}', 3000,
                                         database.archer_gold, database.archer_diamond)

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
        self.wizard_lock = pygame.image.load('War of stick/Picture/button_lock/wizard_lock.png')
        self.wizard_button = TroopButton(self, self.wizard_button_image, self.wizard_button_dim_image, self.wizard_button_flash,
                                         self.wizard_lock,
                                         (100, 100), (300, 70), f'{database.wizard_gold}n{database.wizard_diamond}', 3000,
                                         database.wizard_gold, database.wizard_diamond)
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
        self.sparta_lock = pygame.image.load('War of stick/Picture/button_lock/sparta_lock.png')
        self.sparta_button = TroopButton(self, self.sparta_button_image, self.sparta_button_dim_image, self.sparta_button_flash,
                                         self.sparta_lock,
                                         (100, 100), (400, 70), f'{database.sparta_gold}n{database.sparta_diamond}', 3000,
                                         database.sparta_gold, database.sparta_diamond)

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
        self.giant_lock = pygame.image.load('War of stick/Picture/button_lock/giant_lock.png')
        self.giant_button = TroopButton(self, self.giant_button_image, self.giant_button_dim_image, self.giant_button_flash,
                                        self.giant_lock,
                                        (100, 100),
                                        (500, 70), f'{database.giant_gold}n{database.giant_diamond}', 3000, database.giant_gold,
                                        database.giant_diamond)

        self.enemy_one_normal = [pygame.image.load('Plant vs Stick/Picture/enemy_one/enemy_one_1.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_one/enemy_one_2.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_one/enemy_one_3.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_one/enemy_one_4.png').convert_alpha()]
        self.enemy_one_attack = [pygame.image.load('Plant vs Stick/Picture/enemy_one/enemy_one_attack_1.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_one/enemy_one_attack_2.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_one/enemy_one_attack_3.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_one/enemy_one_attack_4.png').convert_alpha()]
        self.enemy_one_frame_storage = [pygame.transform.scale(frame, (110, 135)) for frame in self.enemy_one_normal]
        self.enemy_one_attack_frame_storage = [pygame.transform.scale(frame, (110, 135)) for frame in self.enemy_one_attack]

        self.enemy_two_normal = [pygame.image.load('Plant vs Stick/Picture/enemy_two/enemy_two_1.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_two/enemy_two_2.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_two/enemy_two_3.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_two/enemy_two_4.png').convert_alpha()]
        self.enemy_two_attack = [pygame.image.load('Plant vs Stick/Picture/enemy_two/enemy_two_attack_1.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_two/enemy_two_attack_2.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_two/enemy_two_attack_3.png').convert_alpha(),
                                 pygame.image.load('Plant vs Stick/Picture/enemy_two/enemy_two_attack_4.png').convert_alpha(), ]
        self.enemy_two_frame_storage = [pygame.transform.scale(frame, (100, 95)) for frame in self.enemy_two_normal]
        self.enemy_two_attack_frame_storage = [pygame.transform.scale(frame, (100, 95)) for frame in self.enemy_two_attack]

        self.enemy_three_normal = [pygame.image.load('Plant vs Stick/Picture/enemy_three/enemy_three_1.png').convert_alpha(),
                                   pygame.image.load('Plant vs Stick/Picture/enemy_three/enemy_three_2.png').convert_alpha(),
                                   pygame.image.load('Plant vs Stick/Picture/enemy_three/enemy_three_3.png').convert_alpha(),
                                   pygame.image.load('Plant vs Stick/Picture/enemy_three/enemy_three_4.png').convert_alpha(),
                                   pygame.image.load('Plant vs Stick/Picture/enemy_three/enemy_three_5.png').convert_alpha(), ]
        self.enemy_three_attack = [pygame.image.load('Plant vs Stick/Picture/enemy_three/enemy_three_attack_1.png').convert_alpha(),
                                   pygame.image.load('Plant vs Stick/Picture/enemy_three/enemy_three_attack_2.png').convert_alpha(),
                                   pygame.image.load('Plant vs Stick/Picture/enemy_three/enemy_three_attack_3.png').convert_alpha(),
                                   pygame.image.load('Plant vs Stick/Picture/enemy_three/enemy_three_attack_4.png').convert_alpha(),
                                   pygame.image.load('Plant vs Stick/Picture/enemy_three/enemy_three_attack_5.png').convert_alpha()]
        self.enemy_three_frame_storage = [pygame.transform.scale(frame, (100, 95)) for frame in self.enemy_three_normal]
        self.enemy_three_attack_frame_storage = [pygame.transform.scale(frame, (100, 95)) for frame in self.enemy_three_attack]

    def reset_func(self):
        # pygame.init()
        # pygame.font.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tower Defend')  # title name
        self.screen = pygame.display.set_mode((1000, 600))
        self.bg_x = 0
        self.scroll_speed = 10
        self.num_gold = 100000
        self.num_diamond = 100000
        self.gold_time = pygame.time.get_ticks()
        self.diamond_time = pygame.time.get_ticks()
        self.gold_interval = 110
        self.diamond_interval = 110
        self.troop_on_court = []
        self.enemy_on_court = []
        self.health_bar_user = HealthBar(database.castle_storage["default_castle"][3], database.castle_storage["default_castle"][3],
                                         (620, 530), 200, 20, (0, 255, 0))  # health bar
        self.health_bar_enemy = HealthBar(5000 * (database.lvl_choose * 2), 5000 * (database.lvl_choose * 2), (620, 560), 200, 20,
                                          (255, 0, 0))
        self.healing_initial_position = (35, 550)
        self.freeze_initial_position = (105, 550)
        self.rage_initial_position = (175, 550)
        self.game_over = False
        self.winner = None
        self.chosen_spell = None
        self.spell_animation = False
        self.time_string = None
        self.num_troops = 0
        self.max_troop = int(99 * (database.lvl_choose / 3))
        self.healing_press = False
        self.freeze_press = False
        self.rage_press = False
        self.healing_press_time = 0
        self.freeze_press_time = 0
        self.rage_press_time = 0
        self.healing_price = 500
        self.freeze_price = 500
        self.rage_price = 500

        self.go_level_py = False

        # set up Ninja timer
        self.ninja_timer = pygame.USEREVENT + 1
        if database.lvl_choose <= 1:
            self.spawn_time = 11000
        else:
            self.spawn_time = int(6000 / (database.lvl_choose / 3))
        pygame.time.set_timer(self.ninja_timer, self.spawn_time)
        self.freeze_timer = pygame.USEREVENT + 2
        self.rage_timer = pygame.USEREVENT + 3
        self.healing = False
        self.heal_run = 0

        self.start_game_time = pygame.time.get_ticks()
        self.end_game_time = 0
        self.played_time = 0

    def event_handling(self):
        def clicked_troop(gold_cost, diamond_cost, button_name, frame_storage, attack_frame_storage, health, attack_damage,
                          speed, troop_width, troop_height, troop_name, troop_size):
            mouse_pos = pygame.mouse.get_pos()  # Check if the left mouse button was clicked and handle accordingly

            if self.num_troops <= self.max_troop:
                if button_name.is_clicked(mouse_pos):
                    if self.num_gold >= gold_cost and self.num_diamond >= diamond_cost:
                        self.num_gold -= gold_cost
                        self.num_diamond -= diamond_cost
                        new_troop = Troop(self, frame_storage, attack_frame_storage, health, attack_damage, speed,
                                          troop_width,
                                          troop_height, troop_name, troop_size)
                        self.troop_on_court.append(new_troop)
                    self.num_troops += troop_size
            else:
                print('have reach the max troop')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.update_user()
                database.push_data()
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.wood_plank_rect.collidepoint(pygame.mouse.get_pos()):
                    self.game_music.stop()
                    self.go_level_py = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check if left mouse button is pressed
                    clicked_troop(database.warrior_gold, database.warrior_diamond, self.warrior_button, self.warrior_frame_storage,
                                  self.warrior_attack_frame_storage,
                                  database.troop_storage["warrior"][3],
                                  database.troop_storage["warrior"][4], database.troop_storage["warrior"][5], 75, 100, 'Warrior', 1)
                    clicked_troop(database.archer_gold, database.archer_diamond, self.archer_button, self.archer_frame_storage,
                                  self.archer_attack_frame_storage,
                                  database.troop_storage["archer"][3], database.troop_storage["archer"][4],
                                  database.troop_storage["archer"][5], 75, 100, 'Archer', 2)
                    clicked_troop(database.wizard_gold, database.wizard_diamond, self.wizard_button, self.wizard_frame_storage,
                                  self.wizard_attack_frame_storage,
                                  database.troop_storage["wizard"][3], database.troop_storage["wizard"][4],
                                  database.troop_storage["wizard"][5], 75, 100, 'Wizard', 4)
                    clicked_troop(database.sparta_gold, database.sparta_diamond, self.sparta_button, self.sparta_frame_storage,
                                  self.sparta_attack_frame_storage,
                                  database.troop_storage["sparta"][3], database.troop_storage["sparta"][4],
                                  database.troop_storage["sparta"][5], 75, 100, 'Sparta', 6)
                    clicked_troop(database.giant_gold, database.giant_diamond, self.giant_button, self.giant_frame_storage,
                                  self.giant_attack_frame_storage,
                                  database.troop_storage["giant"][3], database.troop_storage["giant"][4],
                                  database.troop_storage["giant"][5], 30, 200, 'Giant', 15)

            if event.type == self.ninja_timer:
                if len(self.enemy_on_court) <= 20:
                    new_ninja = None
                    self.ninja_chosen = choice(self.ninja_choice)
                    if self.ninja_chosen == "naruto":
                        new_ninja = Ninja(self.ninja_chosen, self.enemy_one_frame_storage, self.enemy_one_attack_frame_storage,
                                          50 * (database.lvl_choose),
                                          0.9, 1 + (database.lvl_choose / 5),
                                          self.background_image.get_width())
                    elif self.ninja_chosen == "sasuke":
                        new_ninja = Ninja(self.ninja_chosen, self.enemy_two_frame_storage, self.enemy_two_attack_frame_storage,
                                          60 * (database.lvl_choose),
                                          1, 2 + (database.lvl_choose / 5),
                                          self.background_image.get_width())
                    elif self.ninja_chosen == "kakashi":
                        new_ninja = Ninja(self.ninja_chosen, self.enemy_three_frame_storage, self.enemy_three_attack_frame_storage,
                                          70 * (database.lvl_choose), 1.5, 3 + (database.lvl_choose / 5),
                                          self.background_image.get_width())
                    self.enemy_on_court.append(new_ninja)
                else:
                    print('wont be more than 20')

            if database.spell_storage['healing'][0] == True:
                if self.chosen_spell is None and event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.healing_press:
                        if self.healing_spell_rect.collidepoint(event.pos):
                            self.chosen_spell = 'healing'
            if database.spell_storage['rage'][0] == True:
                if self.chosen_spell is None and event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.rage_press:
                        if self.rage_spell_rect.collidepoint(event.pos):
                            self.chosen_spell = 'rage'
            if database.spell_storage['freeze'][0] == True:
                if self.chosen_spell is None and event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.freeze_press:
                        if self.freeze_spell_rect.collidepoint(event.pos):
                            self.chosen_spell = 'freeze'

            if event.type == pygame.MOUSEBUTTONDOWN and self.chosen_spell is not None:
                # can add check condition can release spell or not
                if self.chosen_spell == 'healing':
                    self.healing_press = True
                    if self.num_diamond >= 500:
                        self.num_diamond -= 500
                        self.healing = True
                        for troop in self.troop_on_court:
                            troop.health += database.spell_storage["healing"][3]
                if self.chosen_spell == 'rage':
                    self.rage_press = True
                    if self.num_diamond >= 500:
                        self.num_diamond -= 500
                        for troop in self.troop_on_court:
                            troop.raging = True
                if self.chosen_spell == 'freeze':
                    self.freeze_press = True
                    if self.num_diamond >= 500:
                        self.num_diamond -= 500
                        for ninja in self.enemy_on_court:
                            ninja.freezing = True
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
            self.num_gold += (2 + database.castle_storage["default_castle"][4])

            self.gold_time = current_time

        if current_time - self.diamond_time >= self.diamond_interval:
            self.num_diamond += (1 + database.castle_storage["default_castle"][4])
            self.diamond_time = current_time

        # troop attack tower
        for troop in self.troop_on_court:
            if troop.troop_name == "Archer" or troop.troop_name == "Wizard":
                # troop attack ninja
                for ninja in self.enemy_on_court:
                    if self.far_range_collide(troop, ninja):
                        troop.attack(self.bg_x)
                        troop.move_bullet(self.bg_x)
                        if ninja.ninja_health <= 0:
                            self.enemy_on_court.remove(ninja)
                if self.check_far_collision(troop, self.right_rect_castle):
                    troop.attack(self.bg_x)
                    troop.move_bullet(self.bg_x)
                    for bullet in troop.bullet_on_court:
                        if bullet[1].x + 930 >= self.right_rect_castle.x:
                            self.health_bar_enemy.update_health(troop.attack_damage)
                            troop.bullet_on_court.remove(bullet)
                            print(bullet[1].x)
                            print(self.right_rect_castle.x)
                            print(troop.attack_damage)
                            print(self.health_bar_enemy.current_health)
                else:
                    troop.move_bullet(self.bg_x)
                    break
            else:
                if self.check_collision(troop, self.right_rect_castle):
                    self.health_bar_enemy.update_health(troop.attack_damage)  # Update castle health
                    troop.attack(self.bg_x)
                    troop.move_bullet(self.bg_x)
                else:
                    for ninja in self.enemy_on_court:
                        if self.both_collide(troop, ninja):
                            troop.attack(self.bg_x)
                            troop.move_bullet(self.bg_x)
                            ninja.ninja_take_damage(troop.attack_damage)
                            if ninja.ninja_health <= 0:
                                self.enemy_on_court.remove(ninja)
                            break

        for ninja in self.enemy_on_court:
            # ninja attack tower
            if self.ninja_collision(ninja, self.left_rect_castle):
                self.health_bar_user.update_health(ninja.attack)  # Update castle health
                ninja.ninja_attack()
            else:
                # ninja attack troop
                for troop in self.troop_on_court:
                    if self.both_collide(troop, ninja):
                        ninja.ninja_attack()
                        troop.take_damage(ninja.attack)
                        if troop.health <= 0:
                            self.troop_on_court.remove(troop)
                            self.num_troops -= troop.troop_size
                        break

    @staticmethod
    def check_collision(troop, rect):
        troop_rect = pygame.Rect(troop.coordinate_x, 0, troop.troop_width, troop.troop_height)  # for right castle
        return troop_rect.colliderect(rect)

    @staticmethod
    def check_far_collision(troop, rect):
        troop_rect = pygame.Rect(troop.coordinate_x, 0, troop.troop_width + 400, troop.troop_height)  # for right castle
        return troop_rect.colliderect(rect)

    @staticmethod
    def both_collide(troop, ninja):
        troop_rect = pygame.Rect(troop.coordinate_x, 0, troop.troop_width, troop.troop_height)
        ninja_rect = pygame.Rect(ninja.ninja_coordinate_x, 0, 75, 100)  # for attack each other
        return troop_rect.colliderect(ninja_rect)

    @staticmethod
    def far_range_collide(troop, ninja):
        troop_rect = pygame.Rect(troop.coordinate_x, 0, troop.troop_width + 400, troop.troop_height)
        ninja_rect = pygame.Rect(ninja.ninja_coordinate_x, 0, 75, 100)  # for attack each other
        return troop_rect.colliderect(ninja_rect)

    @staticmethod
    def ninja_collision(ninja, rect):
        ninja_rect = pygame.Rect(ninja.ninja_coordinate_x, 0, 75, 100)  # for left castle
        return ninja_rect.colliderect(rect)

    def check_game_over(self):
        if self.health_bar_user.current_health <= 0:
            self.game_over = True
            self.winner = "Enemy"
        elif self.health_bar_enemy.current_health <= 0:
            self.game_over = True
            self.winner = "User"
            if database.lvl_choose == database.stage_level:
                database.stage_level += 1

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

        if not self.game_over:
            self.end_game_time = pygame.time.get_ticks()  # Get the current time
            self.played_time = self.end_game_time - self.start_game_time
            self.elapsed_time_seconds = (self.played_time) / 1000  # Convert milliseconds to seconds
            self.minutes = int(self.elapsed_time_seconds // 60)
            self.seconds = int(self.elapsed_time_seconds % 60)
            self.time_string = f"{self.minutes:02}:{self.seconds:02}"
            timer_surface = pygame.font.Font(None, 30).render(self.time_string, True, 'black')
            timer_rect = timer_surface.get_rect(center=(908, 50))
            self.screen.blit(timer_surface, timer_rect)

        self.health_bar_user.draw(self.screen)
        self.health_bar_enemy.draw(self.screen)

        # box for spell
        self.screen.blit(self.box_surf, self.box_rect)
        # rage
        if database.spell_storage['rage'][0] == True:
            if self.num_diamond >= self.rage_price:
                self.screen.blit(self.rage_spell_surf, self.rage_spell_rect)
            else:
                self.screen.blit(self.rage_red_surf, self.rage_red_rect)
        elif database.spell_storage['rage'][0] == False:
            self.lock_rect = self.lock_surf.get_rect(center=(self.rage_initial_position))
            self.screen.blit(self.rage_dim_surf, self.rage_dim_rect)
            self.screen.blit(self.lock_surf, self.lock_rect)

        # healing
        if database.spell_storage['healing'][0] == True:
            if self.num_diamond >= self.healing_price:
                self.screen.blit(self.healing_spell_surf, self.healing_spell_rect)
            else:
                self.screen.blit(self.healing_red_surf, self.healing_red_rect)
        elif database.spell_storage['healing'][0] == False:
            self.lock_rect = self.lock_surf.get_rect(center=(self.healing_initial_position))
            self.screen.blit(self.healing_dim_surf, self.healing_dim_rect)
            self.screen.blit(self.lock_surf, self.lock_rect)

        # freeze
        if database.spell_storage['freeze'][0] == True:
            if self.num_diamond >= self.freeze_price:
                self.screen.blit(self.freeze_spell_surf, self.freeze_spell_rect)
            else:
                self.screen.blit(self.freeze_red_surf, self.freeze_red_rect)
        elif database.spell_storage['freeze'][0] == False:
            self.lock_rect = self.lock_surf.get_rect(center=(self.freeze_initial_position))
            self.screen.blit(self.freeze_dim_surf, self.freeze_dim_rect)
            self.screen.blit(self.lock_surf, self.lock_rect)

        if self.healing_press:
            self.screen.blit(self.healing_dim_surf, self.healing_dim_rect)
            self.healing_press_time += 1.75
            if self.healing_press_time >= 300:
                self.healing_press = False
                self.healing_press_time = 0

        if self.freeze_press:
            self.screen.blit(self.freeze_dim_surf, self.freeze_dim_rect)
            self.freeze_press_time += 1.75
            if self.freeze_press_time >= 300:
                self.freeze_press = False
                self.freeze_press_time = 0

        if self.rage_press:
            self.screen.blit(self.rage_dim_surf, self.rage_dim_rect)
            self.rage_press_time += 1.75
            if self.rage_press_time >= 300:
                self.rage_press = False
                self.rage_press_time = 0

        # gold icon
        self.screen.blit(self.pic_gold_surf, self.pic_gold_rect)
        self.num_gold_surf = self.num_gold_font.render(str(self.num_gold), True, 'Black')
        self.screen.blit(self.num_gold_surf, self.num_gold_rect)

        # diamond icon
        self.screen.blit(self.pic_diamond_surf, self.pic_diamond_rect)
        self.num_diamond_surf = self.num_diamond_font.render(str(self.num_diamond), True, 'Black')
        self.screen.blit(self.num_diamond_surf, self.num_diamond_rect)

        # troop icon
        self.screen.blit(self.pic_troop_surf, self.pic_troop_rect)
        self.num_troop_surf = self.num_troop_font.render(f"{self.num_troops} / {self.max_troop}", True, 'Black')
        self.screen.blit(self.num_troop_surf, self.num_troop_rect)

        # timer icon
        self.screen.blit(self.timer_surf, self.timer_rect)

        # spell price
        self.screen.blit(self.price_box_surf, self.price_box_heal_rect)
        self.screen.blit(self.price_box_surf, self.price_box_freeze_rect)
        self.screen.blit(self.price_box_surf, self.price_box_rage_rect)

        self.screen.blit(self.healing_price_surf, self.healing_price_rect)
        self.screen.blit(self.freeze_price_surf, self.freeze_price_rect)
        self.screen.blit(self.rage_price_surf, self.rage_price_rect)

        # button draw
        self.warrior_button.draw(self.screen, database.troop_storage["warrior"][2])
        self.archer_button.draw(self.screen, database.troop_storage["archer"][2])
        self.wizard_button.draw(self.screen, database.troop_storage["wizard"][2])
        self.sparta_button.draw(self.screen, database.troop_storage["sparta"][2])
        self.giant_button.draw(self.screen, database.troop_storage["giant"][2])

        self.check_game_over()
        if self.game_over:
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 68)
            if self.winner == "User":
                text = font.render("You've won!", True, (255, 255, 255))
                time = font.render(f'{self.time_string}', True, (255, 255, 255))
                if 0 <= self.played_time <= 120000:
                    prize = font.render(f"You've earn {30 + database.lvl_choose * 15}$", True, (255, 255, 255))
                    prize_rect = prize.get_rect(center=(500, 200))
                    star_rect = self.three_star_surf.get_rect(center=(500, 100))
                    self.screen.blit(prize, prize_rect)
                    self.screen.blit(self.three_star_surf, star_rect)
                elif 120000 <= self.played_time <= 240000:
                    prize = font.render(f"You've earn {30 + database.lvl_choose * 5}$", True, (255, 255, 255))
                    prize_rect = prize.get_rect(center=(500, 200))
                    star_rect = self.three_star_surf.get_rect(center=(500, 100))
                    self.screen.blit(prize, prize_rect)
                    self.screen.blit(self.two_star_surf, star_rect)
                elif self.played_time >= 240000:
                    prize = font.render(F"You've earn {20 + database.lvl_choose * 2}$", True, (255, 255, 255))
                    prize_rect = prize.get_rect(center=(500, 200))
                    star_rect = self.three_star_surf.get_rect(center=(500, 100))
                    self.screen.blit(prize, prize_rect)
                    self.screen.blit(self.one_star_surf, star_rect)
            else:
                text = font.render("You've lost!", True, (255, 255, 255))
                time = font.render(f'{self.time_string}', True, (255, 255, 255))
                prize = font.render(F"You've earn {int(10 + database.lvl_choose * 1.3)}$", True, (255, 255, 255))
                prize_rect = prize.get_rect(center=(500, 200))
                star_rect = self.three_star_surf.get_rect(center=(500, 100))
                self.screen.blit(prize, prize_rect)
                self.screen.blit(self.no_star_surf, star_rect)
            text_rect = text.get_rect(center=(500, 300))
            time_rect = time.get_rect(center=(500, 400))
            self.screen.blit(text, text_rect)
            self.screen.blit(time, time_rect)
            self.screen.blit(self.wood_plank_surface, self.wood_plank_rect)
            self.screen.blit(self.level_text_surf, self.level_text_rect)
            return  # End the game

        for troop in self.troop_on_court:
            if troop.raging:
                if troop.troop_name == 'Giant':
                    self.screen.blit(self.rage_spell_animation_giant_surf, troop.rect)
                else:
                    self.screen.blit(self.rage_spell_animation_surf, troop.rect)
            if self.healing:
                self.screen.blit(self.healing_spell_animation_surf, troop.rect)
                self.heal_run += 1
                if self.heal_run > 30:
                    self.healing = False
                    self.heal_run = 0
            troop.spawn_troop(self.screen, self.bg_x)
            troop.update()
            for bullet in troop.bullet_on_court:
                self.screen.blit(bullet[0], bullet[1])

        for enemy in self.enemy_on_court:
            if enemy.freezing:
                self.screen.blit(self.freeze_spell_animation_surf, enemy.rect)
            enemy.spawn_ninja(self.screen, self.bg_x)
            enemy.update_ninja()

    def run(self):
        self.reset_func()
        self.game_music = pygame.mixer.Sound('War of stick/Music/game_music.mp3')
        self.game_music.set_volume(0.2)
        self.game_music.play(loops=-1)
        while True:
            self.game_start()
            self.event_handling()

            pygame.display.update()  # Update the display
            self.clock.tick(60)  # Limit frame rate to 60 FPS

"""
"""
"""
"""
"""
"""



# pygame.init()
# pygame.font.init()


# others troop * 10
# archer wiazrd(attack damage) after use the formula *5//1
# spell blit percentage
# backpack 人一开始就Blit

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

        # load backpack stick image
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

        # spell card
        self.freeze_card_image_surf = pygame.image.load('War of stick/Picture/spell/freeze_spell.png').convert_alpha()
        self.freeze_card_image_surf = pygame.transform.scale(self.freeze_card_image_surf, (60, 60))

        self.healing_card_image_surf = pygame.image.load('War of stick/Picture/spell/healing_spell.png').convert_alpha()
        self.healing_card_image_surf = pygame.transform.scale(self.healing_card_image_surf, (60, 60))

        self.rage_card_image_surf = pygame.image.load('War of stick/Picture/spell/rage_spell.png').convert_alpha()
        self.rage_card_image_surf = pygame.transform.scale(self.rage_card_image_surf, (60, 60))


class Game_Store:
    def __init__(self):
        # pygame.init()
        # pygame.font.init()
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
        # define the x,y coordiante for the card
        self.x_coords = ([325, 470, 610, 325, 470, 610, 325, 470, 610])
        self.y_coords = ([200, 200, 200, 336, 336, 336, 477, 477, 477])
        # backpack title surface
        self.x_button_coordinate = ([547, 647, 747, 847])
        self.y_button_coordinate = ([218, 218, 218, 218])
        # troop equipped position
        self.x_troop_equipped_position = ([290, 375, 473, 569, 668])
        self.y_troop_equipped_position = ([58, 58, 58, 58, 58])
        self.troop_equipped_list = []
        # spell equipped position
        self.x_spell_equipped_position = ([290, 375, 473])
        self.y_spell_equipped_position = ([130, 130, 130])
        self.spell_equipped_list = []
        self.selected_category = 'Castle'
        self.clicked_image_surf = 'warrior'
        self.clicked_spell_surf = 'freeze'
        self.go_level_py = False
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
        self.store_castle_image_surf = pygame.transform.scale(self.castle_image_surf, (120, 120))

        self.health_image_surf = pygame.image.load('War of stick/Picture/store/health.png').convert_alpha()
        self.health_image_surf = pygame.transform.scale(self.health_image_surf, (20, 20))

        self.mining_image_surf = pygame.image.load('War of stick/Picture/store/pickaxe.png').convert_alpha()
        self.mining_image_surf = pygame.transform.scale(self.mining_image_surf, (30, 30))

        self.damage_image_surf = pygame.image.load('War of stick/Picture/store/damage.png').convert_alpha()
        self.damage_image_surf = pygame.transform.scale(self.damage_image_surf, (25, 25))

        self.freeze_function_image_surf = pygame.image.load('War of stick/Picture/spell/freeze_animation.png').convert_alpha()
        self.freeze_function_image_surf = pygame.transform.scale(self.freeze_function_image_surf, (30, 30))

        self.healing_function_image_surf = pygame.image.load('War of stick/Picture/spell/healing_animation.png').convert_alpha()
        self.healing_function_image_surf = pygame.transform.scale(self.healing_function_image_surf, (30, 30))

        self.rage_function_image_surf = pygame.image.load('War of stick/Picture/spell/rage_animation.png').convert_alpha()
        self.rage_function_image_surf = pygame.transform.scale(self.rage_function_image_surf, (30, 30))

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
        self.back_level_button_surf = pygame.transform.scale(self.back_level_button_surf, (75, 75))
        self.back_level_button_rect = self.back_level_button_surf.get_rect(topleft=(25, 15))

        self.back_level_background_surf = pygame.image.load(
            'War of stick/Picture/Store/back_to_level_background.png').convert_alpha()
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
        self.level_word_rect = self.level_word_surf.get_rect(topleft=(85, 35))

        # money word
        self.money_surf = self.font.render(str(database.money), True, 'White')
        self.money_rect = self.money_surf.get_rect(topright=(900, 5))

        self.castle_word_surf = self.font.render('Castle', True, 'White')
        self.castle_word_rect = self.castle_word_surf.get_rect(center=(545, 220))

        self.troop_word_surf = self.font.render('Troop', True, 'White')
        self.troop_word_rect = self.troop_word_surf.get_rect(center=(645, 220))

        self.spell_word_surf = self.font.render('Spell', True, 'White')
        self.spell_word_rect = self.spell_word_surf.get_rect(center=(745, 220))

        self.others_word_surf = self.font.render('Others', True, 'White')
        self.others_word_rect = self.others_word_surf.get_rect(center=(845, 220))

        self.store_list = [
            {'image': self.store_castle_image_surf, 'name': 'castle', 'button': self.button_background_surf,
             'locked': database.castle_storage['default_castle'][0],
             'money': self.money_image_surf, 'price': 200},
            {'image': self.cards.warrior_card_surf, 'name': 'warrior', 'button': self.button_background_surf,
             'locked': database.troop_storage['warrior'][0],
             'money': self.money_image_surf, 'price': 250},
            {'image': self.cards.archer_card_surf, 'name': 'archer', 'button': self.button_background_surf,
             'locked': database.troop_storage['archer'][0],
             'money': self.money_image_surf, 'price': 200},
            {'image': self.cards.sparta_card_surf, 'name': 'sparta', 'button': self.button_background_surf,
             'locked': database.troop_storage['sparta'][0],
             'money': self.money_image_surf, 'price': 350},
            {'image': self.cards.wizard_card_surf, 'name': 'wizard', 'button': self.button_background_surf,
             'locked': database.troop_storage['wizard'][0],
             'money': self.money_image_surf, 'price': 450},
            {'image': self.cards.giant_card_surf, 'name': 'giant', 'button': self.button_background_surf,
             'locked': database.troop_storage['giant'][0],
             'money': self.money_image_surf, 'price': 550},
            {'image': self.cards.freeze_card_image_surf, 'name': 'freeze', 'button': self.button_background_surf,
             'locked': database.spell_storage['freeze'][0],
             'money': self.money_image_surf, 'price': 200},
            {'image': self.cards.healing_card_image_surf, 'name': 'healing', 'button': self.button_background_surf,
             'locked': database.spell_storage['healing'][0],
             'money': self.money_image_surf, 'price': 200},
            {'image': self.cards.rage_card_image_surf, 'name': 'rage', 'button': self.button_background_surf,
             'locked': database.spell_storage['rage'][0],
             'money': self.money_image_surf, 'price': 200},
        ]

        self.backpack_troop_list = [
            {
                'name': 'warrior',
                'image': self.cards.warrior_image_surf,
                'button': self.button_background_surf,
                'locked': database.troop_storage['warrior'][0],
                'equip': database.troop_storage['warrior'][2],
                'money': self.money_image_surf,
                'upgrades price': database.troop_storage['warrior'][6],
                'level': database.troop_storage['warrior'][1],
                'health icon': self.health_image_surf,
                'damage icon': self.damage_image_surf,
                'gold icon': self.gold_image_surf_surf,
                'diamond icon': self.diamond_image_surf_surf,
                'upgrades button': self.upgrades_button_surf,
                'health': (database.troop_storage['warrior'][3] * 10),
                'attack damage': (database.troop_storage['warrior'][4] * 10),
                'equip button': self.equip_button_surf,
                'unequip button': self.unequip_button_surf
            },
            {
                'name': 'archer',
                'image': self.cards.archer_image_surf,
                'button': self.button_background_surf,
                'locked': database.troop_storage['archer'][0],
                'equip': database.troop_storage['archer'][2],
                'money': self.money_image_surf,
                'upgrades price': database.troop_storage['archer'][6],
                'level': database.troop_storage['archer'][1],
                'health icon': self.health_image_surf,
                'damage icon': self.damage_image_surf,
                'gold icon': self.gold_image_surf_surf,
                'diamond icon': self.diamond_image_surf_surf,
                'upgrades button': self.upgrades_button_surf,
                'health': (database.troop_storage['archer'][3] * 10),
                'attack damage': (database.troop_storage['archer'][4] * 2),
                'equip button': self.equip_button_surf,
                'unequip button': self.unequip_button_surf
            },
            {
                'name': 'sparta',
                'image': self.cards.sparta_image_surf,
                'button': self.button_background_surf,
                'locked': database.troop_storage['sparta'][0],
                'equip': database.troop_storage['sparta'][2],
                'money': self.money_image_surf,
                'upgrades price': database.troop_storage['sparta'][6],
                'level': database.troop_storage['sparta'][1],
                'health icon': self.health_image_surf,
                'damage icon': self.damage_image_surf,
                'gold icon': self.gold_image_surf_surf,
                'diamond icon': self.diamond_image_surf_surf,
                'upgrades button': self.upgrades_button_surf,
                'health': (database.troop_storage['sparta'][3] * 10),
                'attack damage': (database.troop_storage['sparta'][4] * 10),
                'equip button': self.equip_button_surf,
                'unequip button': self.unequip_button_surf
            },
            {
                'name': 'wizard',
                'image': self.cards.wizard_image_surf,
                'button': self.button_background_surf,
                'locked': database.troop_storage['wizard'][0],
                'equip': database.troop_storage['wizard'][2],
                'money': self.money_image_surf,
                'upgrades price': database.troop_storage['wizard'][6],
                'level': database.troop_storage['wizard'][1],
                'health icon': self.health_image_surf,
                'damage icon': self.damage_image_surf,
                'gold icon': self.gold_image_surf_surf,
                'diamond icon': self.diamond_image_surf_surf,
                'upgrades button': self.upgrades_button_surf,
                'health': (database.troop_storage['wizard'][3] * 10),
                'attack damage': (database.troop_storage['wizard'][4] * 2),
                'equip button': self.equip_button_surf,
                'unequip button': self.unequip_button_surf
            },
            {
                'name': 'giant',
                'image': self.cards.giant_image_surf,
                'button': self.button_background_surf,
                'locked': database.troop_storage['giant'][0],
                'equip': database.troop_storage['giant'][2],
                'money': self.money_image_surf,
                'upgrades price': database.troop_storage['giant'][6],
                'level': database.troop_storage['giant'][1],
                'health icon': self.health_image_surf,
                'damage icon': self.damage_image_surf,
                'gold icon': self.gold_image_surf_surf,
                'diamond icon': self.diamond_image_surf_surf,
                'upgrades button': self.upgrades_button_surf,
                'health': (database.troop_storage['giant'][3] * 10),
                'attack damage': (database.troop_storage['warrior'][4] * 10),
                'equip button': self.equip_button_surf,
                'unequip button': self.unequip_button_surf
            }
        ]
        self.spell_list = [
            {
                'name': 'freeze',
                'image': self.cards.freeze_card_image_surf,
                'button': self.button_background_surf,
                'locked': database.spell_storage['freeze'][0],
                'equip': database.spell_storage['freeze'][2],
                'level': database.spell_storage['freeze'][1],
                'money': self.money_image_surf,
                'diamond icon': self.diamond_image_surf_surf,
                'upgrades price': database.spell_storage['freeze'][4],
                'upgrades button': self.upgrades_button_surf,
                'freeze icon': self.freeze_function_image_surf,
                'spell function': int(database.spell_storage['freeze'][3] * 100),
                'equip button': self.equip_button_surf,
                'unequip button': self.unequip_button_surf
            },
            {
                'name': 'healing',
                'image': self.cards.healing_card_image_surf,
                'button': self.button_background_surf,
                'locked': database.spell_storage['healing'][0],
                'equip': database.spell_storage['healing'][2],
                'level': database.spell_storage['healing'][1],
                'money': self.money_image_surf,
                'diamond icon': self.diamond_image_surf_surf,
                'upgrades price': database.spell_storage['healing'][4],
                'upgrades button': self.upgrades_button_surf,
                'healing icon': self.healing_function_image_surf,
                'healing function': int(database.spell_storage['healing'][3]),
                'equip button': self.equip_button_surf,
                'unequip button': self.unequip_button_surf
            },
            {
                'name': 'rage',
                'image': self.cards.rage_card_image_surf,
                'button': self.button_background_surf,
                'locked': database.spell_storage['rage'][0],
                'equip': database.spell_storage['rage'][2],
                'level': database.spell_storage['rage'][1],
                'money': self.money_image_surf,
                'diamond icon': self.diamond_image_surf_surf,
                'upgrades price': database.spell_storage['rage'][4],
                'upgrades button': self.upgrades_button_surf,
                'rage icon': self.rage_function_image_surf,
                'spell function': int(database.spell_storage['rage'][3] * 100),
                'equip button': self.equip_button_surf,
                'unequip button': self.unequip_button_surf
            }
        ]

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
                'freeze': (558, 280),
                'healing': (695, 280),
                'rage': (830, 280)
            }
        ]

        self.spell_msg_position = [
            {
                'freeze': (558, 320),
                'healing': (695, 320),
                'rage': (830, 320)
            }
        ]
        self.castle_detail = [{
            'image': self.castle_image_surf,
            'name': 'Castle',
            'health icon': self.health_image_surf,
            'health': database.castle_storage['default_castle'][3],
            'health level': database.castle_storage['default_castle'][1],
            'health price': database.castle_storage['default_castle'][5],
            'mining icon': self.mining_image_surf,
            'mining speed': database.castle_storage['default_castle'][4],
            'mining speed level': database.castle_storage['default_castle'][2],
            'mining speed price': database.castle_storage['default_castle'][6],
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
                database.update_user()
                database.push_data()
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
                        if item['locked'] == False:
                            button_background_rect = item['button'].get_rect(
                                center=(self.x_coords[index], self.y_coords[index] + 45))
                            if button_background_rect.collidepoint(mouse_pos):
                                if database.money >= item['price']:
                                    database.money -= item['price']
                                    item['locked'] = True
                                    # Check if the item is a troop or a spell
                                    if item['name'] in ['warrior', 'archer', 'sparta', 'wizard', 'giant']:
                                        troop_data = database.troop_storage.get(item['name'])
                                        if troop_data:
                                            troop_data[0] = True
                                            for troop in self.backpack_troop_list:
                                                if troop['name'] == item['name']:
                                                    troop.update({
                                                        'equip': troop_data[2],
                                                        'money': self.money_image_surf,
                                                        'level': troop_data[1],
                                                        'locked': troop_data[0]
                                                    })
                                                    # Update troop stats based on name
                                                    if item['name'] == 'warrior':
                                                        troop.update({'health': (database.troop_storage['warrior'][3] * 10),
                                                                      'attack damage': (database.troop_storage['warrior'][4] * 10)})
                                                    elif item['name'] == 'archer':
                                                        troop.update({'health': (database.troop_storage['archer'][3] * 10),
                                                                      'attack damage': (database.troop_storage['archer'][4] * 5)})
                                                    elif item['name'] == 'sparta':
                                                        troop.update({'health': (database.troop_storage['sparta'][3] * 10),
                                                                      'attack damage': (database.troop_storage['sparta'][4] * 10)})
                                                    elif item['name'] == 'wizard':
                                                        troop.update({'health': (database.troop_storage['wizard'][3] * 10),
                                                                      'attack damage': (database.troop_storage['wizard'][4] * 5)})
                                                    elif item['name'] == 'giant':
                                                        troop.update({'health': (database.troop_storage['giant'][3] * 10),
                                                                      'attack damage': (database.troop_storage['giant'][4] * 10)})
                                    else:
                                        spell_data = database.spell_storage.get(item['name'])
                                        if spell_data:
                                            spell_data[0] = True
                                            for spell in self.spell_list:
                                                if spell['name'] == item['name']:
                                                    spell.update({
                                                        'locked': spell_data[0],
                                                        'equip': spell_data[2],
                                                        'level': spell_data[1]
                                                    })
                                                    # Update spell-specific data
                                                    if item['name'] == 'freeze':
                                                        spell.update(
                                                            {'spell function': int(database.spell_storage['freeze'][3] * 100)})
                                                    elif item['name'] == 'healing':
                                                        spell.update({'healing function': int(database.spell_storage['healing'][3])})
                                                    elif item['name'] == 'rage':
                                                        spell.update(
                                                            {'spell function': int(database.spell_storage['rage'][3] * 100)})
                                else:
                                    break

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
                        castle_data = database.castle_storage['default_castle']
                        health_button_rect = item['upgrades button'].get_rect(bottomleft=(120, 550))
                        mining_button_rect = item['upgrades button'].get_rect(bottomleft=(340, 550))

                        if health_button_rect.collidepoint(mouse_pos):
                            if database.money >= item['health price']:
                                database.money -= item['health price']
                                item['health level'] += 1
                                item['health price'] = int(item['health price'] * 1.1) // 1
                                item['health'] = int(item['health'] * 1.1) // 1
                                # handle firebase data
                                castle_data[1] += 1
                                castle_data[3] = (castle_data[3] * 1.1) // 1
                                castle_data[5] = (castle_data[5] * 1.1) // 1
                        elif mining_button_rect.collidepoint(mouse_pos):
                            if database.money >= item['mining speed price']:
                                database.money -= item['mining speed price']
                                item['mining speed level'] += 1
                                item['mining speed price'] = int(item['mining speed price'] * 1.1) // 1
                                item['mining speed'] += 5
                                # handle firebase data
                                castle_data[2] += 1
                                castle_data[4] += 5
                                castle_data[6] = (castle_data[6] * 1.1) // 1

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

                if self.backpack:
                    # Clear the list before re-populating it to avoid duplicates
                    self.troop_equipped_list.clear()

                    for item in self.backpack_troop_list:
                        if item['equip']:
                            item_copy = item.copy()

                            if item_copy['name'] == 'warrior':
                                troop_equipped_image = pygame.image.load(
                                    'War of stick/Picture/stickman sword/stickman warrior card.png')
                            elif item_copy['name'] == 'archer':
                                troop_equipped_image = pygame.image.load(
                                    'War of stick/Picture/stickman archer/stickman archer card.png')
                            elif item_copy['name'] == 'sparta':
                                troop_equipped_image = pygame.image.load(
                                    'War of stick/Picture/stickman sparta/stickman sparta card.png')
                            elif item_copy['name'] == 'wizard':
                                troop_equipped_image = pygame.image.load(
                                    'War of stick/Picture/stickman wizard/stickman wizard card.png')
                            elif item_copy['name'] == 'giant':
                                troop_equipped_image = pygame.image.load(
                                    'War of stick/Picture/stickman giant/stickman giant card.png')

                            troop_equipped_image = pygame.transform.scale(troop_equipped_image, (50, 55))
                            item_copy['image'] = troop_equipped_image
                            self.troop_equipped_list.append(item_copy)

                if self.backpack and self.selected_category == 'Troop':
                    for item in self.backpack_troop_list:
                        troop_data = database.troop_storage.get(item['name'])
                        if item['name'] == self.clicked_image_surf:
                            upgrades_button_rect = item['upgrades button'].get_rect(midbottom=(220, 565))
                            if upgrades_button_rect.collidepoint(mouse_pos):
                                if database.money >= item['upgrades price']:
                                    database.money -= item['upgrades price']
                                    item['upgrades price'] = int((item['upgrades price']) * 1.1) // 1
                                    item['health'] = int((item['health']) * 1.1) // 1
                                    item['attack damage'] = int((item['attack damage']) * 1.1)
                                    item['level'] += 1
                                    # handle firebase
                                    troop_data[1] += 1
                                    troop_data[3] = (troop_data[3] * 1.1) // 1  # Update health
                                    troop_data[4] = (troop_data[4] * 1.1)  # Update attack damage
                                    troop_data[6] = (troop_data[6] * 1.1) // 1  # update upgrades price

                            equip_button_rect = item['equip button'].get_rect(midbottom=(383, 565))
                            if equip_button_rect.collidepoint(mouse_pos):
                                if item['equip'] == True:
                                    item['equip'] = False
                                    troop_data[2] = False
                                    for equipped_item in self.troop_equipped_list:
                                        if equipped_item['name'] == item['name']:
                                            self.troop_equipped_list.remove(equipped_item)

                                else:
                                    item['equip'] = True
                                    troop_data[2] = True
                                    item_copy = item.copy()
                                    if item_copy['name'] == 'warrior':
                                        troop_equipped_image = pygame.image.load(
                                            'War of stick/Picture/stickman sword/stickman warrior card.png')
                                    elif item_copy['name'] == 'archer':
                                        troop_equipped_image = pygame.image.load(
                                            'War of stick/Picture/stickman archer/stickman archer card.png')
                                    elif item_copy['name'] == 'sparta':
                                        troop_equipped_image = pygame.image.load(
                                            'War of stick/Picture/stickman sparta/stickman sparta card.png')
                                    elif item_copy['name'] == 'wizard':
                                        troop_equipped_image = pygame.image.load(
                                            'War of stick/Picture/stickman wizard/stickman wizard card.png')
                                    elif item_copy['name'] == 'giant':
                                        troop_equipped_image = pygame.image.load(
                                            'War of stick/Picture/stickman giant/stickman giant card.png')

                                    troop_equipped_image = pygame.transform.scale(troop_equipped_image, (50, 55))
                                    item_copy['image'] = troop_equipped_image
                                    self.troop_equipped_list.append(item_copy)

                if self.backpack:
                    self.spell_equipped_list.clear()

                    for item in self.spell_list:
                        if item['equip'] == True:
                            self.spell_equipped_list.append(item)

                if self.backpack and self.selected_category == 'Spell':
                    for item in self.spell_list:
                        spell_type = item['name']
                        spell_image = item['image']
                        position = self.spell_position[0].get(spell_type, (0, 0))
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
                        spell_data = database.spell_storage.get(item['name'])
                        if item['name'] == self.clicked_spell_surf:
                            upgrades_button_rect = item['upgrades button'].get_rect(midbottom=(220, 565))
                            if upgrades_button_rect.collidepoint(mouse_pos):
                                if database.money >= item['upgrades price']:
                                    database.money -= item['upgrades price']
                                    item['upgrades price'] = int((item['upgrades price']) * 1.1) // 1
                                    item['level'] += 1
                                    # handle firebase data
                                    if spell_data is None:
                                        continue
                                    if item['name'] in ['freeze', 'rage']:
                                        item['spell function'] = int((item['spell function']) * 1.1) // 1
                                        # handle firebase data
                                        spell_data[1] += 1
                                        spell_data[3] += 0.05
                                        spell_data[4] = (spell_data[4] * 1.1) // 1

                                    else:
                                        item['healing function'] += 100
                                        # handle firebase data
                                        spell_data[1] += 1
                                        spell_data[3] += 100
                                        spell_data[4] = (spell_data[4] * 1.1) // 1

                            equip_button_rect = item['equip button'].get_rect(midbottom=(383, 565))
                            if equip_button_rect.collidepoint(mouse_pos):
                                if item['equip']:
                                    item['equip'] = False
                                    spell_data[2] = False
                                    if item in self.spell_equipped_list:
                                        self.spell_equipped_list.remove(item)
                                else:
                                    item['equip'] = True
                                    spell_data[2] = True
                                    if item not in self.spell_equipped_list:
                                        self.spell_equipped_list.append(item)

                if self.store:
                    if self.back_level_background_rect.collidepoint(mouse_pos):
                        self.go_level_py = True

    def backpack_screen(self):
        self.display_detail_info()
        for index, item in enumerate(self.troop_equipped_list):
            if item['equip'] == True and index < len(self.x_troop_equipped_position):
                equipped_troop_image_surf = item['image']
                equipped_troop_image_x_coords = self.x_troop_equipped_position[index]
                equipped_troop_image_y_coords = self.y_troop_equipped_position[index]
                equipped_troop_image_rect = equipped_troop_image_surf.get_rect(
                    topleft=(equipped_troop_image_x_coords, equipped_troop_image_y_coords))
                self.screen.blit(equipped_troop_image_surf, equipped_troop_image_rect)

        for index, item in enumerate(self.spell_equipped_list):
            if item['equip'] == True and index < len(self.x_spell_equipped_position):
                equipped_spell_image_surf = item['image']
                equipped_spell_image_surf = pygame.transform.scale(equipped_spell_image_surf, (55, 55))
                equipped_spell_image_x_coords = self.x_spell_equipped_position[index]
                equipped_spell_image_y_coords = self.y_spell_equipped_position[index]
                equipped_spell_image_rect = equipped_spell_image_surf.get_rect(
                    topleft=(equipped_spell_image_x_coords, equipped_spell_image_y_coords))
                self.screen.blit(equipped_spell_image_surf, equipped_spell_image_rect)

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

        self.money_surf = self.font.render(str(database.money), True, 'Black')
        self.money_num_rect = self.money_surf.get_rect(topright=(460, 210))
        self.screen.blit(self.money_surf, self.money_num_rect)
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

            self.money_surf = self.font.render(str(database.money), True, 'Black')
            self.money_num_rect = self.money_surf.get_rect(topright=(460, 210))
            self.screen.blit(self.money_surf, self.money_num_rect)

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
                health_upgrades_rect = health_upgrades_surf.get_rect(topright=(233, 535))
                self.screen.blit(health_upgrades_surf, health_upgrades_rect)

                health_money_icon_surf = item['money image']
                health_money_icon_rect = health_money_icon_surf.get_rect(bottomleft=(237, 549))
                self.screen.blit(health_money_icon_surf, health_money_icon_rect)

                mining_upgrades_msg_surf = self.font.render(f"Mining: Lv{str(item['mining speed level'])}", True, 'Black')
                mining_upgrades_msg_rect = mining_upgrades_msg_surf.get_rect(bottomleft=(352, 530))
                self.screen.blit(mining_upgrades_msg_surf, mining_upgrades_msg_rect)

                mining_upgrades_surf = self.price_font.render(f"Upgrade {str(item['mining speed price'])}", True, 'Black')
                mining_upgrades_rect = mining_upgrades_surf.get_rect(topright=(450, 535))
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

                if item['locked'] == False:
                    locked_msg_surf = self.price_font.render(f"Locked", True, 'White')
                    locked_msg_rect = locked_msg_surf.get_rect(center=(msg_position))
                    self.screen.blit(locked_msg_surf, locked_msg_rect)
                else:
                    level_msg_surf = self.price_font.render(f"Level: {str(item['level'])}", True, 'White')
                    level_msg_rect = level_msg_surf.get_rect(center=(msg_position))
                    self.screen.blit(level_msg_surf, level_msg_rect)

        elif self.selected_category == 'Spell':
            for index, item in enumerate(self.spell_list):
                spell_type = item['name']
                spell_image = item['image']
                position = self.spell_position[0].get(spell_type, (0, 0))
                spell_rect = spell_image.get_rect(center=(position))
                self.screen.blit(spell_image, spell_rect)

                msg_position = self.spell_msg_position[0].get(spell_type, (0, 0))

                if item['locked'] == False:
                    locked_msg_surf = self.price_font.render(f"Locked", True, 'White')
                    locked_msg_rect = locked_msg_surf.get_rect(center=(msg_position))
                    self.screen.blit(locked_msg_surf, locked_msg_rect)
                else:
                    level_msg_surf = self.price_font.render(f"Level: {str(item['level'])}", True, 'White')
                    level_msg_rect = level_msg_surf.get_rect(center=(msg_position))
                    self.screen.blit(level_msg_surf, level_msg_rect)

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

                if item['locked'] == True:
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

                            gold_text_surf = self.font.render(str(100), True, 'White')
                            gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                            self.screen.blit(gold_text_surf, gold_text_rect)

                            diamond_icon_surf = item['diamond icon']
                            diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                            self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                            diamond_text_surf = self.font.render(('-'), True, "White")
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

                            diamond_text_surf = self.font.render(str(200), True, "White")
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

                            gold_text_surf = self.font.render(str(700), True, 'White')
                            gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                            self.screen.blit(gold_text_surf, gold_text_rect)

                            diamond_icon_surf = item['diamond icon']
                            diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                            self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                            diamond_text_surf = self.font.render(str(200), True, "White")
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

                            gold_text_surf = self.font.render(str(500), True, 'White')
                            gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                            self.screen.blit(gold_text_surf, gold_text_rect)

                            diamond_icon_surf = item['diamond icon']
                            diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                            self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                            diamond_text_surf = self.font.render(str(500), True, "White")
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

                            gold_text_surf = self.font.render(str(700), True, 'White')
                            gold_text_rect = gold_text_surf.get_rect(midleft=(406, 293))
                            self.screen.blit(gold_text_surf, gold_text_rect)

                            diamond_icon_surf = item['diamond icon']
                            diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                            self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                            diamond_text_surf = self.font.render(str(200), True, "White")
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

                else:
                    pass

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

                if item['locked'] == True:
                    if self.clicked_spell_surf == 'freeze':
                        if item['name'] == 'freeze':
                            freeze_spell_image_surf = item['image']
                            freeze_spell_image_surf = pygame.transform.scale(freeze_spell_image_surf, (220, 220))
                            freeze_spell_image_rect = freeze_spell_image_surf.get_rect(midleft=(142, 375))
                            self.screen.blit(freeze_spell_image_surf, freeze_spell_image_rect)

                            spell_name_surf = self.title_font.render(f"{str(item['name'])}", True, 'White')
                            spell_name_rect = spell_name_surf.get_rect(midtop=(246, 205))
                            self.screen.blit(spell_name_surf, spell_name_rect)

                            diamond_icon_surf = item['diamond icon']
                            diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                            self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                            diamond_text_surf = self.font.render(str(500), True, "White")
                            diamond_text_rect = diamond_text_surf.get_rect(midleft=(406, 332))
                            self.screen.blit(diamond_text_surf, diamond_text_rect)

                            freeze_animation_image_surf = item['freeze icon']
                            freeze_animation_image_rect = freeze_animation_image_surf.get_rect(midleft=(370, 370))
                            self.screen.blit(freeze_animation_image_surf, freeze_animation_image_rect)

                            freeze_animation_text = self.font.render(f"{str(item['spell function'])}%", True, 'White')
                            freeze_animation_text_rect = freeze_animation_text.get_rect(midleft=(410, 371))
                            self.screen.blit(freeze_animation_text, freeze_animation_text_rect)

                            upgrades_button_surf = item['upgrades button']
                            upgrades_button_rect = upgrades_button_surf.get_rect(midbottom=(220, 565))
                            self.screen.blit(upgrades_button_surf, upgrades_button_rect)

                            level_msg_surf = self.font.render(f"Freeze: Lv{str(item['level'])}", True, 'Black')
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

                            diamond_icon_surf = item['diamond icon']
                            diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                            self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                            diamond_text_surf = self.font.render(str(500), True, "White")
                            diamond_text_rect = diamond_text_surf.get_rect(midleft=(406, 332))
                            self.screen.blit(diamond_text_surf, diamond_text_rect)

                            healing_animation_image_surf = item['healing icon']
                            healing_animation_image_rect = healing_animation_image_surf.get_rect(midleft=(370, 370))
                            self.screen.blit(healing_animation_image_surf, healing_animation_image_rect)

                            healing_animation_text = self.font.render(f"{str(item['healing function'])}", True, 'White')
                            healing_animation_text_rect = healing_animation_text.get_rect(midleft=(410, 371))
                            self.screen.blit(healing_animation_text, healing_animation_text_rect)

                            upgrades_button_surf = item['upgrades button']
                            upgrades_button_rect = upgrades_button_surf.get_rect(midbottom=(220, 565))
                            self.screen.blit(upgrades_button_surf, upgrades_button_rect)

                            level_msg_surf = self.font.render(f"Healing: Lv{str(item['level'])}", True, 'Black')
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

                            diamond_icon_surf = item['diamond icon']
                            diamond_icon_rect = diamond_icon_surf.get_rect(midleft=(366, 330))
                            self.screen.blit(diamond_icon_surf, diamond_icon_rect)

                            diamond_text_surf = self.font.render(str(400), True, "White")
                            diamond_text_rect = diamond_text_surf.get_rect(midleft=(406, 332))
                            self.screen.blit(diamond_text_surf, diamond_text_rect)

                            rage_animation_image_surf = item['rage icon']
                            rage_animation_image_rect = rage_animation_image_surf.get_rect(midleft=(370, 370))
                            self.screen.blit(rage_animation_image_surf, rage_animation_image_rect)

                            rage_animation_text = self.font.render(f"{str(item['spell function'])}%", True, 'White')
                            rage_animation_text_rect = rage_animation_text.get_rect(midleft=(410, 371))
                            self.screen.blit(rage_animation_text, rage_animation_text_rect)

                            upgrades_button_surf = item['upgrades button']
                            upgrades_button_rect = upgrades_button_surf.get_rect(midbottom=(220, 565))
                            self.screen.blit(upgrades_button_surf, upgrades_button_rect)

                            level_msg_surf = self.font.render(f"Rage: Lv{str(item['level'])}", True, 'Black')
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
            self.money_surf = self.font.render(str(database.money), True, 'Black')
            self.screen.blit(self.money_surf, self.money_rect)

            self.screen.blit(self.back_level_background_surf, self.back_level_background_rect)
            self.screen.blit(self.back_level_button_surf, self.back_level_button_rect)
            self.screen.blit(self.level_word_surf, self.level_word_rect)

            for index, item in enumerate(self.store_list):
                if item['locked'] == False and index < len(self.x_coords):
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
                    button_background_surf = pygame.transform.scale(button_background_surf, (225, 75))
                    button_background_rect = button_background_surf.get_rect(
                        center=(self.x_coords[index] - 5, self.y_coords[index] + 45))
                    self.screen.blit(button_background_surf, button_background_rect)

                    unlocked_text_surf = self.price_font.render('Unlocked', True, 'Black')
                    unlocked_text_rect = unlocked_text_surf.get_rect(center=(self.x_coords[index] - 7, self.y_coords[index] + 46))
                    self.screen.blit(unlocked_text_surf, unlocked_text_rect)

        elif self.backpack:
            self.backpack_screen()

    def run(self):
        while True:
            self.screen.fill((255, 255, 255))

            self.event_handling()
            self.game_start()
            pygame.display.update()
            self.clock.tick(60)


"""
"""
"""
"""


home = GameHome()
level = GameLevel()
stick_of_war = GameStickOfWar()
pokemon_vs_stick = GamePokemonVsStick()
run_pokemon_vs_stick = False
run_home = True
run_level = False
run_store = False
run_stick_of_war = False

async def main():
    global home
    global level
    global stick_of_war
    global run_pokemon_vs_stick
    global run_home
    global run_level
    global run_store
    global run_stick_of_war

    while True:
        try:
            if run_home:
                home.home_music = pygame.mixer.Sound('War of stick/Music/home_music.wav')
                home.home_music.set_volume(0.2)
                home.home_music.play(loops=-1)
                while True:
                    home.screen.fill((255, 255, 255))

                    home.event_handling()
                    home.game_start_bg()
                    if home.go_pokemon_py:
                        run_home = False
                        run_pokemon_vs_stick = True
                        home.go_pokemon_py = False
                        break
                    if home.go_level_py:
                        run_home = False
                        run_level = True
                        home.go_level_py = False
                        break
                    if database.login_method is None:
                        if home.loading:
                            home.update_progress()
                        elif home.finish_loading:
                            if home.choosing_login_method:
                                home.signing_user()
                            elif home.signing_in:
                                home.sign_in()
                            elif home.signing_up:
                                home.sign_up()
                            elif home.choose_game_to_play:
                                home.choose_game()
                    else:
                        home.choose_game()
                    home.display_message()
                    pygame.display.update()
                    home.clock.tick(60)
                    await asyncio.sleep(0)

            elif run_pokemon_vs_stick:
                pokemon_vs_stick.reset_func()
                pokemon_vs_stick.bg_music = pygame.mixer.Sound('Plant vs Stick/audio/bg_music.mp3')
                pokemon_vs_stick.bg_music.set_volume(0.1)
                pokemon_vs_stick.bg_music.play(loops=-1)
                while True:
                    if pokemon_vs_stick.go_home_py:
                        run_home = True
                        run_pokemon_vs_stick = False
                        pokemon_vs_stick.go_home_py = False
                        home.choose_game_to_play = True
                        home.choosing_login_method = False
                        break

                    # Clear screen
                    pokemon_vs_stick.screen.fill((255, 255, 255))

                    # event_handling_control_function
                    pokemon_vs_stick.event_handling()

                    # start function which will blit screen and etc
                    pokemon_vs_stick.game_start()

                    pygame.display.update()
                    pygame.display.flip()  # redraw the screen

                    pokemon_vs_stick.clock.tick(60)  # 60 fps
                    await asyncio.sleep(0)

            elif run_level:
                level.level_select_music = pygame.mixer.Sound('War of stick/Music/level.mp3')
                level.level_select_music.set_volume(0.2)
                level.level_select_music.play(loops=-1)

                while True:
                    if level.go_store_py:
                        run_level = False
                        run_store = True
                        level.go_store_py = False
                        break
                    elif level.go_home_py:
                        run_level = False
                        run_home = True
                        level.go_home_py = False
                        home.choose_game_to_play = True
                        home.choosing_login_method = False
                        break
                    elif level.go_stick_of_war:
                        run_level = False
                        run_stick_of_war = True
                        level.go_stick_of_war = False
                        break

                    level.screen.fill((255, 255, 255))

                    level.choose_level(stick_of_war.winner, stick_of_war.played_time)

                    level.event_handling()

                    pygame.display.update()
                    level.clock.tick(60)
                    await asyncio.sleep(0)

            elif run_store:
                store = Game_Store()
                while True:
                    if store.go_level_py:
                        run_store = False
                        run_level = True
                        store.go_level_py = False
                        break
                    store.screen.fill((255, 255, 255))

                    store.event_handling()
                    store.game_start()
                    pygame.display.update()
                    store.clock.tick(60)
                    await asyncio.sleep(0)

            elif run_stick_of_war:
                stick_of_war.reset_func()
                stick_of_war.game_music = pygame.mixer.Sound('War of stick/Music/game_music.mp3')
                stick_of_war.game_music.set_volume(0.2)
                stick_of_war.game_music.play(loops=-1)
                while True:
                    if stick_of_war.go_level_py:
                        run_level = True
                        run_stick_of_war = False
                        stick_of_war.go_level_py = False
                        break
                    stick_of_war.game_start()
                    stick_of_war.event_handling()

                    pygame.display.update()  # Update the display
                    stick_of_war.clock.tick(60)  # Limit frame rate to 60 FPS
                    await asyncio.sleep(0)
        except:
            database.update_user()
            database.push_data()
            break

asyncio.run(main())
