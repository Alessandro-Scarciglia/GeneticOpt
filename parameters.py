# Population size and generations
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1
N_RESTART = 1
VERBOSE = False
OUT_PATH = "test_output/"

# Define parameters for the satellite design
opt_params = {
    "numerical":
    {
        "inclination": [0, 90],
        "orientation": [0, 360],
        "num_panels": [1, 100],
        "battery_capacity": [100, 1000],
        "antenna_size": [1, 10],
        "propellant": [50, 500]
    },

    "categorical":
    {
        "coating": ["Type A", "Type B", "Type C"]
    }
}

# Test to be performed for algorithm assessment
# List of tuples containing test name, population size, and n_restarts
TESTS = [("Test0", 100, 1), ("Test1", 100, 10), ("Test2", 1000, 1)]