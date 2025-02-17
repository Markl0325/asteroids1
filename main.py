import pygame

from constants import *

from player import *


def main():
    #start pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Player Location
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #player
    player = Player(x, y)
    
    #game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fill screen
        screen.fill((0, 0, 0))

        #Draw player
        player.draw(screen)

        #update display
        pygame.display.flip()
        
        #frame rate
        dt = clock.tick(60) / 1000



print("Starting asteroids!")
print (f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()


