import pygame

from constants import *

from player import Player

from asteroid import Asteroid

from asteroidfield import AsteroidField




def main():
    #start pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

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


