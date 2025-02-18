#imports pygame
import pygame

#imports circleshape
from circleshape import CircleShape

#imports player attributes
from constants import *

from Shots import Shot




class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.rate_limit = 0


    #draw player
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    #player rotation
    def rotate(self, dt):
        rotation = PLAYER_TURN_SPEED * dt
        self.rotation = self.rotation + rotation
        

    #player movement
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    #player shoot
    def shoot(self):
        if self.rate_limit <= 0:
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = direction * PLAYER_SHOOT_SPEED
            self.rate_limit = PLAYER_SHOOT_COOLDOWN
            return Shot(self.position.x, self.position.y, velocity)
        return None       



    # update location
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(+dt)

        if keys[pygame.K_w]:
            self.move(+dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        
    
        
        self.rate_limit = max(0, self.rate_limit -dt)


 