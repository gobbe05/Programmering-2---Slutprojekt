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

    def move(self, food):
        #If there is food spawn new Tail
        if self.get_position() == food.get_position():
            if not self.tails:
                self.tails.append(
                    Tail(self.get_position(), self.get_direction(), self))

        for tail in self.tails:
            tail.move()
            if self.get_position() == tail.get_position():
                self.reset()
            else:
                next = len(self.tails) - 1
                self.tails.append(
                    Tail(self.tails[next].get_position(),
                         self.tails[next].get_direction(), self.tails[next]))

            food.randomize_position()

        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]

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

    def __init__(self, position, direction, next):
        self.position = position
        self.direction = direction
        self.next = next

    def move(self):
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]

        self.direction = self.next.get_direction()

    def get_direction(self):
        return self.direction

    def get_position(self):
        return self.position
