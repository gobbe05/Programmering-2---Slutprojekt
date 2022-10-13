import pygame
import random


class Snake(object):

    def __init__(self):
        self.length = 1
        self.position = [10, 10]
        self.direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        self.tails = []
        self.color = (17, 24, 47)

    def get_position(self):
        return [self.position[0], self.position[1]]

    def get_direction(self):
        return (self.direction[0], self.direction[1])

    def turn(self, direction):
        initialDirection = self.direction

        if (direction == "left"):
            self.direction = (-1, 0)
        if (direction == "right"):
            self.direction = (1, 0)
        if (direction == "up"):
            self.direction = (0, -1)
        if (direction == "down"):
            self.direction = (0, 1)

        if initialDirection[0] + self.direction[0] == 0 and initialDirection[
                1] + self.direction[1] == 0:
            self.direction = initialDirection

    def reset(self):
        pass

    def draw(self, surface, GRID_SIZE):
        pygame.draw.rect(
            surface, self.color,
            pygame.Rect(self.position[0] * GRID_SIZE,
                        self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        for i in self.tails:
            pygame.draw.rect(
                surface, self.color,
                pygame.Rect(i.get_position()[0] * GRID_SIZE,
                            i.get_position()[1] * GRID_SIZE, GRID_SIZE,
                            GRID_SIZE))




    # Moves all the tail parts. Then checks if food is eating.
    # In that case spawn a new tail on the latest tail/head position
    # Then move the head
    def move(self, food):
        
        # Loop through tails array backwards
        for i in reversed(range(0, len(self.tails))):
            if i == 0: #Move the tail closest to head
                self.tails[i].move(self.get_position())

            else:      # Move the other tails
                self.tails[i].move(self.tails[i-1].get_position())

        if self.get_position() == food.get_position():
            self.tails.append(Tail(self.position))  # Create a new tail
            food.randomize_position()               # Change food position
        # Moving the head
        self.position[0] += self.direction[0]   # X
        self.position[1] += self.direction[1]   # Y
        
        

            




    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.turn("left")
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.turn("right")
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.turn("up")
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.turn("down")


class Tail(object):

    def __init__(self, position):
        self.position = position

    def move(self, position):
        self.position = position

    def get_direction(self):
        return self.direction

    def get_position(self):
        return self.position
