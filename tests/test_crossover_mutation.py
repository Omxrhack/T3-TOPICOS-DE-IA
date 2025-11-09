import numpy as np
from ga.population import Individual
from ga.crossover import arithmetic_crossover
from ga.mutation import gaussian_mutation
def test_crossover_bounds_and_shape():
    rng = np.random.default_rng(1)
    a = Individual(np.array([1.0, 2.0, 3.0]))
    b = Individual(np.array([4.0, 5.0, 6.0]))
    c1, c2 = arithmetic_crossover(a, b, alpha=0.6, rng=rng)
    assert c1.genes.shape == a.genes.shape == c2.genes.shape
    assert (c1.genes >= np.minimum(a.genes, b.genes)).all()
    assert (c1.genes <= np.maximum(a.genes, b.genes)).all()
def test_gaussian_mutation_with_clamp():
    rng = np.random.default_rng(2)
    ind = Individual(np.array([0.0, 10.0]))
    child = gaussian_mutation(ind, sigma=5.0, rate=1.0, rng=rng, low=0.0, high=10.0)
    assert (child.genes >= 0.0).all() and (child.genes <= 10.0).all()
