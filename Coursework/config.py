from nsga_ii import tournament_selection, roulette_wheel_selection, rank_based_selection, single_point_crossover, two_point_crossover, uniform_crossover, swap_mutation, scramble_mutation, inversion_mutation

# Define the key configurations
key_configurations = [
    ('tournament', 100, 'single_point', 'swap', 200),  # Baseline Configuration
    ('roulette', 100, 'single_point', 'swap', 200),   # Different Selection Operators
    ('rank', 100, 'single_point', 'swap', 200),       # Different Selection Operators
    ('tournament', 50, 'single_point', 'swap', 200),  # Different Population Sizes
    ('tournament', 200, 'single_point', 'swap', 200), # Different Population Sizes
    ('tournament', 100, 'two_point', 'scramble', 200),# Different Reproduction Operators
    ('tournament', 100, 'uniform', 'inversion', 200), # Different Reproduction Operators
    ('rank', 150, 'two_point', 'scramble', 200)       # Combination of Different Parameters
]

# Define a function to convert operator names to functions
def get_operator_function(operator_name):
    operators = {
        'tournament': tournament_selection,
        'roulette': roulette_wheel_selection,
        'rank': rank_based_selection,
        'single_point': single_point_crossover,
        'two_point': two_point_crossover,
        'uniform': uniform_crossover,
        'swap': swap_mutation,
        'scramble': scramble_mutation,
        'inversion': inversion_mutation
    }
    return operators[operator_name]

# Fixed crossover and mutation rates
crossover_rate = 0.8
mutation_rate = 0.1

# Number of trials to average results
num_trials = 5
