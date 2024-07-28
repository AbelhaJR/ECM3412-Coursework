import random

def swap_mutation(individual, mutation_rate):
    """
    Performs swap mutation on an individual. Each gene has a probability of being swapped
    with another gene in the individual.
    
    Parameters:
    - individual: list of integers representing the individual's genes
    - mutation_rate: probability of each gene being swapped
    
    Returns:
    - mutated_individual: mutated individual
    """
    # Iterate over each gene in the individual
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            # Select a random gene to swap with
            j = random.randint(0, len(individual) - 1)
            # Swap the genes
            individual[i], individual[j] = individual[j], individual[i]

def scramble_mutation(individual, mutation_rate):
    """
    Performs scramble mutation on an individual. A subset of genes is randomly selected
    and shuffled.
    
    Parameters:
    - individual: list of integers representing the individual's genes
    - mutation_rate: probability of the individual undergoing scramble mutation
    
    Returns:
    - mutated_individual: mutated individual
    """
    if random.random() < mutation_rate:
        # Select two random points to define the subset
        start = random.randint(0, len(individual) - 2)
        end = random.randint(start + 1, len(individual) - 1)
        # Scramble the subset of genes
        subset = individual[start:end]
        random.shuffle(subset)
        # Replace the original subset with the scrambled subset
        individual[start:end] = subset

def inversion_mutation(individual, mutation_rate):
    """
    Performs inversion mutation on an individual. A subset of genes is randomly selected
    and the order of the genes in this subset is reversed.
    
    Parameters:
    - individual: list of integers representing the individual's genes
    - mutation_rate: probability of the individual undergoing inversion mutation
    
    Returns:
    - mutated_individual: mutated individual
    """
    if random.random() < mutation_rate:
        # Select two random points to define the subset
        start = random.randint(0, len(individual) - 2)
        end = random.randint(start + 1, len(individual) - 1)
        # Invert the order of the genes in the subset
        subset = individual[start:end]
        subset.reverse()
        # Replace the original subset with the inverted subset
        individual[start:end] = subset
