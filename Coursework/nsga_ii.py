import random
from selection import tournament_selection, roulette_wheel_selection, rank_based_selection
from crossover import single_point_crossover, two_point_crossover, uniform_crossover
from mutation import swap_mutation, scramble_mutation, inversion_mutation
from utils import generate_initial_population, calculate_fitness, non_dominated_sorting, calculate_crowding_distance
import time

def nsga_ii(jobs, changeover_costs, population_size, generations, crossover_rate, mutation_rate, selection_operator, crossover_operator, mutation_operator):
    """
    Implements the NSGA-II (Non-dominated Sorting Genetic Algorithm II) for solving the multi-objective scheduling problem.

    Parameters:
    - jobs: list of jobs with their due dates and processing times
    - changeover_costs: matrix of changeover costs between jobs
    - population_size: size of the population
    - generations: number of generations to run the algorithm
    - crossover_rate: probability of crossover
    - mutation_rate: probability of mutation
    - selection_operator: function for selecting parents
    - crossover_operator: function for performing crossover
    - mutation_operator: function for performing mutation

    Returns:
    - pareto_front: list of individuals in the final Pareto front
    - running_time: total running time of the algorithm
    - fitness_history: list of average fitness values for each generation
    """
    # Generate initial population
    population = generate_initial_population(jobs, population_size)
    
    # Start measuring time
    start_time = time.time()
    
    fitness_history = []

    # Main loop for each generation
    for generation in range(generations):
        # Calculate fitness for each individual in the population
        fitnesses = [calculate_fitness(ind, jobs, changeover_costs) for ind in population]
        
        # Non-dominated sorting
        fronts = non_dominated_sorting(population, fitnesses)
        
        # Calculate crowding distance for individuals in each front
        distances = calculate_crowding_distance(fitnesses, fronts)
        
        new_population = []
        for i, front in enumerate(fronts):
            if len(new_population) + len(front) > population_size:
                break
            new_population.extend(front)
        remaining = population_size - len(new_population)
        if remaining > 0:
            sorted_front = sorted(fronts[i], key=lambda x: distances[x], reverse=True)
            new_population.extend(sorted_front[:remaining])
        
        # Selection
        selected_population = selection_operator(new_population, fitnesses)
        
        # Generate offspring through crossover and mutation
        offspring_population = []
        while len(offspring_population) < population_size:
            parents = random.sample(selected_population, 2)
            if random.random() < crossover_rate:
                child1, child2 = crossover_operator(parents[0], parents[1])
            else:
                child1, child2 = parents[0], parents[1]
            
            mutation_operator(child1, mutation_rate)
            mutation_operator(child2, mutation_rate)

            offspring_population.extend([child1, child2])
        
        # Combine the old and new populations and select the next generation
        population = new_population + offspring_population
        
        # Ensure all individuals are valid lists of job indices
        population = [ind for ind in population if isinstance(ind, list) and all(isinstance(x, int) for x in ind)]

        # Record average fitness for the generation
        avg_fitness = sum([calculate_fitness(ind, jobs, changeover_costs) for ind in population]) / len(population)
        fitness_history.append(avg_fitness)
    
    # End measuring time
    end_time = time.time()
    running_time = end_time - start_time
    
    # Calculate fitness for the final population
    fitnesses = [calculate_fitness(ind, jobs, changeover_costs) for ind in population]
    pareto_front = non_dominated_sorting(population, fitnesses)[0]
    
    return [fitnesses[i] for i in pareto_front], running_time, fitness_history
