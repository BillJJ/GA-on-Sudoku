from genetic_algo import run
from matplotlib import pyplot as plt

pop_size = 100
num_parents = 25
mutation_rate = 0.35

trials_per_average = 5

pop_size = []
results = []
plt.xlabel('Population Size')
plt.ylabel('Average solve times (s)')

for i in range(25, 101, 25):
    pop_size.append(i)

    tries = [run(i, i//4, mutation_rate) for j in range(trials_per_average)]
    results.append(sum(tries) / len(tries))
    print("Pop_size =",i, ", results =",results[-1])
    plt.plot(pop_size, results)
    plt.pause(0.01)