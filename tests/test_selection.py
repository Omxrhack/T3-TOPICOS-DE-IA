import numpy as np
from ga.population import Population, Individual
from ga.selection import tournament_selection
def test_tournament_bias():
    rng = np.random.default_rng(0)
    inds = [Individual(np.array([i], dtype=float), fitness=float(i)) for i in range(10)]
    pop = Population(inds)
    wins = 0
    trials = 200
    for _ in range(trials):
        w = tournament_selection(pop.individuals, k=3, rng=rng)
        if w.fitness == 9.0:
            wins += 1
    assert wins > trials * 0.3
