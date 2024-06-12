# Standard import
import numpy as np

# Fitness function to evaluate satellite designs
def fitness_function(individual: dict):

    # Compute energy absorbed
    energy = (
        individual["num_panels"] * 
        np.cos(np.radians(individual["inclination"])) *
        np.cos(np.radians(individual["orientation"])) 
    )

    # Compute weight of the solution
    weight = (
        individual["num_panels"] * 5 + 
        individual["battery_capacity"] * 0.1 + 
        individual["antenna_size"] * 10 + 
        individual["propellant"] * 2
    )

    # Define an efficiency value to maximize
    efficiency = energy / weight
    
    # Handle non-numerical data
    if individual["coating"] == 'Type A':
        efficiency *= 1.05
    elif individual["coating"] == 'Type B':
        efficiency *= 1.1
    else:
        efficiency *= 1.2

    return efficiency
