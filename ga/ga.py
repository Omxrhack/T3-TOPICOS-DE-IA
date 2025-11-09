from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from .population import Population, Individual
from .selection import tournament_selection
from .crossover import arithmetic_crossover
from .mutation import gaussian_mutation

@dataclass
class GAConfig:
    pop_size: int = 60
    genome_length: int = 8
    low: float = 0.0
    high: float = 10.0
    tournament_k: int = 3
    crossover_rate: float = 0.9
    crossover_alpha: float = 0.6
    mutation_rate: float = 0.1
    mutation_sigma: float = 0.2
    elitism: int = 2
    generations: int = 100
    seed: int | None = 42

class GeneticAlgorithm:
    def __init__(self, fitness_fn, config: GAConfig):
        self.cfg = config
        self.fitness_fn = fitness_fn
        self.rng = np.random.default_rng(config.seed)

    def initialize(self) -> Population:
        pop = Population.random_uniform(
            size=self.cfg.pop_size,
            genome_length=self.cfg.genome_length,
            low=self.cfg.low,
            high=self.cfg.high,
            rng=self.rng
        )
        pop.evaluate(self.fitness_fn)
        return pop

    def evolve(self, pop: Population):
        history_best = [pop.best().fitness]
        for _ in range(self.cfg.generations):
            elites = sorted(pop.individuals, key=lambda i: i.fitness, reverse=True)[: self.cfg.elitism]
            children = []
            while len(children) < self.cfg.pop_size - self.cfg.elitism:
                p1 = tournament_selection(pop.individuals, self.cfg.tournament_k, self.rng)
                p2 = tournament_selection(pop.individuals, self.cfg.tournament_k, self.rng)
                if self.rng.random() < self.cfg.crossover_rate:
                    c1, c2 = arithmetic_crossover(p1, p2, self.cfg.crossover_alpha, self.rng)
                else:
                    c1, c2 = p1.copy(), p2.copy()
                c1 = gaussian_mutation(c1, sigma=self.cfg.mutation_sigma, rate=self.cfg.mutation_rate,
                                       rng=self.rng, low=self.cfg.low, high=self.cfg.high)
                c2 = gaussian_mutation(c2, sigma=self.cfg.mutation_sigma, rate=self.cfg.mutation_rate,
                                       rng=self.rng, low=self.cfg.low, high=self.cfg.high)
                children.extend([c1, c2])
            new_inds = elites + children[: self.cfg.pop_size - self.cfg.elitism]
            pop = Population(new_inds)
            pop.evaluate(self.fitness_fn)
            history_best.append(pop.best().fitness)
        return pop, history_best
