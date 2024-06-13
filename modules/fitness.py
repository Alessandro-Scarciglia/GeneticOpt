# Custom import
from parameters import *


# Custom fitness function definition
def fitness(individual: str, units: dict) -> float:

    weights = {
        "cost": -1.0,  # Lower cost is better
        "processing_power": 3.0,  # Higher processing power is better
        "fps": 2.0,  # Higher fps is better
        "reliability": 5.0  # Higher reliability is better
    }

    # Initialize aggregated values
    total_cost = 0
    total_processing_power = 0
    total_fps = 0
    reliability_score = 0

    # Processor
    processor = units["processors"][individual["processor"]]
    total_cost += processor["cost"]
    total_processing_power += processor["processing_power"]

    # Co-Processor
    coprocessor = units["coprocessors"][individual["coprocessor"]]
    total_cost += coprocessor["cost"]
    total_processing_power += coprocessor["processing_power"]

    # Redundancy
    if individual["processor_redundancy"] == "Yes":
        total_cost += processor["cost"]
        total_processing_power += processor["processing_power"]
        reliability_score += 2  # Arbitrary increase for redundancy

    if individual["coprocessor_redundancy"] == "Yes":
        total_cost += coprocessor["cost"]
        total_processing_power += coprocessor["processing_power"]
        reliability_score += 2  # Arbitrary increase for redundancy

    # Inspection Camera
    inspection_camera = units["inspection_cameras"][individual["inspection_camera"]]
    total_cost += inspection_camera["cost"]
    total_fps += inspection_camera["fps"]

    # Multispectral Camera
    multispectral_camera = units["multispectral_cameras"][individual["multispectral_camera"]]
    total_cost += multispectral_camera["cost"]
    total_fps += multispectral_camera["fps"]

    # Calculate fitness score
    fitness = 0.0
    fitness += weights["cost"] * (200000 - total_cost) / 199000  # Normalizing cost
    fitness += weights["processing_power"] * total_processing_power / 3000  # Normalizing processing power
    fitness += weights["fps"] * total_fps / 120  # Normalizing fps
    fitness += weights["reliability"] * reliability_score / 4  # Normalizing reliability score

    return fitness
