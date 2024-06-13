# Import from custom modules
from parameters import *
from modules.ga_functions import genetic_algorithm
from utils.display_utils import fitness_trend


# Main function
def main():

    # Run genetic optimization
    _, _, best_fitnesses, avg_fitnesses = genetic_algorithm(dataframe=features_table,
                                                            n_population=POPULATION_SIZE,
                                                            n_generations=GENERATIONS,
                                                            mutation_rate=MUTATION_RATE,
                                                            parent_pool=PARENT_POOL,
                                                            n_mutation=N_MUTATION,
                                                            verbose=VERBOSE)
    
    
    
    # Plot optimization trend
    fitness_trend(n_generations=GENERATIONS,
                  best_fitnesses=best_fitnesses,
                  avg_fitnesses=avg_fitnesses)
    
    
if __name__ == "__main__":
    main()
