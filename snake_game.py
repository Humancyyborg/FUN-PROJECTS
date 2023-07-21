import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)
        self.body.insert(0, new_head)

    def grow(self):
        tail_x, tail_y = self.body[-1]
        dx, dy = self.direction
        new_tail = ((tail_x - dx) % GRID_WIDTH, (tail_y - dy) % GRID_HEIGHT)
        self.body.append(new_tail)

    def check_collision(self):
        return len(set(self.body)) < len(self.body)

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

# Apple class
class Apple:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

    def respawn(self):
        self.position = self.randomize_position()

# Main function
def main():
    snake = Snake()
    apple = Apple()

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1, 0)

        # Move the snake
        snake.move()

        # Check for collisions
        if snake.body[0] == apple.position:
            apple.respawn()
            snake.grow()

        if snake.check_collision():
            running = False

        # Draw everything
        screen.fill(BLACK)

        # Draw the snake
        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw the apple
        pygame.draw.rect(screen, RED, (apple.position[0] * GRID_SIZE, apple.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
