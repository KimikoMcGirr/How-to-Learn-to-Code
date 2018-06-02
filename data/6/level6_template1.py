import random
import sys

BOARD = 20


class Food:

    def __init__(self):
        self.x = random.randint(0, BOARD)
        self.y = random.randint(0, BOARD)
        self.mass = 10

    def degrade(self):
        if random.choice((True, False)):
            self.mass -= 1


class Virus:

    def __init__(self, x=None, y=None):
        self.x = x if x is not None else random.randint(0, BOARD)
        self.y = y if x is not None else random.randint(0, BOARD)
        self.mass = 10

    def defense(self):
        return self.mass ** .5 / 20

    def move(self):
        dx = random.choice((-1, 0, 1))
        if 0 <= self.x + dx <= BOARD:
            self.x += dx
        dy = random.choice((-1, 0, 1))
        if 0 <= self.y + dy <= BOARD:
            self.y += dy

    def check_eating(self, food_ls):
        new_food_ls = []
        for food in food_ls:
            if self.x == food.x and self.y == food.y:
                self.mass += food.mass
            else:
                new_food_ls.append(food)
        return new_food_ls

    def check_dividing(self):
        if self.mass >= 25:
            self.mass = 10
            return Virus(self.x, self.y)


class Macrophage:

    def __init__(self):
        self.x = random.randint(0, BOARD)
        self.y = random.randint(0, BOARD)
        self.history = 0
        self.attack = .35

    def try_kill(self, virus):
        success = self.attack + self.history - virus.defense()
        if success <= 0:
            return False

        failure = 1 - success
        kill = random.choices((True, False), (success, failure))[0]
        if kill:
            self.history += .05
        return kill

    def check_killing(self, virus_ls):
        new_virus_ls = []
        for virus in virus_ls:
            if self.x == virus.x and self.y == virus.y:
                kill = self.try_kill(virus)
                if not kill:
                    new_virus_ls.append(virus)
            else:
                new_virus_ls.append(virus)
        return new_virus_ls

    def move_straight(self, virus_ls):
        self.attack = .35
        x_y = random.choice(('x', 'y'))
        pos_neg = random.choice((-1, 1))
        for i in range(5):
            if 0 <= vars(self)[x_y] + pos_neg <= BOARD:
                if x_y == 'x':
                    self.x += pos_neg
                else:
                    self.y += pos_neg
                virus_ls = self.check_killing(virus_ls)
            else:
                break
        return virus_ls

    def move_random(self, virus_ls):
        self.attack = .5
        for i in range(3):
            x_y = random.choice(('x', 'y'))
            pos_neg = random.choice((-1, 0, 1))
            if 0 <= vars(self)[x_y] + pos_neg <= BOARD:
                if x_y == 'x':
                    self.x += pos_neg
                else:
                    self.y += pos_neg
                virus_ls = self.check_killing(virus_ls)
        return virus_ls

    def move_and_kill(self, virus_ls):
        current_move = random.choice((self.move_straight, self.move_random))
        virus_ls = current_move(virus_ls)
        return virus_ls


class Simulation:

    def __init__(self, n_food, n_viruses, n_macs):
        self.food_ls = [Food() for i in range(n_food)]
        self.virus_ls = [Virus() for i in range(n_viruses)]
        self.mac_ls = [Macrophage() for i in range(n_macs)]

    def update_viruses(self):
        new_viruses = []
        for v in self.virus_ls:
            v.move()
            self.food_ls = v.check_eating(self.food_ls)
            new_virus = v.check_dividing()
            if new_virus is not None:
                new_viruses.append(new_virus)
        self.virus_ls += new_viruses

    def update_macs(self):
        for m in self.mac_ls:
            self.virus_ls = m.move_and_kill(self.virus_ls)

    def update_food(self):
        remaining_food = []
        for food in self.food_ls:
            food.degrade()
            if food.mass > 0:
                remaining_food.append(food)
        self.food_ls = remaining_food
        self.food_ls += [Food() for i in range(40)]

    def run(self):
        virus_hits_100 = None
        virus_hits_200 = None
        for step in range(100):
            self.update_viruses()
            self.update_macs()
            self.update_food()
            if len(self.virus_ls) > 10000 and virus_hits_100 is None:
                virus_hits_100 = step
            elif len(self.virus_ls) > 20000:
                virus_hits_200 = step
                break
            #print(step, len(self.food_ls), len(self.virus_ls))

        return virus_hits_100, virus_hits_200


if __name__ == '__main__':
    random.seed(sys.argv[4])
    sim = Simulation(int(sys.argv[1]),
                     int(sys.argv[2]),
                     int(sys.argv[3]))
    print(sim.run())
