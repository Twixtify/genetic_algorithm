import random
import string
from typing import Tuple


def get_fitness(candidate: str, target: str):
    """
    :param candidate: A string of the chromosome or a list of genes in chromosome.
    :param target: string target
    :return: Integer of single candidate fitness.
    """
    fitness = 0
    for index, gene in enumerate(list(candidate)):  # enumerate returns current index and element in list
        if gene == list(target)[index]:
            fitness += 1
    return fitness

def get_population(pop_size: int, sample_space: list[str], target: str) -> Tuple:
    """
    Calculate an initial set of candidates and their fitness.
    Note element index in each list have to be preserved,
    so that:
    'population[0]=first individual',
    'fitness[0]=fitness first individual'.

    :param pop_size: Number of candidates or individuals in population
    :param sample_space: Space of possible genes
    :param target: target string
    :return: list of population and fitness
    """
    candidate_size = len(target)
    population, fitness = [], []
    for individual in range(pop_size):
        candidate = generate_chromosome(sample_space=sample_space, size=candidate_size)
        population.append(candidate)
        fitness.append(get_fitness(candidate, target))
    return population, fitness


def generate_chromosome(sample_space, size):
    """
    Generate a random individual, each gene is drawn from sample_space with replacement.

    :param sample_space: list of all characters to search from
    :param size: integer determining the length of the chromosome or individual
    :return: string representing a random chromosome or individual
    """
    return ''.join(random.choices(sample_space, k=size))

def mutate(child: str):
    """
    Mutates chromosome of child with probability prob_mutation
    :param child: string of chromosome
    :return: mutated child as a string
    """
    prob_mutation = 0.05
    for i, gene in enumerate(child):
        if random.random() < prob_mutation:
            child[i] = generate_chromosome(SAMPLE_SPACE, size=1)

if __name__ == "__main__":
    from tools import evolve

    TARGET = "Hello world"

    SAMPLE_SPACE = list(string.printable)

    random.seed()  # Seed random generator
    population, fitness = get_population(pop_size=200, sample_space=SAMPLE_SPACE, target=TARGET)

    generation = 0
    print('Generation ', generation, '-', population[fitness.index(max(fitness))] + '.', ' Fitness: ', max(fitness))
    while get_fitness(population[fitness.index(max(fitness))], TARGET) < len(TARGET):
        generation += 1
        population = evolve.evolve_best(population, fitness, 20, mutate)
        for index, individual in enumerate(population):
            fitness[index] = get_fitness(individual, TARGET)
        print('Generation ', generation, '-', population[fitness.index(max(fitness))], ' Fitness: ', max(fitness))
    print('Best fit: ', ''.join(population[fitness.index(max(fitness))]))
