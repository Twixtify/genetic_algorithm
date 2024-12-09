import numpy as np

from tools import extra


"""
Crossover is the process of creating children from individuals.
There exists many types of crossover methods. Below two of them have been implemented.

Uniform crossover is the process of swapping genes between two individuals to produce two children.
One point crossover is the process of picking a point in each individuals genome and swapping the tail after this point 
between them.
"""


def co_uniform(ind1: list, ind2: list, co_prob=0.5, modify_in_place=False) -> tuple[list, list]:
    """
    Uniform crossover. Each individual keep their length.
    Note that this method returns two individuals.
    Each gene has a probability co_prob of being swapped between individual 1 and individual 2.
    :param ind1: individual of genome 1
    :param ind2: individual of genome 2
    :param co_prob: Double
    :param modify_in_place: Boolean
    :return: Two Lists
    """
    size = min(len(ind1), len(ind2))
    co_ind1, co_ind2 = [], []
    # Iterate over the smallest individual
    for gene in range(size):
        if np.random.random() < co_prob:
            co_ind1.append(ind2[gene])
            co_ind2.append(ind1[gene])
        else:
            co_ind1.append(ind1[gene])
            co_ind2.append(ind2[gene])
    # Modify individuals
    if modify_in_place:
        # This assignment works for both numpy arrays and lists
        ind1[:size] = co_ind1
        ind2[:size] = co_ind2
        return ind1, ind2

    return co_ind1, co_ind2


def co_one_point(ind1, ind2):
    """
    One point crossover.
    Pick a position in the chromosome for both individuals and swap their genes at that position.
    Note that if len(ind1) != len(ind2) then the length of the output arrays will be interchanged.
    :param ind1: List or numpy array
    :param ind2: List or numpy array
    :return: Lists or numpy arrays
    """
    size = min(len(ind1), len(ind2))
    co_point = np.random.randint(1, size - 1)  # pick crossover point between first and last element
    """ 
    Since numpy arrays are fixed in size we have to convert them to lists first.
    This is necessary since individuals 1 and 2 might be of different lengths.
    """
    if extra.is_numpy(ind1) and extra.is_numpy(ind2):
        ind1, ind2 = ind1.tolist(), ind2.tolist()
        co_ind1, co_ind2 = ind1[:co_point] + ind2[co_point:], ind2[:co_point] + ind1[co_point:]
        ind1, ind2 = np.array(co_ind1), np.array(co_ind2)
    else:
        co_ind1, co_ind2 = ind1[:co_point] + ind2[co_point:], ind2[:co_point] + ind1[co_point:]
        ind1, ind2 = co_ind1, co_ind2

    return ind1, ind2
