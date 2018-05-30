import random
import sys

BOARD = 20


class Food:

    def __init__(self):
        self.x = random.randint(0, BOARD)
        self.y = ...
        self.mass = 10

    def degrade(self):
        if random.choice((True, False)):
            self.mass -= 1

class Virus:

    def __init__(self, x=None, y=None):
        self.x = ...
        self.y = ...
        self.mass = 10

    def defense(self):
        return self.mass ** .5 / 20

    def move(self):
        ...

    def check_eating(self, food_ls):
        ...
        return new_food_ls

    def check_dividing(self):
        ...
        return Virus(..., ...)

class Macrophage:

    def __init__(self):
        self.x = random.randint(0, BOARD)
        self.y = ...
        self.history = ...
        self.attack = ...

    def try_kill(self, virus):
        ...
        return kill

    def check_killing(self, virus_ls):
        ...
        return new_virus_ls

    def move_straight(self, virus_ls):
        ...
        return virus_ls

    def move_random(self, virus_ls):
        ...
        return virus_ls

    def move_and_kill(self, virus_ls):
        ...
        return virus_ls


class Simulation:

    def __init__(self, n_food, n_viruses, n_macs):
        self.food_ls = [Food() for i in range(n_food)]
        self.virus_ls = ...
        self.mac_ls = ...

    def update_viruses(self):
        ...

    def update_macs(self):
        ...

    def update_food(self):
        ...

    def run(self):
        ...

        return ..., ...


if __name__ == '__main__':
    results = [Simulation(*map(int, sys.argv[1:])).run() for i in range(50)]
    results100, results200 = zip(*results)
    mean100 = round(np.mean(results100))
    mean200 = round(np.mean(results200))
    results = f'({mean100}, {mean200})'
    print(results)
    with open('results/6.txt', 'w') as outfile:
        outfile.write(results)
