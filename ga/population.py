from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Callable
import numpy as np

@dataclass
class Individual:
    genes: np.ndarray
    fitness: float | None = None
    def copy(self) -> "Individual":
        return Individual(self.genes.copy(), self.fitness)

@dataclass
class Population:
    individuals: List[Individual] = field(default_factory=list)
    def best(self) -> Individual:
        return max(self.individuals, key=lambda ind: ind.fitness if ind.fitness is not None else -np.inf)
    def evaluate(self, fitness_fn: Callable[[np.ndarray], float]) -> None:
        for ind in self.individuals:
            ind.fitness = fitness_fn(ind.genes)
    @staticmethod
    def random_uniform(size: int, genome_length: int, low: float, high: float, rng: np.random.Generator) -> "Population":
        inds = [Individual(rng.uniform(low, high, size=genome_length)) for _ in range(size)]
        return Population(inds)
