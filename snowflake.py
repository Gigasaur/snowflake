import random

class Particle:
    def __init__(self, n, m):
        self.x = random.randint(0, n)
        self.y = random.randint(0, m)

    def move(self):
        self.x = (self.x + random.randint(-1, 1))%n
        self.y = (self.y + random.randint(-1, 1))%m

    def draw(self):
        pass

class Board:
    def __init__(self, n, m, N):
        self.particles = [Particle(n, m)]*N

    def draw(self):
        map(lambda x: x.draw(), self.particles)

    def step(self):
        map(lambda x: x.move(), self.particles)

def main():
    b = Board(2048, 2048, 2048)
    for i in range(2048):
        b.step()
    pass

if __name__ == "__main__":
    main()
