import matplotlib.pyplot as plt
import pandas as pd

# Function to plot Pareto fronts
def plot_pareto_fronts(results, title_prefix):
    for name, result in results.items():
        pareto_front_100_df = pd.DataFrame(result['pareto_fronts_100'][0], columns=['Total Tardiness', 'Changeover Cost'])
        pareto_front_50_df = pd.DataFrame(result['pareto_fronts_50'][0], columns=['Total Tardiness', 'Changeover Cost'])

        # Plot Pareto Front for 100 Jobs
        plt.figure(figsize=(10, 5))
        plt.scatter(pareto_front_100_df['Total Tardiness'], pareto_front_100_df['Changeover Cost'], label=f'{name}')
        plt.title(f'{title_prefix} - {name} - 100 Jobs')
        plt.xlabel('Total Tardiness (minutes)')
        plt.ylabel('Changeover Cost (pounds)')
        plt.legend()
        plt.show()

        # Plot Pareto Front for 50 Jobs
        plt.figure(figsize=(10, 5))
        plt.scatter(pareto_front_50_df['Total Tardiness'], pareto_front_50_df['Changeover Cost'], label=f'{name}')
        plt.title(f'{title_prefix} - {name} - 50 Jobs')
        plt.xlabel('Total Tardiness (minutes)')
        plt.ylabel('Changeover Cost (pounds)')
        plt.legend()
        plt.show()

# Function to plot evolution of fitness over generations
def plot_fitness_evolution(fitness_evolution, title):
    generations = range(len(fitness_evolution))

    plt.figure(figsize=(10, 5))
    plt.plot(generations, fitness_evolution, marker='o')
    plt.title(f'{title} - Evolution of Average Fitness')
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.grid(True)
    plt.show()