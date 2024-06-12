# Standard import
import matplotlib.pyplot as plt


# Plot the fitness evolution
def fitness_trend(n_generations: int,
                  best_fitnesses: list,
                  avg_fitnesses: list) -> None:
    
    # Set domain 
    generations = range(n_generations)

    # Design output plot
    _, ax = plt.subplots()
    ax.plot(generations, best_fitnesses, label='Best Fitness', color='blue', linewidth=2)
    ax.plot(generations, avg_fitnesses, label='Average Fitness', color='orange', linewidth=2)
    ax.fill_between(generations, best_fitnesses, avg_fitnesses, color='blue', alpha=0.1)

    ax.set_xlabel('Generation')
    ax.set_ylabel('Fitness')
    ax.set_title('Fitness Evolution Over Generations')
    ax.legend()
    plt.grid(True)

    # Store it
    plt.show()