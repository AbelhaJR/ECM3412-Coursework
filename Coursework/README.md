# Job Scheduling Optimization with NSGA-II

## Overview

This project implements a multi-objective optimization algorithm using the NSGA-II (Non-dominated Sorting Genetic Algorithm II) to solve a job scheduling problem. The objectives are to minimize the total tardiness and the sum of changeover costs in the schedule. The project explores different configurations of the genetic algorithm to determine the optimal parameters.

## Directory Structure

project_root/
|-- datasets/
| |-- SMTTCC1problem
| |-- SMTTCC2problem
|-- main.py
|-- nsga_ii.py
|-- selection.py
|-- crossover.py
|-- mutation.py
|-- utils.py
|-- plotting.py
|-- config.py
|-- README.md


## Files and Their Purpose

- **datasets/SMTTCC1problem**: Dataset for the job scheduling problem with 100 jobs.
- **datasets/SMTTCC2problem**: Dataset for the job scheduling problem with 50 jobs.
- **main.py**: The main script to run the experiments and generate results.
- **nsga_ii.py**: Implementation of the NSGA-II algorithm.
- **selection.py**: Selection operators for the genetic algorithm.
- **crossover.py**: Crossover operators for the genetic algorithm.
- **mutation.py**: Mutation operators for the genetic algorithm.
- **utils.py**: Utility functions for data parsing and fitness calculation.
- **plotting.py**: Functions for plotting Pareto fronts and fitness evolution.
- **config.py**: Configuration file containing experiment parameters and settings.
- **README.md**: This readme file.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Required Python packages: `pandas`, `matplotlib`

You can install the necessary packages using:
pip install pandas matplotlib


## Running the Experiments

To run the experiments and generate results, execute the following command:
python main.py

This will read the datasets, run the NSGA-II algorithm with different configurations, and produce plots of the Pareto fronts and fitness evolution.

## Configuration
The config.py file contains the configurations for the experiments. You can adjust the parameters such as population size, mutation rate, selection operator, crossover operator, and the number of generations.

## Output
The output of the experiments includes:

Pareto Fronts: Scatter plots showing the trade-offs between total tardiness and changeover cost for different configurations.
Fitness Evolution: Line plots showing the evolution of the average fitness over generations for different configurations.
Summary Table: A summary table displaying the average performance metrics for each configuration.
Detailed Descriptions

## NSGA-II Algorithm
The NSGA-II algorithm is implemented in nsga_ii.py. It includes functions for non-dominated sorting, crowding distance calculation, selection, crossover, and mutation operations.

## Selection Operators
Implemented in selection.py:

Tournament Selection: Selects the best individual out of a randomly chosen subset.
Roulette Wheel Selection: Selects individuals based on their fitness proportion.
Rank-Based Selection: Selects individuals based on their rank in the population.

## Crossover Operators
Implemented in crossover.py:

Single-Point Crossover: Splits parents at a single point and exchanges segments.
Two-Point Crossover: Splits parents at two points and exchanges middle segments.
Uniform Crossover: Randomly exchanges genes between parents.

## Mutation Operators
Implemented in mutation.py:

Swap Mutation: Swaps two genes in the individual.
Scramble Mutation: Randomly scrambles a subset of genes.
Inversion Mutation: Reverses the order of a subset of genes.

## Utility Functions
Implemented in utils.py:

read_and_parse_dataset: Reads and parses the job scheduling datasets.
calculate_fitness: Calculates the fitness of an individual based on total tardiness and changeover cost.
Plotting Functions
Implemented in plotting.py:

plot_pareto_fronts: Plots the Pareto fronts for different configurations.
plot_fitness_evolution: Plots the fitness evolution over generations.