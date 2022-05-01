"""
Other utilities or GA functions.
"""
import math
import random
from typing import TypeAlias

Individual: TypeAlias = list[int]


def view_chessboard(individual: Individual) -> None:
    """
    Print the individual solution.

    :param individual: the solution to visualize.
    """

    print(f"\nNumber of possible solution {math.factorial(len(individual)):,}")
    print(f"Solution: {individual}\n")

    for row, _ in enumerate(individual):
        for col, _ in enumerate(individual):
            cell = "[Q]" if individual[col] - 1 == row else "[ ]"
            print(cell, end="")
        print()


def max_fitness(length: int) -> int:
    """
    The maximum (worse) fitness for an NxN chessboard.
    All queens must be on the same row, column or diagonal.

    :param length: the length N of the chessboard (NxN)
    :return the maximum fitness score

    (N-1) + (N-2) +...+ 2 + 1 ≡ N*(N-1)/2
    """

    return int(length * (length - 1) / 2)


def multi_swap_mutation(
    individual: Individual, num_mutations: int = 5, probability: float = 0.5
) -> Individual:
    """
    Randomly flip two genes of an individual multiple times with a given probability.

    :param individual: the individual to be possibly mutated.
    :param num_mutations: the number of times the mutation will occur.
    :param probability: the probability that multi-mutation will take place.
    :return: the mutated individual with given `probability`, the input individual otherwise.
    """

    if random.random() <= probability:
        for _ in range(num_mutations):
            pos1 = random.randint(0, len(individual) - 1)
            pos2 = random.randint(0, len(individual) - 1)
            individual[pos1], individual[pos2] = individual[pos2], individual[pos1]
    return individual


def shuffle_mutation(individual: Individual, probability: float = 0.2) -> Individual:
    """
    Randomly shuffle the genes of an individual with a given probability.
    Also called permutation.

    :param individual: the individual to be possibly mutated.
    :param probability: the probability that mutation will take place.
    :return: the shuffled individual with given `probability`, the input individual otherwise.
    """

    if random.random() <= probability:
        random.shuffle(individual)
    return individual
