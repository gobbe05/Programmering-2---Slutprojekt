import pygame
from snake import Snake
from food import Food

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

state = {

  "score": 0,
  "foodPos": [0,0]
  
}

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    food = Food(GRID_WIDTH, GRID_HEIGHT, state)

    while True:
        clock.tick(3)
        snake.handle_keys()
        surface.fill((0, 0, 0))
        snake.move(food)
        snake.draw(surface, GRID_SIZE)
        food.draw(surface, GRID_SIZE)
        screen.blit(surface, (0, 0))
        pygame.display.update()


main()