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
        screen.set_at((self.x, self.y), (255,255,255))

class Board:
    def __init__(self, n, m, N):
        self.n = n
        self.m = m
        self.screen = pygame.display.set_mode((n, m))
        self.particles = [Particle(n, m) for i in range(N)]

    def draw(self):
        self.screen.fill((0,0,0))
        for p in self.particles:
            p.draw(self.screen)
        pygame.display.flip()

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
                    if math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2) == 1:
                        p1.free = 0
                        p2.free = 0

def main():
    
    pygame.init()

    b = Board(10, 10, 20)
    b.print_state()
    while 1:
        b.iterate()
    print("")
    b.print_state()

if __name__ == "__main__":
    main()
