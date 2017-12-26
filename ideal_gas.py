import math
import random
import numpy as np
import pygame

dot = lambda x, y: sum([x[i]*y[i] for i in range(2)])

class Particle
    def __init__(self, n, m, v)
        self.position = np.array([np.random.randint(0, n-1), np.random.randint(0, m-1)])
        self.velocity = np.array([np.random.randn(), np.random.randn()])
        self.mass = 1
        self.collision_radius = 0.1

    def collide(self, particle):
        self.velocity = self.velocity - np.dot(self.velocity - particle.velocity, self.position - particle.position)/np.dot(self.position-particle.position, self.position-particle.position)*(self.position-particle.position)
        particle.velocity = position.velocity - np.dot(-self.velocity + particle.velocity, -self.position + particle.position)/np.dot(-self.position+particle.position, _self.position+particle.position)*(-self.position+particle.position)
        pass

    def move(self):
        for i in range(2):
            self.position[i] += self.velocity[i]

    def bounce(self, axis):
        self.velocity[axis] *=-1
        
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.position[0], self.position[1]), 1)

class Board:
    def __init__(self, screen, n, m):
        self.n = n
        self.m = m
        self.particles = [Particle(self.n, self.m, 5) for i in range(100)]
        self.screen = screen

    def draw(self)
        self.screen.fill((255, 255, 255))
        for p in self.particles:
            p.draw(self.screen)
        pass

    def step(self):
        for p in self.particles:
            p.move()
            #boundry check
            if p.position[0] <= 0 or p.position[0] >= self.n:
                p.bounce[0]
            if p.position[1] <= 0 or p.position[1] >= self.m:
                p.bounce[1]

    def iterate(self):
        self.step()
        self.draw()
        # boundry / collision check
        for p1 in self.particles:
            for p2 in self.particles:
                if p1 is not p2:
                    if np.dot(p1.position - p2.position) <=1:
                        p1.collide(p2)
        

def main():
    pygame.init()
    screen = pygame.display.set_mode(300, 300)
    b = Board(300, 300, screen)
    while 1:
        b.iterate()
        pygame.display.flip()

if __name__ == "__main__":
    main()
