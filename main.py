import random

from genetic_algo import run
from matplotlib import pyplot as plt

num_parents = 36
pop_size = 80
mutation_rate = 0.8

trials_per_average = 5

x = []
results = []
plt.xlabel('Run Rate')
plt.ylabel('Time Taken (s)')
plt.title('A few trials')

def trial(a, b, c, d): return sum([run(a, b, c) for i in range(d)]) / d

for i in range(20):
    x.append(i)
    results.append(run(pop_size, num_parents, mutation_rate))
    print("Trial $", i, "results =",results[-1])
    plt.plot(x, results)
    plt.pause(0.01)

plt.show()
