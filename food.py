import random
import pygame

class Food(object):
  def __init__(self, GRID_WIDTH, GRID_HEIGHT, state):
    self.color = (255, 0, 0)
    self.position = [0,0]
    self.state = state
    self.GRID = [GRID_WIDTH, GRID_HEIGHT]
    self.randomize_position()

  def randomize_position(self):
    self.position = [random.randint(0, self.GRID[0]), random.randint(0, self.GRID[1])]
    self.state['score'] += 1
    self.state['foodPos'] += self.position

  def get_position(self):
    return self.position
  
  def draw(self, surface, GRID_SIZE):
    pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))