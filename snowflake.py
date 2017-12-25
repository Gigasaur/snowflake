import math
import random
import pygame

class Particle:
    def __init__(self, n, m):
        self.x = random.randint(0, n)
        self.y = random.randint(0, m)
        self.free = 1

    def move(self):
        self.x = (self.x + self.free * random.randint(-1, 1))
        self.y = (self.y + self.free * random.randint(-1, 1))

    def draw(self, screen):
        rect = pygame.Rect(int(4*self.x), int(4*self.y), 4, 4)
        pygame.draw.rect(screen, (0, 0, 0), rect)

class Board:
    def __init__(self, n, m, N, screen):
        self.n = n
        self.m = m
        self.screen = screen
        self.particles = [Particle(n, m) for i in range(N)]
        self.particles[0].free = 0

    def draw(self):
        self.screen.fill((255, 255, 255))
        for p in self.particles:
            p.draw(self.screen)

    def step(self):
        for p in self.particles:
            p.move()
            # boundary check
            p.x %= self.n
            p.y %= self.m

    def print_state(self):
        for p in self.particles:
            print("{}, {}".format(p.x, p.y))

    def iterate(self):
        self.step()
        self.draw()
        #stuck check
        for p1 in self.particles:
            for p2 in self.particles:
                if p1 is not p2:
                    if ((p1.x-p2.x)%(self.n))**2 + ((p1.y-p2.y)%(self.m))**2 == 1 \
                       and (not p1.free or not p2.free):
                        p1.free = 0
                        p2.free = 0
                    

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((600, 200)) 

    b = Board(150, 50, 2000, screen)
    b.print_state()
    while 1:
        b.iterate()
        pygame.display.flip()
    print("")
    b.print_state()

if __name__ == "__main__":
    main()
