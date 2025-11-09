from __future__ import annotations
import numpy as np
from .population import Individual

def gaussian_mutation(ind: Individual, sigma: float, rate: float, rng: np.random.Generator,
                      low: float | None = None, high: float | None = None) -> Individual:
    child = ind.copy()
    mask = rng.random(size=child.genes.size) < rate
    noise = rng.normal(loc=0.0, scale=sigma, size=child.genes.size)
    child.genes[mask] += noise[mask]
    if low is not None:
        child.genes = np.maximum(child.genes, low)
    if high is not None:
        child.genes = np.minimum(child.genes, high)
    child.fitness = None
    return child

def bitflip_mutation(ind: Individual, rate: float, rng: np.random.Generator) -> Individual:
    child = ind.copy()
    bits = (child.genes > 0.5).astype(int)
    flip = rng.random(size=bits.size) < rate
    bits[flip] = 1 - bits[flip]
    child.genes = bits.astype(float)
    child.fitness = None
    return child
