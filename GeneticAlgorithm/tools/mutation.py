import random


def mut_uniform(ind, range_max, range_min, prob=0.01):
    """
    Mutate an individual
    :param ind: List of values
    :param range_max: Float, maximum constraint
    :param range_min: Float, minimum constraint
    :param prob: Double, Mutation rate
    :return: List
    """
    for i, val in enumerate(ind):
        if random.random() <= prob:
            ind[i] = range_min + (range_max - range_min) * random.random()
#    print(ind)
    return ind


def mut_gauss(ind, mut_prob, perturb_size=1.):
    """
    Mutate an individual using a Gaussian distribution
    :param ind: List of values
    :param mut_prob: Float, probability for mutation
    :param perturb_size: Float, size of perturbation
    :return: List
    """
    for i, val in enumerate(ind):
        if random.random() <= mut_prob:
            ind[i] = val + perturb_size * random.gauss(0, 0.1)
            #if random.random() < 0.75:  # 75% of the time make a random gaussian change
            #    ind[i] = val + perturb_size * random.gauss(0, 0.1)
            #else:
            #    ind[i] = 2 * random.random() - 1  # Pick new random value between -1 and 1
    return ind

# ---------------------------------------------------------------------------------------------------------------------
