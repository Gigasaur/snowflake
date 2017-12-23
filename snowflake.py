import random

class Particle:
    def __init__(n, m):
        self.x = random.randint(0, n)
        self.y = random.randint(0, m)

    def move(self):
        self.x = (self.x + random.randint(-1, 1))%n
        self.y = (self.y + random.randint(-1, 1))%m

    def draw(self):
        pass

class Board:
    def __init__(n, m, N):
        pass
    def draw(self):
        pass
    def step(self):
        pass

def main():
    b = Board(2048, 2048, 2048)
    while(b):
        b.step()
    pass

if __name__ == "__main__":
    main()
