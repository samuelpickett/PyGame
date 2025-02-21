import pygame

# Set size of the screen
screen_width = 800
screen_height = 800
screen_title = "Crossy RPG"
# Colors according to RGB codes
white_color = (255,255,255)
black_color = (0,0,0)
# Sets the clock rate for game
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("comicsans", 75)

class Game():
    tick_rate = 60
    direction = 0
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height
    
        # Creates the window to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        # Set the game window color to white
        self.game_screen.fill(white_color)
        pygame.display.set_caption(title)
        
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))
    
    def run_game_loop(self, level_speed):
        player = PlayerCharacter("images/player.png", 375, 700, 50, 50)
        enemy0 = EnemyCharacter("images/enemy.png", 20, 600, 50, 50)
        enemy0.speed *= level_speed
        enemy1 = EnemyCharacter("images/enemy.png", self.width - 50, 400, 50, 50)
        enemy1.speed *= level_speed
        enemy2 = EnemyCharacter("images/enemy.png", 20, 200, 50, 50)
        enemy2.speed *= level_speed
        treasure = GameObject("images/treasure.png", 375, 50, 50,50)
        direction = 0
        is_game_over = False
        did_win = False
        # Main game loop
        while not is_game_over:
            # checks for events
            for event in pygame.event.get():
                # Quits the game
                if event.type == pygame.QUIT:
                    is_game_over = True
                # Moves the player character up and down
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Stops moving the player if they stop pressing a key
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
            self.game_screen.fill(white_color)
            self.game_screen.blit(self.image,(0,0))
            treasure.draw(self.game_screen)
            # Updates the player's position
            player.move(direction, self.height)
            player.draw(self.game_screen)
            enemy0.move(self.width)
            enemy0.draw(self.game_screen)
            if level_speed >= 2:
                enemy1.move(self.width)
                enemy1.draw(self.game_screen)
            if level_speed >= 4:
                enemy1.move(self.width)
                enemy1.draw(self.game_screen)
            
            # Detects if the player is colliding with an object and ends the game
            if player.detect_collision(enemy0):
                is_game_over = True
                text = font.render("You lose", True, black_color)
                self.game_screen.blit(text, (275,350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render("You win", True, black_color)
                self.game_screen.blit(text, (275,350))
                pygame.display.update()
                clock.tick(1)
                break
            
            # Update the game graphics
            pygame.display.update()
            clock.tick(self.tick_rate)
        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return


# Generic game object class to be subclassed by other objects in the game
class GameObject():
    
    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        # Scales the image up
        self.image = pygame.transform.scale(object_image, (50,50))

        self.xpos = x
        self.ypos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.xpos, self.ypos))

# Player character class
class PlayerCharacter(GameObject):
    speed = 10
    # Initializes the character's variables
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
    # Moves the player
    def move(self, direction, max_height):
        if direction > 0:
            self.ypos -= self.speed
        elif direction < 0:
            self.ypos += self.speed
        
        if self.ypos >= max_height - 50:
            self.ypos = max_height - 50
        elif self.ypos <= 0:
            self.ypos = 0
    
    def detect_collision(self, other):
        if self.ypos > other.ypos + other.height or self.ypos + self.height < other.ypos:
            return False
        if self.xpos > other.xpos + other.width or self.xpos + self.width < other.xpos:
            return False
        
        return True

# Enemy character class
class EnemyCharacter(GameObject):
    speed = 10
    # Initializes the character's variables
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
    # Moves the player
    def move(self, max_width):
        if self.xpos <= 20:
            self.speed = abs(self.speed)
        elif self.xpos >= max_width - 70:
            self.speed = -abs(self.speed)
        self.xpos += self.speed


pygame.init()

new_game = Game("images/background.png", screen_title, screen_width, screen_height)
new_game.run_game_loop(1)

# Quite pygame and the program
pygame.quit()
quit()
