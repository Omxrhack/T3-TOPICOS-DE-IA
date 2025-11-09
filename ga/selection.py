from __future__ import annotations
import numpy as np
from .population import Individual

def tournament_selection(pop, k: int, rng: np.random.Generator) -> Individual:
    aspirantes = rng.choice(pop, size=k, replace=False)
    return max(aspirantes, key=lambda ind: ind.fitness)

def roulette_wheel(pop, rng: np.random.Generator) -> Individual:
    fits = np.array([max(ind.fitness, 0.0) for ind in pop], dtype=float)
    total = fits.sum()
    if total == 0.0:
        return rng.choice(pop)
    probs = fits / total
    idx = rng.choice(np.arange(len(pop)), p=probs)
    return pop[idx]
