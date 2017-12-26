import math
import random
import numpy as np
import pygame

class Particle
    def __init__(self, n, m, v)
        self.position = np.random.randint(0, n-1), np.random.randint(0, m-1)
        self.momentum = np.random.randn(), np.random.randn() 
        self.mass = 1
        self.collision_radius = 0.1

    def collide(self, particle):
        pass

    def move(self):
        for coord in self.position:
            coord += (self.momentum / self.mass)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.position[0], self.position[1]), 1)

class Board:
    def __init__(self, screen, n, m):
        pass

def main():
    pass

if __name__ == "__main__":
    main()
