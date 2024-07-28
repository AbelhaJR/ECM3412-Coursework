import random

def swap_mutation(individual, mutation_rate=0.1):
    if not isinstance(individual, list):
        print(f"Error: individual type: {type(individual)}")
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]

def scramble_mutation(individual, mutation_rate=0.1):
    if not isinstance(individual, list):
        print(f"Error: individual type: {type(individual)}")
    if random.random() < mutation_rate:
        start, end = sorted(random.sample(range(len(individual)), 2))
        individual[start:end] = random.sample(individual[start:end], len(individual[start:end]))

def inversion_mutation(individual, mutation_rate=0.1):
    if not isinstance(individual, list):
        print(f"Error: individual type: {type(individual)}")
    if random.random() < mutation_rate:
        start, end = sorted(random.sample(range(len(individual)), 2))
        individual[start:end] = individual[start:end][::-1]
