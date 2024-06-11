import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import norm
from tqdm import tqdm

# Define parameters for the satellite design
# TODO: Encode parameters with binary code and assess performances shift, if any.
ANGLE_MIN, ANGLE_MAX = 0, 90  # Inclination angle in degrees
ORIENT_MIN, ORIENT_MAX = 0, 360  # Orientation in degrees
PANELS_MIN, PANELS_MAX = 1, 100  # Number of solar panels
BATTERY_MIN, BATTERY_MAX = 100, 1000  # Battery capacity in Ah
ANTENNA_MIN, ANTENNA_MAX = 1, 10  # Antenna size in meters
COATING_TYPES = ['Type A', 'Type B', 'Type C']  # Thermal coating types
PROPELLANT_MIN, PROPELLANT_MAX = 50, 500  # Propellant amount in kg

# Population size and generations
POPULATION_SIZE = 50
GENERATIONS = 1000
MUTATION_RATE = 0.1
N_RESTART = 1
VERBOSE = False
OUT_PATH = "test_output/"

# Fitness function to evaluate satellite designs
def fitness_function(chromosome):
    inclination, orientation, panels, battery, antenna, coating, propellant = chromosome
    # Simplified models
    energy = panels * np.cos(np.radians(inclination)) * np.cos(np.radians(orientation))
    weight = panels * 5 + battery * 0.1 + antenna * 10 + propellant * 2
    efficiency = energy / weight
    
    if coating == 'Type A':
        efficiency *= 1.05
    elif coating == 'Type B':
        efficiency *= 1.1
    else:
        efficiency *= 1.2
    return efficiency * 100

# Initialize population
def initialize_population():
    population = []
    for _ in range(POPULATION_SIZE):
        inclination = random.uniform(ANGLE_MIN, ANGLE_MAX)
        orientation = random.uniform(ORIENT_MIN, ORIENT_MAX)
        panels = random.randint(PANELS_MIN, PANELS_MAX)
        battery = random.randint(BATTERY_MIN, BATTERY_MAX)
        antenna = random.uniform(ANTENNA_MIN, ANTENNA_MAX)
        coating = random.choice(COATING_TYPES)
        propellant = random.randint(PROPELLANT_MIN, PROPELLANT_MAX)
        population.append([inclination, orientation, panels, battery, antenna, coating, propellant])
    return population

# Selection: Tournament selection
def select(population, fitnesses):
    tournament_size = 5
    selected = random.sample(range(POPULATION_SIZE), tournament_size)
    selected_fitnesses = [fitnesses[i] for i in selected]
    return population[selected[np.argmax(selected_fitnesses)]]

# Crossover: Single point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, 6)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation
# TODO: What if the randomicity gets modified?
def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        gene_to_mutate = random.randint(0, 6)
        if gene_to_mutate == 0:
            chromosome[0] = random.uniform(ANGLE_MIN, ANGLE_MAX)
        elif gene_to_mutate == 1:
            chromosome[1] = random.uniform(ORIENT_MIN, ORIENT_MAX)
        elif gene_to_mutate == 2:
            chromosome[2] = random.randint(PANELS_MIN, PANELS_MAX)
        elif gene_to_mutate == 3:
            chromosome[3] = random.randint(BATTERY_MIN, BATTERY_MAX)
        elif gene_to_mutate == 4:
            chromosome[4] = random.uniform(ANTENNA_MIN, ANTENNA_MAX)
        elif gene_to_mutate == 5:
            chromosome[5] = random.choice(COATING_TYPES)
        else:
            chromosome[6] = random.randint(PROPELLANT_MIN, PROPELLANT_MAX)
    return chromosome

# Genetic Algorithm
def genetic_algorithm():
    population = initialize_population()
    best_fitnesses = []
    avg_fitnesses = []
    
    for generation in range(GENERATIONS):
        fitnesses = [fitness_function(individual) for individual in population]
        new_population = []
        
        for _ in range(POPULATION_SIZE // 2):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        
        population = new_population
        
        best_fitness = max(fitnesses)
        avg_fitness = sum(fitnesses) / POPULATION_SIZE
        best_fitnesses.append(best_fitness)
        avg_fitnesses.append(avg_fitness)
        
        # Print the best fitness in the current generation
        best_individual = population[np.argmax(fitnesses)]
        if VERBOSE:
            print(f"Generation {generation+1}: Best Fitness = {best_fitness}")
            print(f"Best Design: Inclination = {best_individual[0]}, Orientation = {best_individual[1]}, Panels = {best_individual[2]}, "
                f"Battery = {best_individual[3]}, Antenna = {best_individual[4]}, Coating = {best_individual[5]}, Propellant = {best_individual[6]}")
        
    # Return the best individual from the final population
    final_fitnesses = [fitness_function(individual) for individual in population]
    best_final_index = np.argmax(final_fitnesses)
    
    # Plot the fitness evolutiob
    if VERBOSE:
        generations = range(GENERATIONS)
        _, ax = plt.subplots()
        ax.plot(generations, best_fitnesses, label='Best Fitness', color='blue', linewidth=2)
        ax.plot(generations, avg_fitnesses, label='Average Fitness', color='orange', linewidth=2)
        ax.fill_between(generations, best_fitnesses, avg_fitnesses, color='blue', alpha=0.1)

        ax.set_xlabel('Generation')
        ax.set_ylabel('Fitness')
        ax.set_title('Fitness Evolution Over Generations')
        ax.legend()

        plt.grid(True)
        plt.show()
    
    return population[best_final_index], max(final_fitnesses)

# Montecarlo to select best-of-the-best individual 
def montecarlo():
    
    # Initialize history of variables
    designs, fitnesses = list(), list()
    
    # Restart GA for N_RESTART times
    for _ in range(N_RESTART):
        best_design, best_fitness = genetic_algorithm()
        
        # Store best design and individuals
        designs.append(best_design)
        fitnesses.append(best_fitness)
        
    # Choose best-of-best (bob) among the N_RESTART outputs
    bob_design = designs[np.argmax(fitnesses)]
    bob_fitness = fitnesses[np.argmax(fitnesses)]
    
    return bob_design, bob_fitness

# Run the genetic algorithm
def main():
    
    # Initialize bob fitness history
    ts_fitness = list()
    
    # Iterate through test cases
    for _ in tqdm(range(100)):
        out_design, out_fitness = montecarlo()
        # print(f"Best Design Found: {out_design}")
        # print(f"Best Fitness Value: {out_fitness}")
        ts_fitness.append(out_fitness)
    
    # Build Gaussian for plots
    mean = np.mean(ts_fitness)
    std = np.std(ts_fitness)
    
if __name__ == "__main__":
    main()
