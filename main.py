import pygame
import sys
from constants import *
from logger import log_state, log_event
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() #pygame object to track time
    dt = 0
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    
    while True:
        log_state()
        #exits when window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        
        #checks collisions for each asteroids with player and shots
        for i in asteroids:
            if i.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if i.collides_with(s):
                    log_event("asteroid_shot")
                    i.split(asteroid_field)
                    s.kill()
        
        #draws everything onto the black screen
        for i in drawable:
            i.draw(screen)
        
        pygame.display.flip()
        
        #returns time passed since last tick in seconds, MAX_FPS limits the maximum FPS to the set constant
        dt = clock.tick(MAX_FPS) / 1000


if __name__ == "__main__":
    main()
