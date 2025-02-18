import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shots import Shot



def main():
    #start pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable,)

    dt = 0
    asteroid_field = AsteroidField()
    
    # Player Location
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
    #game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #player update
        updatable.update(dt)

        #shot
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            new_shot = player.shoot()
            if new_shot:  # If the shoot method successfully creates a Shot
                shots.add(new_shot)

        #shoot collision
        for shot in shots:
            for asteroid in asteroids:
                distance = (shot.position - asteroid.position).length()
                if distance < (shot.radius + asteroid.radius):
                    asteroid.kill()
                    shot.kill()
            

        #collision check
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                sys.exit()

        #fill screen
        screen.fill((0, 0, 0))

        #Draw player
        for obj in drawable:
            obj.draw(screen)

        #update display
        pygame.display.flip()
        
        #frame rate
        dt = clock.tick(60) / 1000



print("Starting asteroids!")
print (f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()


