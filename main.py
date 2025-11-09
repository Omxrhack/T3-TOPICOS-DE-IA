from ga import GeneticAlgorithm, GAConfig, maximize_f_x_sin_x

def run():
    cfg = GAConfig(pop_size=80, genome_length=10, generations=120,
                   mutation_rate=0.12, mutation_sigma=0.25,
                   crossover_rate=0.9, crossover_alpha=0.55,
                   elitism=2, low=0.0, high=10.0, seed=42)
    ga = GeneticAlgorithm(maximize_f_x_sin_x, cfg)
    pop = ga.initialize()
    final_pop, history = ga.evolve(pop)
    best = final_pop.best()
    print("Mejor aptitud:", best.fitness)
    print("Mejor individuo:", best.genes)

if __name__ == "__main__":
    run()
