import random

class Particle:
    def __init__(self, n, m):
        self.x = random.randint(0, n)
        self.y = random.randint(0, m)

    def move(self):
        self.x = (self.x + random.randint(-1, 1))
        self.y = (self.y + random.randint(-1, 1))

    def draw(self):
        pass

class Board:
    def __init__(self, n, m, N):
        self.n = n
        self.m = m
        self.particles = [Particle(n, m) for i in range(N)]

    def draw(self):
        for p in self.particles:
            p.draw()

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

def main():
    b = Board(10, 10, 5)
    b.print_state()
    for i in range(2048):
        b.iterate()
    print("")
    b.print_state()

if __name__ == "__main__":
    main()
