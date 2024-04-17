import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Tower Defend")

# Load images
background_image = pygame.image.load('War of stick/map_bg.jpg')
army_one = pygame.image.load('War of stick/background_photo.jpg').convert_alpha()

# Initial position of the background image
bg_x = 0

# Scrolling speed
scroll_speed = 2


class Button:
    def __init__(self, x, y, image, width, height):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        # Mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and click condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                return True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # Draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Create button instance
button_one = Button(40, 20, army_one, 40, 40)

# Flag to keep track of whether the button has been clicked
button_clicked = False

# Main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    # Scroll the background based on keyboard input
    if keys[pygame.K_a]:
        bg_x += scroll_speed
    if keys[pygame.K_d]:
        bg_x -= scroll_speed

    # Ensure the background stays within the window boundaries
    bg_x = max(bg_x, 1000 - background_image.get_width())
    bg_x = min(bg_x, 0)

    # Draw background image
    screen.blit(background_image, (bg_x, 0))

    # Check if the button is clicked
    if button_one.draw() and not button_clicked:
        # If the button is clicked, draw the army image 
        screen.blit(army_one, (100, 100))
        # Set the button clicked status
        button_clicked = True

        # Update the display
    pygame.display.flip()


# mok stupid lah


# jehukewhfoiaejfa\efjegf
# kuaegfueak