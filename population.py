import numpy as np
import random

nine = 9
three = 3
with open("puzzle.txt", "r") as f:
    a = f.read().split()
    puzzle = [[] for j in range(nine)]
    for i in range(nine):
        for j in range(nine):
            puzzle[(i//three)*three + j//three].append(0 if a[i][j] == '.' else int(a[i][j]))

class Board:
    # a is the board
    # fit = fitness level

    def __init__(self):
        a = [[i for i in range(1, nine + 1)] for j in range(1, nine + 1)]
        for row in a:
            random.shuffle(row)
        self.a = np.array(a)

    def dups_row(self):
        res = 0
        for group in range(three):
            for row in range(three):
                s = set(np.ndarray.flatten(self.a[group*three : group*three+three, row*three:row*three+three]))
                res += nine - len(s)
        return res

    def dups_col(self):
        res = 0
        for group in range(three):
            for col in range(three):
                s = set(np.ndarray.flatten(self.a[group : : three, col: : three]))
                res += nine-len(s)
        return res
    def not_innit_nums(self):
        res = 0
        for i in range(nine):
            for j in range(nine):
                if puzzle[i][j] and self.a[i][j] != puzzle[i][j]: res += 10
        return res

    def fitness(self):
        self.fit= self.dups_row() + self.dups_col() + self.not_innit_nums()

    def __getitem__(self, item):
        return self.a[item]
    def __setitem__(self, key, value):
        self.a[key] = value
    def __lt__(self, other):
        return self.fit < other.fit

    def __str__(self):
        res = ""
        for group in range(three):
            for row in range(three):
                for i in np.ndarray.flatten(self.a[group*three : group*three+three, row*three:row*three+three]):
                    res += str(i) + " "
                res += "\n"
        return res


class Population:
    # a population of Sudoku boards
    def __init__(self, pop_size=100):
        self.pop_size = pop_size
        self.pop = [Board() for i in range(pop_size)]
        self.fit_func = lambda x : x.fit

    def evaluate(self):
        # fitness val stored in each member
        s = 0
        best = nine*nine*nine
        for i in self.pop:
            i.fitness()
            s += i.fit
            best = min(best, i.fit)
        self.best_fitness_val = best
        self.avg_fitness_val = s / self.pop_size

    def select_mating_pool(self, num_parents):
        self.pop.sort()
        self.parents = []
        for i in range(num_parents):
            p = min(random.sample(range(self.pop_size), 5))
            self.parents.append(self.pop[p])


    def crossover(self, a, b)->Board:
        k = np.random.choice([i for i in range(nine)], random.randint(1, 8))
        res = Board()
        for i in range(nine):
            if i in k:
                res[i] = a[i]
            else:
                res[i] = b[i]
        return res

    def mutate(self, a):
        t = random.randint(0, nine-1)
        x, y = random.randint(0, nine-1), random.randint(0, nine-1)
        a[t, x], a[t, y] = a[t, y], a[t, x]

    def breed_new_pop(self, mutation_rate):
        new_pop = []
        for i in range(self.pop_size):
            child = self.crossover(self.parents[i%len(self.parents)], self.parents[(i+1)%len(self.parents)])
            if random.random() <= mutation_rate:
                self.mutate(child)
            new_pop.append(child)
        self.pop = new_pop
