from GeneticAlgorithm.tools.selection import *
from GeneticAlgorithm.tools.mutation import *
from GeneticAlgorithm.tools.breed import *


def evolve_best(individuals, fitness, n_parents):
    """
    Breed only the best individuals
    :param individuals: List of floats
    :param fitness: List of floats
    :param n_parents: Integer
    :return: List
    """
    # -- Select parents --
    parents = sel_best(fitness, n_parents)  # Indexes of best individuals in descending order

    # -- Produce children --
    children = breed_uniform(individuals, parents, n_children=len(individuals), co_prob=0.5)

    # -- Mutate children --
    for child in children:
        mut_gauss(child, 0.01)

    new_individuals = list(children)

    # -- Elitism --
    best_id = sel_best(fitness, round(0.05 * len(fitness)))
    for i, best in enumerate(best_id):
        new_individuals[i] = list(individuals[best])

    return new_individuals


def evolve_tournament(individuals, fitness, tournaments, tour_size):
    """
    Perform tournament selection and mutate children. Replace non-parents with children
    :param individuals: List of floats
    :param fitness: List of floats
    :param tournaments: Integer
    :param tour_size: Integer
    :return: List
    """
    # ------- Tournament selection --------
    parents = sel_tournament(fitness, tournaments, tour_size, replace=False)

    # -- Perform Crossover --
    children = breed_uniform(individuals, parents, n_children=len(individuals), co_prob=0.5)

    # ------- Mutate children -------
    for child in children:
        mut_gauss(child, 0.01)

    new_individuals = list(children)

    # -- Elitism --
    best_id = sel_best(fitness, round(0.05 * len(fitness)))
    for i, best in enumerate(best_id):
        new_individuals[i] = list(individuals[best])

    return new_individuals


def evolve_roulette(individuals, fitness, tournaments):
    """
    Breed a new population using roulette selection.
    :param individuals: List of floats
    :param fitness: List of floats
    :param tournaments: Integer
    :return: List
    """
    # -- Select parents --
    parents = sel_roulette(fitness, tournaments)

    # -- Perform Crossover --
    children = breed_uniform(individuals, parents, n_children=len(individuals), co_prob=0.5)

    # ------- Mutate children -------
    for child in children:
        mut_gauss(child, 0.01)

    new_individuals = list(children)

    # -- Elitism --
    best_id = sel_best(fitness, round(0.05 * len(fitness)))
    for i, best in enumerate(best_id):
        new_individuals[i] = list(individuals[best])

    return new_individuals


def evolve_breed_roulette(individuals, fitness, tournaments):
    """
    Breed a new population using breed_roulette.

    **
    This method does - NOT - use roulette selection to pick parents from the population.
    It uses roulette selection when picking which parents should breed.
    See 'evolve_roulette' for using roulette selection.
    **

    :param individuals: List of floats
    :param fitness: List of floats
    :param tournaments: Integer
    :return: List
    """
    # -- Select parents --
    parents = sel_random(list(range(len(fitness))), tournaments)
    parents_fitness = [fitness[val] for val in parents]

    # -- Perform Crossover --
    children = breed_roulette(individuals, parents, parents_fitness, n_children=len(individuals), co_prob=0.5)

    # ------- Mutate children -------
    for child in children:
        mut_gauss(child, 0.01)

    new_individuals = list(children)

    # -- Elitism --
    best_id = sel_best(fitness, round(0.05 * len(fitness)))
    for i, best in enumerate(best_id):
        new_individuals[i] = list(individuals[best])

    return new_individuals
