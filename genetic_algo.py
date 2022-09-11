import sys
import time

from population import *

print_interval = 50

def print(*s):
    if __name__ != '__main__':
        sys.stdout.write(" ".join(list(map(str, s))) + "\n")

def run(pop_size = 100, num_parents = 25, mutation_rate = 0.35):
    p = Population(pop_size)
    last_best = 0
    run = 0
    restarts = 0
    best_overall = 1000
    start = time.time()
    for t in range(int(1e6)):
        p.evaluate()

        if last_best == p.best_fitness_val: run += 1
        else:
            last_best = p.best_fitness_val
            run = 0
        best_overall = min(best_overall, p.best_fitness_val)
        if t % print_interval == 0:
            print(f"Restart: {restarts} ---- Gen {t} best fitness: {p.best_fitness_val}, avg fitness : {p.avg_fitness_val}")
            if t % (print_interval * 10) == 0:
                p.pop.sort()
                print(p.pop[0])
        if p.best_fitness_val == 0:
            print("FOUND")
            print(p.pop[0])
            break

        p.select_mating_pool(num_parents)
        p.breed_new_pop(mutation_rate)

        if run >= 100:
            print("Stuck for over 100, restarting now", "current best = ",best_overall)
            p = Population(pop_size)
            run = 0
            last_best = 0
            restarts += 1

    duration = round(time.time()-start, 3)
    print(f"Time taken: {duration}")
    return duration
pop_size = 100
num_parents = 25
mutation_rate = 0.35
if __name__ == '__main__':
    run(pop_size, num_parents, mutation_rate)