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


class Game():
    tick_rate = 60
    direction = 0
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
    
        # Creates the window to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        # Set the game window color to white
        self.game_screen.fill(white_color)
        pygame.display.set_caption(title)
    def run_game_loop(self):
        player = PlayerCharacter("images/player.png", 375, 700, 50, 50)
        enemy0 = EnemyCharacter("images/enemy.png", 20, 400, 50, 50)
        treasure = GameObject("images/treasure.png", 375, 50, 50,50)
        direction = 0
        is_game_over = False
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
            treasure.draw(self.game_screen)
            # Updates the player's position
            player.move(direction, self.height)
            player.draw(self.game_screen)
            enemy0.move(self.width)
            enemy0.draw(self.game_screen)
            
            # Detects if the player is colliding with an object and ends the game
            if player.detect_collision(enemy0):
                is_game_over = True
            elif player.detect_collision(treasure):
                is_game_over = True
            
            # Update the game graphics
            pygame.display.update()
            clock.tick(self.tick_rate)


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

new_game = Game(screen_title, screen_width, screen_height)
new_game.run_game_loop()





# Quite pygame and the program
pygame.quit()
quit()
