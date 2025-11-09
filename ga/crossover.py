from __future__ import annotations
import numpy as np
from .population import Individual

def one_point_crossover(a: Individual, b: Individual, rng: np.random.Generator):
    n = a.genes.size
    if n < 2:
        return a.copy(), b.copy()
    point = rng.integers(1, n)
    child1 = a.genes.copy()
    child2 = b.genes.copy()
    child1[point:], child2[point:] = child2[point:].copy(), child1[point:].copy()
    return Individual(child1), Individual(child2)

def arithmetic_crossover(a: Individual, b: Individual, alpha: float, rng: np.random.Generator):
    c1 = alpha * a.genes + (1 - alpha) * b.genes
    c2 = (1 - alpha) * a.genes + alpha * b.genes
    return Individual(c1.copy()), Individual(c2.copy())
