import random

def generate_initial_population(jobs, population_size):
    population = []
    for _ in range(population_size):
        individual = list(range(len(jobs)))
        random.shuffle(individual)
        population.append(individual)
    return population

def calculate_fitness(schedule, jobs, changeover_costs):
    total_tardiness = 0
    total_changeover_cost = 0
    current_time = 0

    for i in range(len(schedule)):
        job_id = schedule[i]
        due_date, processing_time = jobs[job_id]
        current_time += processing_time
        tardiness = max(0, current_time - due_date)
        total_tardiness += tardiness
        
        if i == 0:
            total_changeover_cost += changeover_costs[0][job_id]
        else:
            previous_job_id = schedule[i - 1]
            total_changeover_cost += changeover_costs[previous_job_id][job_id]
    
    return total_tardiness, total_changeover_cost

def non_dominated_sorting(population, fitnesses):
    S = [[] for _ in range(len(population))]
    front = [[]]
    n = [0] * len(population)
    rank = [0] * len(population)

    for p in range(len(population)):
        S[p] = []
        n[p] = 0
        for q in range(len(population)):
            if pareto_dominates(fitnesses[p], fitnesses[q]):
                S[p].append(q)
            elif pareto_dominates(fitnesses[q], fitnesses[p]):
                n[p] += 1
        if n[p] == 0:
            rank[p] = 0
            front[0].append(p)

    i = 0
    while len(front[i]) > 0:
        Q = []
        for p in front[i]:
            for q in S[p]:
                n[q] -= 1
                if n[q] == 0:
                    rank[q] = i + 1
                    Q.append(q)
        i += 1
        front.append(Q)
    front.pop(-1)
    return front

# Fixing the calculate_crowding_distance function
def calculate_crowding_distance(fitnesses, front):
    distance = [0] * len(fitnesses)
    for i in range(len(fitnesses[0])):
        sorted_fitnesses = sorted(enumerate(fitnesses), key=lambda x: x[1][i])
        distance[sorted_fitnesses[0][0]] = float('inf')
        distance[sorted_fitnesses[-1][0]] = float('inf')
        
        max_value = max(fitnesses, key=lambda x: x[i])[i]
        min_value = min(fitnesses, key=lambda x: x[i])[i]
        if max_value == min_value:
            continue  # Avoid division by zero

        range_value = max_value - min_value
        if range_value == 0:
            range_value = 1  # To avoid division by zero

        for j in range(1, len(sorted_fitnesses) - 1):
            distance[sorted_fitnesses[j][0]] += (sorted_fitnesses[j+1][1][i] - sorted_fitnesses[j-1][1][i]) / range_value
    return distance



def pareto_dominates(a, b):
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))

def read_and_parse_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    jobs = []
    changeover_costs = []
    reading_jobs = False
    reading_changeover = False

    for line in lines:
        line = line.strip().replace(',', ' ')
        if line == "@jobs":
            reading_jobs = True
            reading_changeover = False
            continue
        elif line == "@changeover":
            reading_jobs = False
            reading_changeover = True
            continue
        
        if reading_jobs:
            if line != "0 0":  # Skip the reference point
                try:
                    job = tuple(map(int, line.split()))
                    if len(job) == 2:
                        jobs.append(job)
                    else:
                        print(f"Skipping invalid job line: {line}")
                except ValueError:
                    print(f"Skipping invalid job line: {line}")
        elif reading_changeover:
            try:
                changeover_costs.append(list(map(int, line.split())))
            except ValueError:
                print(f"Skipping invalid changeover line: {line}")
    
    return jobs, changeover_costs