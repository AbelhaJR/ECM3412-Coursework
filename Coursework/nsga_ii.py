import random
from selection import tournament_selection, roulette_wheel_selection, rank_based_selection
from crossover import single_point_crossover, two_point_crossover, uniform_crossover
from mutation import swap_mutation, scramble_mutation, inversion_mutation
from utils import generate_initial_population, calculate_fitness, non_dominated_sorting, calculate_crowding_distance
import time

def nsga_ii(jobs, changeover_costs, population_size, generations, crossover_rate, mutation_rate, selection_operator, crossover_operator, mutation_operator):
    population = generate_initial_population(jobs, population_size)
    fitness_evolution = []

    start_time = time.time()  # Start measuring time
    
    for generation in range(generations):
        # Calculate fitness for each individual
        fitnesses = [calculate_fitness(ind, jobs, changeover_costs) for ind in population]
        
        # Record average fitness for this generation
        avg_fitness = sum(sum(fit) for fit in fitnesses) / len(fitnesses)
        fitness_evolution.append(avg_fitness)
        
        # Non-dominated sorting
        fronts = non_dominated_sorting(population, fitnesses)
        
        # Calculate crowding distance
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
        if selection_operator == 'tournament':
            selected_population = tournament_selection(new_population, fitnesses)
        elif selection_operator == 'roulette':
            selected_population = roulette_wheel_selection(new_population, fitnesses)
        elif selection_operator == 'rank':
            selected_population = rank_based_selection(new_population, fitnesses)
        else:
            selected_population = new_population  # Default to no selection

        # Generate offspring
        offspring_population = []
        while len(offspring_population) < population_size:
            parents = random.sample(selected_population, 2)
            if random.random() < crossover_rate:
                if crossover_operator == 'single_point':
                    child1, child2 = single_point_crossover(population[parents[0]], population[parents[1]])
                elif crossover_operator == 'two_point':
                    child1, child2 = two_point_crossover(population[parents[0]], population[parents[1]])
                elif crossover_operator == 'uniform':
                    child1, child2 = uniform_crossover(population[parents[0]], population[parents[1]])
                else:
                    child1, child2 = population[parents[0]], population[parents[1]]  # Default to no crossover
            else:
                child1, child2 = population[parents[0]], population[parents[1]]  # Default to no crossover

            # Mutation
            if mutation_operator == 'swap':
                swap_mutation(child1, mutation_rate)
                swap_mutation(child2, mutation_rate)
            elif mutation_operator == 'scramble':
                scramble_mutation(child1, mutation_rate)
                scramble_mutation(child2, mutation_rate)
            elif mutation_operator == 'inversion':
                inversion_mutation(child1, mutation_rate)
                inversion_mutation(child2, mutation_rate)

            offspring_population.extend([child1, child2])
        
        population = new_population + offspring_population
        
        # Ensure all individuals are valid lists of job indices
        population = [ind for ind in (new_population + offspring_population) if isinstance(ind, list) and all(isinstance(x, int) for x in ind)]
    
    end_time = time.time()  # End measuring time
    running_time = end_time - start_time  # Calculate running time
    
    fitnesses = [calculate_fitness(ind, jobs, changeover_costs) for ind in population]
    pareto_front = non_dominated_sorting(population, fitnesses)[0]
    return [fitnesses[i] for i in pareto_front], running_time, fitness_evolution
