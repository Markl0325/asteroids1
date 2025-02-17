#imports pygame
import pygame

#imports circleshape
from circleshape import CircleShape

#imports player radius
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED




class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    #draw player
    def draw(self, screen):
        pygame.draw.polygon(
            screen, 
            "white",
            self.triangle(),
            2
        )

    #player rotation
    def rotate(self, dt):
        rotation = PLAYER_TURN_SPEED * dt
        self.rotation = self.rotation + rotation
        
        
    # update location
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)


        if keys[pygame.K_d]:
            self.rotate(+dt)
 