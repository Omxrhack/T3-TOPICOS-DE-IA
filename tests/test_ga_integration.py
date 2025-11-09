from ga import GeneticAlgorithm, GAConfig, maximize_f_x_sin_x
def test_ga_improves_best():
    cfg = GAConfig(pop_size=40, genome_length=6, generations=40, seed=123)
    ga = GeneticAlgorithm(maximize_f_x_sin_x, cfg)
    pop = ga.initialize()
    baseline = pop.best().fitness
    final_pop, history = ga.evolve(pop)
    assert final_pop.best().fitness >= baseline
    assert history[-1] >= history[0]
