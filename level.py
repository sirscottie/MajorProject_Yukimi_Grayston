#level_Yukimi_Grayston
#this code will set up the tiles within the game and create the world map
import pygame
from addtiles import lightsphere, chest



#defines variables
s_width = 500
s_height = 500
screen = pygame.display.set_mode((s_width, s_height))
tile_size = 25
lightsphere_group = pygame.sprite.Group()
chest_group = pygame.sprite.Group()


#sets up the world class
class World():
    """This class draws each of the tiles onto the numbers that are represented on the world map"""
    def __init__(self, data):
        """This function draws all the tiles onto each number they are assigned on the world map"""
        self.tile_list = []

        #load images
        terrain_img = pygame.image.load('terrian .png')
        platform_img = pygame.image.load('shadowtile.png')

        #draws the the tiles onto the numbers each sprite is assigned
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                #adds the solid purple blocks in the place of 1's on the tike map
                if tile == 1:
                    img = pygame.transform.scale(terrain_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                #adds the platform blocks on 2's on the tile map
                if tile == 2:
                    img = pygame.transform.scale(platform_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                #adds the coin/light tiles where 3's are on the tile map
                if tile == 3:
                    light = lightsphere(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                    lightsphere_group.add(light)
                #draws the chest onto the screen where there are 8's on the tile map
                if tile == 8:
                    endchest = chest(col_count * tile_size, row_count * tile_size + 20)
                    chest_group.add(endchest)
                col_count += 1
            row_count += 1

    def draw(self):
        """draws the tiles onto each of their assigned tile numbers"""
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


#this list contains all the tile placements
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 3, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 8, 1],
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 2, 5, 0, 0, 0, 1],
[1, 0, 0, 0, 3, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
[1, 7, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
[1, 0, 2, 3, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 4, 2, 2, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 2, 7, 0, 0, 0, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
[1, 0, 0, 0, 0, 0, 3, 0, 2, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
[1, 3, 0, 0, 3, 3, 2, 2, 1, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
[1, 2, 0, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
