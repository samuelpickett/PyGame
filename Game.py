import pygame

pygame.init()
# Set size of the screen
screen_width = 800
screen_height = 800
screen_title = "Crossy RPG"
# Colors according to RGB codes
white_color = (255,255,255)
black_color = (0,0,0)
# Sets the clock rate for game
clock = pygame.time.Clock()
tick_rate = 60
is_game_over = False
# Creates the window to display the game
game_screen = pygame.display.set_mode((screen_width, screen_height))
# Set the game window color to white
game_screen.fill(white_color)
pygame.display.set_caption(screen_title)

player_image = pygame.image.load("images/player.png")
player_image = pygame.transform.scale(player_image, (50,50))


# Main game loop
while not is_game_over:
    # Exits game if we have a quite type event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True
    # Draws a circle and rectangle
    # pygame.draw.rect(game_screen, (0,255,0), [350,350,100,100])
    # pygame.draw.circle(game_screen, (0,0,255), (400,400), 50)
    
    game_screen.blit(player_image, (375, 375))
    
    
    # Update the game graphics
    pygame.display.update()
    clock.tick(tick_rate)
# Quite pygame and the program
pygame.quit()
quit()
