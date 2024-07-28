import random

def swap_mutation(individual, mutation_rate):
  
    # Iterate over each gene in the individual
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            # Select a random gene to swap with
            j = random.randint(0, len(individual) - 1)
            # Swap the genes
            individual[i], individual[j] = individual[j], individual[i]

def scramble_mutation(individual, mutation_rate):
  
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
    
    if random.random() < mutation_rate:
        # Select two random points to define the subset
        start = random.randint(0, len(individual) - 2)
        end = random.randint(start + 1, len(individual) - 1)
        # Invert the order of the genes in the subset
        subset = individual[start:end]
        subset.reverse()
        # Replace the original subset with the inverted subset
        individual[start:end] = subset
