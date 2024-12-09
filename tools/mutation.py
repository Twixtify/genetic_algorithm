import random


"""
Mutation is the process of changing a gene of an individual by random chance.
This process is used to maintain and introduce diversity in the population.
Ideally each individual should have its own mutation function.

Here is a list of possible mutation strategies:
Perturbation: Change at random some gene of the individual by perturbing its value.
Swap: Choose two genes and swap their position.
Scramble: Choose a random length segment and interchange genes in this segment.
Inversion: Choose a random length segment and reverse the order of genes in it.
"""

def mut_uniform(individual, mut_prob, range_max, range_min):
    """
    Mutate an individual of genes with float values.
    :param individual: List of values
    :param mut_prob: Double, probability for mutation
    :param range_max: Float, maximum constraint
    :param range_min: Float, minimum constraint
    :return: List
    """
    for i, val in enumerate(individual):
        if random.random() <= mut_prob:
            individual[i] = range_min + (range_max - range_min) * random.random()
    return individual


def mut_gauss(individual: list, mut_prob: float, perturb_size=1., mu=0., sigma=0.1):
    """
    Mutate an individual using a Gaussian distribution.
    This function assume the individual genes are a list of floats.
    :param individual: List of values
    :param mut_prob: Float, probability for mutation
    :param perturb_size: Float, size of perturbation
    :param mu: mean for the gaussian distribution
    :param sigma: the standard deviation
    :return: List
    """
    for i, val in enumerate(individual):
        if random.random() <= mut_prob:
            individual[i] = val + perturb_size * random.gauss(mu, sigma)
    return individual
