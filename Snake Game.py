import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initial position and direction
snake = [(2, 2)]
snake_direction = (1, 0)

# Food initial position
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score
score = 0

# Game over flag
game_over = False

# Font for displaying the score
font = pygame.font.Font(None, 36)

# Clock for controlling the game speed
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            if event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            if event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            if event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Update snake position
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # Check for collisions
    if snake[0] == food:
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Check if the snake collided with itself or the wall
    if (snake[0] in snake[1:]) or (snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or snake[0][1] < 0 or snake[0][1] >= GRID_HEIGHT):
        game_over = True

    # Clear the screen
    screen.fill(BLACK)

    # Draw the grid, snake, and food
    draw_grid()
    draw_snake(snake)
    draw_food(food)

    # Display the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(10)

# Game over
pygame.quit()
sys.exit()
