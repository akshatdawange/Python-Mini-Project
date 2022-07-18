import pygame
import time
import random

# To initialize pygame module
pygame.init()

# Window Size
window_x = 720
window_y = 720

# Defining colors
color_1 = (255,193,37)  # Color code for Golden
color_2 = (34,139,34)  # Color code for Green
color_3 = (139,26,26)  # Color code for Red (background)
color_4 = (255, 255, 255)  # Color code for White
color_5 = (255,48,48) # Color code for Red (food)

# To initialize the game window
add_cap = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("SNAKE")

# To control the game's framerate
timer = pygame.time.Clock()

# Defining the snake speed
snake_speed = 15

#Defining the first snake block
snake_block = 10

# Initializing fonts for the text at the end and the score throughout the game
display_style = pygame.font.SysFont("Old English Text MT", 25, "bold")
score_font = pygame.font.SysFont("Old English Text MT", 25, "bold")

# Function to display the final score
def f_score(score):
    value = score_font.render("Score: " + str(score), True, color_4)
    add_cap.blit(value, [0, 0])

# Function to make the snake
def make_snake(snake_block, list_snake):
    for x in list_snake:
        pygame.draw.rect(add_cap, color_1, [x[0], x[1], snake_block, snake_block])

# Function to display message at the end of the game
def display_msg(msg, color):
    mssg = display_style.render(msg, True, color)
    add_cap.blit(mssg, [105, window_y / 2])

# Function for when the game starts
def game_start():
    # Initialize game over and game close as false 
    game_over = False
    game_close = False

    # Position of the snake 
    values_x1 = window_x / 2
    values_y1 = window_y / 2

    # The new position of the snake that gets added to the original position
    new_x1 = 0
    new_y1 = 0

    # List snake stores number of blocks the snake has
    list_snake = []
    # It is the length of the snake
    snake_len = 1

    # To initialize the random position of the food
    food_posx = round(random.randrange(0, window_x - snake_block) / 10.0) * 10.0
    food_posy = round(random.randrange(0, window_y - snake_block) / 10.0) * 10.0

    # This loop goes on till game over becomes true
    while not game_over:

        # This loop goes on when game close becomes true
        while game_close == True:
            
            #The background will be filled with color 3
            add_cap.fill(color_3)

            #This message is displayed on screen after the game closes
            display_msg("Game Over :( To play again press P and to Quit press Q", color_4)
            f_score(snake_len - 1)
            
            # Updates the screen
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #If the 'P' key is pressed the game restarts
                    if event.key == pygame.K_p:
                        game_start()
                    #If the 'Q' key is pressed the program ends
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                #If the 'Left Arrow' key is pressed the snake goes left
                if event.key == pygame.K_LEFT:
                    new_x1 = -snake_block
                    new_y1 = 0
                #If the 'Right Arrow' key is pressed the snake goes right
                elif event.key == pygame.K_RIGHT:
                    new_x1 = snake_block
                    new_y1 = 0
                #If the 'Up Arrow' key is pressed the snake goes up
                elif event.key == pygame.K_UP:
                    new_y1 = -snake_block
                    new_x1 = 0
                #If the 'Down Arrow' key is pressed the snake goes down    
                elif event.key == pygame.K_DOWN:
                    new_y1 = snake_block
                    new_x1 = 0

        # If the snake tries to exit the window the game closes
        if values_x1 >= window_x or values_x1 < 0 or values_y1 >= window_y or values_y1 < 0:
            game_close = True

        # The position of the snake changes continuously
        values_x1 = values_x1 + new_x1
        values_y1 = values_y1 + new_y1
        add_cap.fill(color_2)

        #The food is shown onscreen
        pygame.draw.rect(add_cap, color_5, [food_posx, food_posy, snake_block, snake_block])

        # Initialize the  new block of the snake
        snake_head = []
        #This block gets appended to the snake
        snake_head.append(values_x1)
        snake_head.append(values_y1)
        list_snake.append(snake_head)

        # To stop the snake from growing without eating
        if len(list_snake) > snake_len:
            del list_snake[0]

        # If the snake hits itself the game closes
        for x in list_snake[:-1]:
            if x == snake_head:
                game_close = True

        # make_snake function is called to increase the size of the snake when the snake eats
        make_snake(snake_block, list_snake)
        # Increases the score as soon as you eat the food
        f_score(snake_len - 1)

        # The display updates showing new score and bigger snake
        pygame.display.update()

        # When the snake block and the food block collide the food position changes and the snake length increases by 1
        if values_x1 == food_posx and values_y1 == food_posy:
            food_posx = round(random.randrange(0, window_x - snake_block)/10.0)*10.0
            food_posy = round(random.randrange(0, window_y - snake_block)/10.0)*10.0
            snake_len = snake_len + 1

        # To keep the game's framerate constant at the speed of the snake
        timer.tick(snake_speed)

    # To quit the pygame library
    pygame.quit()
    # To quit the program
    quit()

# To call game start function at the start of the code
game_start()
