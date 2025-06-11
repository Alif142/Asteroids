import pygame
from circleshape import *
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PlAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= PlAYER_TURN_SPEED * dt

        if keys[pygame.K_d]:
            self.rotation += PlAYER_TURN_SPEED * dt

        if keys[pygame.K_w]:
            self.move_Forward(dt)

        if keys[pygame.K_s]:
            self.move_Back(dt)

    def move_Forward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def move_Back(self, dt):
        backward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position -= backward * PLAYER_SPEED * dt
