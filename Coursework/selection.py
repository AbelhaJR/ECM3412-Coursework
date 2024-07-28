import random
import numpy as np

def tournament_selection(population, fitnesses, k=2):
    selected = []
    for _ in range(len(population)):
        aspirants = random.sample(list(zip(population, fitnesses)), k)
        selected.append(min(aspirants, key=lambda x: x[1])[0])
    return selected

def roulette_wheel_selection(population, fitnesses):
    total_fitness = sum(1.0 / f[0] for f in fitnesses)
    probabilities = [(1.0 / f[0]) / total_fitness for f in fitnesses]
    selected = []
    for _ in range(len(population)):
        selected.append(population[np.random.choice(len(population), p=probabilities)])
    return selected

def rank_based_selection(population, fitnesses):
    ranks = np.argsort(np.argsort([f[0] for f in fitnesses]))
    total_ranks = sum(ranks)