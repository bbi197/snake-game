import turtle
import random

# Set up constants for the game
WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 10
DELAY = 100

# Define movement offsets for the snake in different directions
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# Initialize global variables for the game
snake = [[0, 0], [0, 20], [0, 40], [0, 50], [0, 60]]
snake_direction = "up"
food_pos = (0, 100)

# Define function to reset the game
def reset():
    global snake, snake_direction, food_pos, pen
    
    # Reset snake to starting position
    snake = [[0, 0], [0, 20], [0, 40], [0, 50], [0, 60]]
    snake_direction = "up"
    
    # Choose a random position for the food
    food_pos = get_random_food_pos()
    
    # Move food turtle to new position
    food.goto(food_pos)
    
    # Start the game loop
    move_snake()

# Define function to move the snake
def move_snake():
    global snake_direction
    
    # Determine the next position for the head of the snake
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_direction][0]
    new_head[1] = snake[-1][1] + offsets[snake_direction][1]

    # Check for self-collision
    if new_head in snake[:-1]:
        reset()
    else:
        # Add new head to the snake
        snake.append(new_head)
        
        # Check if the snake has collided with the food
        if not food_collision():
            # Remove the tail of the snake if it hasn't eaten food
            snake.pop(0)
        
        # Allow the snake to wrap around the screen if it goes off the edge
        if snake[-1][0] > WIDTH / 2:
            snake[-1][0] -= WIDTH
        elif snake[-1][0] < - WIDTH / 2:
            snake[-1][0] += WIDTH
        elif snake[-1][1] > HEIGHT / 2:
            snake[-1][1] -= HEIGHT
        elif snake[-1][1] < -HEIGHT / 2:
            snake[-1][1] += HEIGHT
        
        # Clear the previous snake stamps
        pen.clearstamps()
        
        # Draw the snake on the screen
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()
        
        # Update the screen
        screen.update()
        
        # Rinse and repeat
        turtle.ontimer(move_snake, DELAY)

# Define function to check if the snake has collided with the food
def food_collision():
    global food_pos
    
    # Check the distance between the snake head and the food
    if get_distance(snake[-1], food_pos) < 20:
        # Choose a new position for the food and move the turtle there
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    
    return False

# Define function to get a random position for the food
def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)

# Set up the screen and pen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.penup()

# Create a turtle to represent the food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()
food.goto(food_pos)

# Bind arrow keys to change the snake direction
screen.onkeypress(lambda: change_direction("up"), "Up")
screen.onkeypress(lambda: change_direction("down"), "Down")
screen.onkeypress(lambda: change_direction("left"), "Left")
screen.onkeypress(lambda: change_direction("right"), "Right")
screen.listen()

# Start the game
reset()
turtle.done()
