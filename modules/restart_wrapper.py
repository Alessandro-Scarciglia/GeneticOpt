# Standard import
import numpy as np

# Import from custom modules
from .ga_functions import genetic_algorithm


# Montecarlo to select best-of-the-best individual 
def montecarlo(n_restart: int = 1) -> tuple:
    
    # Initialize history of variables
    designs, fitnesses = list(), list()
    
    # Restart GA for N_RESTART times
    for _ in range(n_restart):
        best_design, best_fitness = genetic_algorithm()
        
        # Store best design and individuals
        designs.append(best_design)
        fitnesses.append(best_fitness)
        
    # Choose best-of-best (bob) among the N_RESTART outputs
    bob_design = designs[np.argmax(fitnesses)]
    bob_fitness = fitnesses[np.argmax(fitnesses)]
    
    return bob_design, bob_fitness