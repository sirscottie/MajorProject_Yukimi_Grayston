#buttons_Yukimi_Grayston
#this code defines the button class and checks if the player has clicked the button

import pygame

#defines the screen
s_width = 500
s_height = 500
screen = pygame.display.set_mode((s_width, s_height))

class button():
    """Creates the user interatable buttons"""
    def __init__(self, x, y, image):
        """Creates all the variables for the button class"""
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        """Draws the button onto the screen """
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check fot the mouse clicks
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        #draw button
        screen.blit(self.image, self.rect)

        return action