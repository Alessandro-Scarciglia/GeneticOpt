# Standard import
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 

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
  

def assessments_plot(samples: dict) -> None:
    norms = [norm.pdf(sample, loc=np.mean(sample), scale=np.std(sample)) for sample in samples.values()]
    labels = [key for key in samples.keys()]
    axes, lines = list(range(len(norms))), list(range(len(norms)))
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']
    _, axes[0] = plt.subplots()
    for i in range(len(norms)):
        if i < len(norms) - 1:
          axes[i+1] = axes[0].twinx()
        lines[i] = axes[i].scatter(samples[i], norms[i], label=labels[i], color=colors[i], linewidth=0.5, alpha=0.5)
    axes[0].legend(lines, [line.get_label() for line in lines])
    plt.show()