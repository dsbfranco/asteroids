import pygame
import sys
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_WIDTH / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)

        for asteroid  in asteroids:            
            for shot in shots:
                if asteroid.collided(shot):
                    shot.kill()
                    asteroid.kill()
            if asteroid.collided(player):                
                print("Game Over!")
                sys.exit(0)            
        
        screen.fill("black")
        
        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()