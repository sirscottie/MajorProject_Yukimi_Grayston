# main_Yukimi_Grayston
# runs the game functions and updates the game for the collisions and game over conditions

import pygame
from level import World, world_data,  lightsphere_group, chest_group
from player import Player
from buttons import button
from addtiles import lightsphere
pygame.init()

# pygame set up
s_width = 500
s_height = 500

screen = pygame.display.set_mode((s_width, s_height))

# pygame window name
pygame.display.set_caption("Lumi's Land")

#define font
font = pygame.font.Font('BauhausRegular.ttf', 25)
font_score = pygame.font.Font('BauhausRegular.ttf', 10)


# game variables
game_over = 0
main_menu = True
score = 0
tile_size = 25

#define colours
white = (255,255,255)

# loads images
background = pygame.image.load('backgroud.png')
restart_img = pygame.image.load('restart.png')
start_img = pygame.image.load('start.png')
end_img = pygame.image.load('end.png')

def draw_text(text, font, text_col, x, y):
    """This code draws the text onto the screen"""
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



#draws the player onto the screen
player = Player(90, s_height - 100)

#dummy coin to show the score
score_coin = lightsphere(tile_size // 2, tile_size // 2 )
lightsphere_group.add(score_coin )

# loads the level
world = World(world_data)

# create buttons
restart_button = button(s_width // 2, s_height // 2, restart_img)
start_button = button(s_width // 2 - 100, s_height // 2, start_img)
end_button = button(s_width // 2 + 30, s_height // 2, end_img)

# Makes sure the pygame window doesn't close on it's own
run = True
while run:
    #draws the background onto the screen
    screen.blit(background, (0, 0))

    #main menu
    if main_menu == True:
        if end_button.draw():
            run = False
        if start_button.draw():
            main_menu = False

    else:
        #draws the world when the start button is pressed
        world.draw()
        if game_over == 0:
            if pygame.sprite.spritecollide(player, lightsphere_group, True):
                score += 1
            draw_text('X' + str(score), font_score, white, tile_size - 10, 10)

            # draws the collectable coins on screen
            lightsphere_group.draw(screen)
            chest_group.draw(screen)
            # constantly looks for if the player is colliding with the chest
            game_over = player.update(game_over)

        #controls what happens when the game ends
        if game_over == -1:
            #draws "You Win!" next to the restart button
            draw_text('You Win!', font, white, (s_width // 2) - 140, s_height // 2)
            #draws teh restart button onto the screen
            if restart_button.draw():
                #restarts the player
                player.restart(90, s_height - 130)
                game_over = 0
                #stops counting score
                score = 0
    #this is for checking if the user has pressed the exit window button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()
pygame.quit()



