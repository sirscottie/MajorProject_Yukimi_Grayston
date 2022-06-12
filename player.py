#player_Yukimi_Grayston
#this python file contains all of the players collisions asw ell as the players movements

import pygame
from level import World, world_data, chest_group

#player variables
s_width = 100
s_height = 100
tile = 25
game_over = 0
world = World(world_data)
screen = pygame.display.set_mode((s_width, s_height))

class Player():
    """This class creates the player character Lumi, within the class is her movements and collisions"""
    def __init__(self, x, y):
        """restarts the player when they click the restart button after hitting the chest"""
        self.restart(x, y)


    def update(self, game_over):
        """contains all the character movement and key presses"""
        dx = 0
        dy = 0

        if game_over == 0:
            # key presses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False:
                self.vel_y = -12
                self.jumped = True

            if key[pygame.K_SPACE] == False:
                self.jumped = False

            if key[pygame.K_LEFT]:
                dx -= 2

            elif key[pygame.K_a]:
                dx -= 2

            if key[pygame.K_RIGHT]:
                dx += 2

            elif key[pygame.K_d]:
                dx += 2

            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            for tile in world.tile_list:
                #check for horizontal collision
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0


                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground (jumping)
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y >= 0
                    #check if above the ground (falling)
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
            #check for collision with chest, the chest causes the game to end
            if pygame.sprite.spritecollide(self, chest_group, False):
                game_over = -1

            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy

            #draw the player onto the screen
            screen.blit(self.image, self.rect)

          # processes the game over variable and ends the game when colliding with the chest
            return game_over

    def restart(self, x, y):
        """Sets up all of the variables for the player class"""
        img = pygame.image.load('lumisprite.png')
        # rezises the image to fit with the tiles
        self.image = pygame.transform.scale(img, (20, 20))
        self.rect = self.image.get_rect()
        # player movement
        self.rect.x = x
        self.rect.y = y
        # rectangle width and height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        # jumping
        self.vel_y = 0
        self.jumped = False



