import random

def single_point_crossover(parent1, parent2):
    """
    Perform single-point crossover between two parents to produce two offspring.

    Parameters:
    - parent1: The first parent (list of job indices).
    - parent2: The second parent (list of job indices).

    Returns:
    - child1: The first offspring (list of job indices).
    - child2: The second offspring (list of job indices).
    """
    # Determine the crossover point
    crossover_point = random.randint(1, len(parent1) - 1)
    
    # Create offspring by combining segments from both parents
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    return child1, child2

def two_point_crossover(parent1, parent2):
    """
    Perform two-point crossover between two parents to produce two offspring.

    Parameters:
    - parent1: A list containing all jobs id
    - parent2: Alist containing all jobs id.

    Returns:
    - child1: First offspring containing all jobs id
    - child2: Second offspring containing all jobs id
    """
    # Determine two crossover points
    crossover_point_one = random.randint(1, len(parent1) - 2)
    crossover_point_two = random.randint(crossover_point_one + 1, len(parent1) - 1)
    
    # Create offspring by combining segments from both parents
    child1 = parent1[:crossover_point_one] + parent2[crossover_point_one:crossover_point_two] + parent1[crossover_point_two:]
    child2 = parent2[:crossover_point_one] + parent1[crossover_point_one:crossover_point_two] + parent2[crossover_point_two:]
    
    return child1, child2

def uniform_crossover(parent1, parent2):
    """
    Perform uniform crossover between two parents to produce two offspring.

     Parameters:
    - parent1: A list containing all jobs id
    - parent2: Alist containing all jobs id.

    Returns:
    - child1: First offspring containing all jobs id
    - child2: Second offspring containing all jobs id
    """
    child1 = child2 = []
    
    # Perform uniform crossover by randomly selecting genes from each parent
    for gene1, gene2 in zip(parent1, parent2):
        if random.random() < 0.5:
            child1.append(gene1)
            child2.append(gene2)
        else:
            child1.append(gene2)
            child2.append(gene1)
    
    return child1, child2
