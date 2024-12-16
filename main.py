import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init() # Init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    updateble = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() #ADDED
    shots = pygame.sprite.Group()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    Asteroid.containers = (asteroids, updateble, drawable) #ADDED
    Shot.containers = (shots, updateble, drawable)
    AsteroidField.containers = updateble #ADDED
    Player.containers = (updateble, drawable)
    asteroidfild = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        for update in updateble:
            update.update(dt)

        

        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                asteroid.shooted(shot)



        screen.fill((0,0,0))
        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        # 60FPS
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
