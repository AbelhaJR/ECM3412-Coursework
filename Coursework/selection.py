import random

def tournament_selection(population, fitnesses, tournament_size=2):

    selected_individuals = []
    
    # Perform tournament for each individual to be selected
    for _ in range(len(population)):
        # Randomly select individuals to participate in the tournament
        tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
        # Select the individual with the best fitness from the tournament
        winner = min(tournament, key=lambda x: x[1])
        selected_individuals.append(winner[0])
    
    return selected_individuals

def roulette_wheel_selection(population, fitnesses):
    """
    Performs roulette wheel selection on the population. Selects individuals based on their 
    relative fitness, giving higher chances to individuals with better fitness.
    
    Parameters:
    - population: list of individuals in the population
    - fitnesses: list of fitness values corresponding to the individuals
    
    Returns:
    - selected_individuals: list of selected individuals
    """
    # Calculate total fitness and relative probabilities
    total_fitness = sum(fitnesses)
    selection_probabilities = [f / total_fitness for f in fitnesses]
    
    selected_individuals = []
    
    # Perform selection for each individual to be selected
    for _ in range(len(population)):
        # Select individual based on their selection probability
        selected_index = random.choices(range(len(population)), weights=selection_probabilities, k=1)[0]
        selected_individuals.append(population[selected_index])
    
    return selected_individuals

def rank_based_selection(population, fitnesses):
    """
    Performs rank-based selection on the population. Selects individuals based on their rank
    rather than their absolute fitness values.
    
    Parameters:
    - population: list of individuals in the population
    - fitnesses: list of fitness values corresponding to the individuals
    
    Returns:
    - selected_individuals: list of selected individuals
    """
    # Rank individuals based on their fitness
    sorted_population = sorted(zip(population, fitnesses), key=lambda x: x[1])
    ranks = list(range(1, len(population) + 1))
    
    # Calculate selection probabilities based on rank
    total_rank = sum(ranks)
    selection_probabilities = [r / total_rank for r in ranks]
    
    selected_individuals = []
    
    # Perform selection for each individual to be selected
    for _ in range(len(population)):
        # Select individual based on their selection probability
        selected_index = random.choices(range(len(population)), weights=selection_probabilities, k=1)[0]
        selected_individuals.append(sorted_population[selected_index][0])
    
    return selected_individuals
