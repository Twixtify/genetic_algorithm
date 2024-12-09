from typing import Callable, Optional

from tools import breed
from tools import mutation as mut
from tools import selection

"""
Genetic Algorithm entrypoint to evolve current generation.

Individuals or chromosomes represent the generation to evolve through the genetic algorithm process.
Each individual represent a set of parameters or genes. 
These genes are encoded parameters. Encoding strategies are for example binary-, float- or order values.

For example:
individual_binary=[0, 1, 1, 0] 
individual_float=[0.34, 4.241, 51.123, 0.4567]
individual_order=[2, 4, 1, 7]

The fitness for each individual is calculated using a fitness function.
This function takes as candidate a particular solution and outputs the quality of this solution.
Hence this fitness function makes it possible to evaluate candidate solutions. 
Selection based on fitness is what evolves the candidate solutions towards the optimal solution each generation.

Below are a few example of how to evolve a generation.
"""


def evolve_best(individuals, fitness, n_parents, mutation: Callable):
    """
    Breed only the best individuals
    :param individuals: List of floats
    :param fitness: List of floats
    :param n_parents: Integer
    :param mutation: Callable representing the mutation function to use on the children of the new population.
    :return: List
    """
    # -- Select parents --
    parents = selection.sel_best(fitness, n_parents)  # Indexes of the best individuals in descending order

    # -- Produce children --
    children = breed.breed_uniform(individuals, parents, n_children=len(individuals), co_prob=0.5)

    # -- Mutate children --
    for child in children:
        if mutation:
            mutation(child)
        else:
            mut.mut_gauss(child, 0.01)

    new_individuals = list(children)

    # -- Elitism --
    best_id = selection.sel_best(fitness, round(0.05 * len(fitness)))
    for i, best in enumerate(best_id):
        new_individuals[i] = list(individuals[best])

    return new_individuals


def evolve_tournament(individuals, fitness, tournaments, tour_size, mutation: Callable):
    """
    Perform tournament selection and mutate children. Replace non-parents with children
    :param individuals: List of floats
    :param fitness: List of floats
    :param tournaments: Integer
    :param tour_size: Integer
    :param mutation: Callable representing the mutation function to use on the children of the new population.
    :return: List
    """
    # ------- Tournament selection --------
    parents = selection.sel_tournament(fitness, tournaments, tour_size, replace=False)

    # -- Perform Crossover --
    children = breed.breed_uniform(individuals, parents, n_children=len(individuals), co_prob=0.5)

    # ------- Mutate children -------
    for child in children:
        if mutation:
            mutation(child)
        else:
            mut.mut_gauss(child, 0.01)

    new_individuals = list(children)

    # -- Elitism --
    best_id = selection.sel_best(fitness, round(0.05 * len(fitness)))
    for i, best in enumerate(best_id):
        new_individuals[i] = list(individuals[best])

    return new_individuals


def evolve_roulette(individuals, fitness, tournaments, mutation: Callable):
    """
    Breed a new population using roulette selection.
    :param individuals: List of floats
    :param fitness: List of floats
    :param tournaments: Integer
    :param mutation: Callable representing the mutation function to use on the children of the new population.
    :return: List
    """
    # -- Select parents --
    parents = selection.sel_roulette(fitness, tournaments)

    # -- Perform Crossover --
    children = breed.breed_uniform(individuals, parents, n_children=len(individuals), co_prob=0.5)

    # ------- Mutate children -------
    for child in children:
        if mutation:
            mutation(child)
        else:
            mut.mut_gauss(child, 0.01)

    new_individuals = list(children)

    # -- Elitism --
    best_id = selection.sel_best(fitness, round(0.05 * len(fitness)))
    for i, best in enumerate(best_id):
        new_individuals[i] = list(individuals[best])

    return new_individuals


def evolve_breed_roulette(individuals, fitness, tournaments, mutation: Callable):
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
    :param mutation: Callable representing the mutation function to use on the children of the new population.
    :return: List
    """
    # -- Select parents --
    parents = selection.sel_random(list(range(len(fitness))), tournaments)
    parents_fitness = [fitness[val] for val in parents]

    # -- Perform Crossover --
    children = breed.breed_roulette(individuals, parents, parents_fitness, n_children=len(individuals), co_prob=0.5)

    # ------- Mutate children -------
    for child in children:
        if mutation:
            mutation(child)
        else:
            mut.mut_gauss(child, 0.01)

    new_individuals = list(children)

    # -- Elitism --
    best_id = selection.sel_best(fitness, round(0.05 * len(fitness)))
    for i, best in enumerate(best_id):
        new_individuals[i] = list(individuals[best])

    return new_individuals


def evolve_sus(individuals: list, fitness: list, n_parents: int, mutation: Optional[Callable]) -> list:
    """
    Breed a new population using Stochastic Universal Sampling (SUS).
    Individuals represent the generation to evolve through the genetic algorithm process.
    Each individual must contain a set of parameters or genes. These genes are encoded for example as binary-,
    float- or order values.
    :param individuals: list of parameters or genes.
    :param fitness: list of fitness values for each individual.
    :param n_parents: how many individuals survive to reproduce from this population
    :param mutation: Callable representing the mutation function to use on the children of the new population.
    :return: List
    """
    # -- Select parents --
    parents = selection.sel_sus(fitness, n_parents)

    # -- Perform crossover --
    children = breed.breed_uniform(individuals, parents, n_children=len(individuals), co_prob=0.5)

    # ------- Mutate children -------
    for child in children:
        if mutation is not None:
            mutation(child)
        else:
            mut.mut_gauss(child, 0.01)

    new_individuals = list(children)

    # -- Elitism --
    best_id = selection.sel_best(fitness, round(0.05 * len(fitness)))
    for i, best in enumerate(best_id):
        new_individuals[i] = list(individuals[best])

    return new_individuals
