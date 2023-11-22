import random
import math


def rvg_poisson(alpha):
    """
    Generate a random variable drawn from poisson distribution
    :param alpha: parameter of poisson distribution
    :return: random poisson variable
    """
    # Step 1
    n = 0
    p = 1
    # Step 2 & 3
    lower_bound = math.exp(- alpha)
    while p >= lower_bound:
        n += 1
        random_number = random.random()
        p *= random_number
    return n

def rvg_exponential(parameter):
    """
    Generate a random variable drawn from exponential distribution
    :param parameter: parameter of exponential distribution
    :return: random exponential variable
    """
    random_number = random.random()
    random_variable = - (1 / parameter) * math.log(random_number, 2.71)
    return random_variable

def rvg_triangular(minimum, most_likely, maximum):
    """
    Generate a random variable drawn from triangular distribution
    :param minimum: (distribution parameter) min possible value
    :param most_likely: (distribution parameter) most likely possible value
    :param maximum: (distribution parameter) max possible value
    :return: random triangular variable
    """
    random_number = random.random()
    parser = (most_likely - minimum) / (maximum - minimum)
    if random_number <= parser:
        random_variable = minimum + math.sqrt((most_likely - minimum) * (maximum - minimum) * random_number)
    else:
        random_variable = maximum - math.sqrt((maximum - minimum) * (maximum - most_likely) * (1 - random_number))
    return random_variable

