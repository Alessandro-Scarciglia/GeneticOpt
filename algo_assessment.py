from modules.restart_wrapper import montecarlo
from utils.display_utils import assessments_plot
from parameters import *

def generate_montecarlo_samples(n_samples = 10):
    samples = dict().fromkeys([test[0] for test in TESTS])
    for test in TESTS:
      POPULATION_SIZE = test[1]
      N_RESTART = test[2]
      results = []
      for i in range(n_samples):
        results.append(montecarlo(N_RESTART))
      samples[test[0]] = results
    return samples

def main():
    test_samples = generate_montecarlo_samples()
    assessments_plot(test_samples)

if __name__ == "__main__":
    main()