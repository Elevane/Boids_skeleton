from math import *
import pygame, sys

import pygame, sys, random

SECONDS = 60
height, width = 800, 600
BLACK = (0, 0, 0)
RED = (0, 0, 255)
SPEED = 5
NUMBEROFBOIDS = 15
class Boid:
    def __init__(self):
        self.x = 150
        self.y = 150
        self. dir = pygame.Vector2()
        self.angle = random.randint(1,360)
        self.timing = random.randint(0, 4)
        self.time = 0
        self.seconds = 0
        self.speed = 5
    def draw(self, screen):
        self.update()
        pygame.draw.circle(screen, RED, (self.dir), 5, 5)
    
    def update(self):
        if self.timing  <= 0:
            self.angle = random.randint(1,360)
            self.reset_timing()

        if self.x > width or self.x < 0 or self.y > height or self.y < 0:
            self.reset_timing()
            if self.angle > 0 :
                self.angle = self.angle - 180
            else :
                self.angle = self.angle + 180
        if self.seconds >= self.timing:
            self.timing = self.timing - 1

        self.time = self.time + 1
        if self.time > SECONDS:
            self.seconds = int(self.time / SECONDS)
        self.compute_direction()
        

    def compute_direction(self):
        ##print(cos(self.angle) + self.x, sin(self.angle) + self.y)
        self.x += sin(self.angle)
        self.y += cos(self.angle)
        self.dir =  self.x + self.speed,  self.y + self.speed

    def reset_timing(self):
        
        self.timing = random.randint(1, 4)
        self.seconds = 0
        self.time = 0

class App:
    def __init__(self, boids):
        self.screen =  pygame.display.set_mode((width,height))
        self.boids = boids
        self.clock = pygame.time.Clock()

    def draw(self):
        for boid in self.boids:
            boid.draw(self.screen)



    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def update(self):
        pygame.display.update()
        self.screen.fill(BLACK)

    def run(self):
        while True:
            self.clock.tick(60)
            self.update()
            self.event()
            self.draw()

def create_boids(num):
    boids = []
    for n in range(num):
        b = Boid()
        boids.append(b)
    return boids
if __name__ == "__main__":
    boids = create_boids(NUMBEROFBOIDS)
    app = App(boids)
    
    app.run()