from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return "This was a small asteroid"
        else:
            random_angle = int(random.uniform(0.2, 0.5) * 100)
            a1 = Asteroid(self.position.x, self.position.y, self.radius)
            a2 = Asteroid(self.position.x, self.position.y, self.radius)
            a1.radius = self.radius - ASTEROID_MIN_RADIUS
            a2.radius = self.radius - ASTEROID_MIN_RADIUS
            a1.velocity = self.velocity = self.velocity.rotate(random_angle)
            a2.velocity = self.velocity = self.velocity.rotate(-random_angle)
            return a1, a2
