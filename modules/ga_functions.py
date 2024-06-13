import random
import numpy as np
from .fitness import fitness
from parameters import *


# Selection: Tournament selection
def select(population: list,
           fitnesses: list,
           tournament_size = 5) -> list:
    
    # Select n individuals and choose the best among them
    selected = random.sample(range(len(population)), tournament_size)
    selected_fitnesses = [fitnesses[i] for i in selected]
    return population[selected[np.argmax(selected_fitnesses)]]


# Crossover: Single point crossover
def crossover(parent1: dict,
              parent2: dict) -> tuple:

    # Define the crossover point by random
    child1, child2 = dict(), dict()
    crossover_point = random.randint(1, len(parent1)-1)

    # Breed children accordingly
    for i, (feature_name, _) in enumerate(parent1.items()):
        if i < crossover_point:
            child1[feature_name] = parent1[feature_name]
            child2[feature_name] = parent2[feature_name]
        else:
            child1[feature_name] = parent2[feature_name]
            child2[feature_name] = parent1[feature_name]

    return child1, child2


# Mutation
def mutate(individual: dict,
           dataframe: dict,
           rate: int) -> dict:
    
    # Random mutation
    if random.random() < rate:
        gene_to_mutate = random.choice(list(individual.keys()))

        # Mutate the feature according to the datatype
        if gene_to_mutate in list(dataframe["numerical"].keys()):
            individual[gene_to_mutate] = random.uniform(*dataframe["numerical"][gene_to_mutate])
        else:
            individual[gene_to_mutate] = random.choice(dataframe["categorical"][gene_to_mutate])

    return individual


# Initialize population
def initialize_population(dataframe: dict,
                          n_population: int) -> list:

    # Initialize population variable
    population = []

    # Loop through each individual
    for _ in range(n_population):

        # Initialize individual
        individual = dict()

        # Loop through each data type
        for typename, features in dataframe.items():

            # If data are numerical, draw from U[min, max], else draw a category
            if typename == "numerical":

                # Loop through all numerical features
                for feature_name, feature_val in features.items():
                    individual[feature_name] = random.uniform(*feature_val)
            else:
                # Loop through all catgorical features
                for feature_name, feature_val in features.items():
                    individual[feature_name] = random.choice(feature_val)
        
        # Add individual to the population
        population.append(individual)

    return population


# Genetic Algorithm
def genetic_algorithm(dataframe: dict,
                      n_population: int = 50,
                      n_generations: int = 100,
                      mutation_rate: int = 0.1,
                      parent_pool: int = 2,
                      n_mutation: int = 1,
                      verbose: bool = False) -> tuple:
    
    # Initialize population
    population = initialize_population(dataframe=dataframe,
                                       n_population=n_population)

    # Initialize history of fitness
    best_fitnesses = []
    avg_fitnesses = []
    
    # Optimize through generations
    for generation in range(n_generations):

        # Compute fitness for each individual
        fitnesses = [fitness(individual, units) for individual in population]
        new_population = []
        
        # Breeding phase
        for _ in range(n_population // 2):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, dataframe, mutation_rate))
            new_population.append(mutate(child2, dataframe, mutation_rate))
        
        # Update population
        population = new_population
        
        # Update goodness of generation
        best_fitness = max(fitnesses)
        avg_fitness = sum(fitnesses) / n_population
        best_fitnesses.append(best_fitness)
        avg_fitnesses.append(avg_fitness)
        
        # Print the best fitness of the current generation
        if verbose:
            best_individual = population[np.argmax(fitnesses)]
            print(f"Generation {generation+1}: Best Fitness = {best_fitness}")
            print(f"Best Design:\n"
                  f"{best_individual}")
            print()

    # Return the best individual from the final population
    final_fitnesses = [fitness(individual, units) for individual in population]
    best_final_index = np.argmax(final_fitnesses)

    
    return population[best_final_index], max(final_fitnesses), best_fitnesses, avg_fitnesses