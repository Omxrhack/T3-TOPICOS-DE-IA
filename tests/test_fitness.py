import numpy as np
from ga.fitness import maximize_f_x_sin_x
def test_fitness_known_values():
    x = np.array([0.0, np.pi, np.pi/2])
    val = maximize_f_x_sin_x(x)
    assert abs(val - (np.pi/2)) < 1e-6
