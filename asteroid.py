import pygame
import random


from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def update(self, dt):
            self.position += self.velocity * dt
            
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
           angle = random.uniform(20, 50)
           a1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
           a2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
           a1.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
           a2.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
