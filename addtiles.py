#addtiles_Yukimi_Grayston
#this code creates the classes needed for placing interactive tiles onto the screen
import pygame

class lightsphere(pygame.sprite.Sprite):
    """This class creates the collectable objects"""
    def __init__(self, x, y):
        """draws the collectable item onto the screen"""
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('lightsphere.png')
        self.image = pygame.transform.scale(img, (11, 11))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class chest(pygame.sprite.Sprite):
    """This class creates the chest that ends the game """
    def __init__(self, x, y):
        """draws the chest onto the screen"""
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('chest.png')
        self.image = pygame.transform.scale(img, (11, 11))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
