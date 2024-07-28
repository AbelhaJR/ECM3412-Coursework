import random

def single_point_crossover(parent1, parent2):
    if not isinstance(parent1, list) or not isinstance(parent2, list):
        print(f"Error: parent1 type: {type(parent1)}, parent2 type: {type(parent2)}")
    size = len(parent1)
    point = random.randint(1, size - 1)
    child1 = parent1[:point] + [gene for gene in parent2 if gene not in parent1[:point]]
    child2 = parent2[:point] + [gene for gene in parent1 if gene not in parent2[:point]]
    return child1, child2

def two_point_crossover(parent1, parent2):
    if not isinstance(parent1, list) or not isinstance(parent2, list):
        print(f"Error: parent1 type: {type(parent1)}, parent2 type: {type(parent2)}")
    size = len(parent1)
    point1, point2 = sorted(random.sample(range(size), 2))
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2

def uniform_crossover(parent1, parent2):
    if not isinstance(parent1, list) or not isinstance(parent2, list):
        print(f"Error: parent1 type: {type(parent1)}, parent2 type: {type(parent2)}")
    size = len(parent1)
    child1 = []
    child2 = []
    for i in range(size):
        if random.random() < 0.5:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])
    return child1, child2
