import dataclasses
import random
from functools import partial
from typing import Callable, TypeAlias

from genetic_algorithm.utils import view_chessboard

# Set the seed for reproducibility
random.seed(123)

Individual: TypeAlias = list[int]
IndividualPair: TypeAlias = tuple[Individual, Individual]
Population: TypeAlias = list[Individual]

FitnessFunc: TypeAlias = Callable[[Individual], int]
SelectionFunc: TypeAlias = Callable[[Population, FitnessFunc], IndividualPair]
CrossoverFunc: TypeAlias = Callable[[IndividualPair], IndividualPair]
MutationFunc: TypeAlias = Callable[[Individual, float], Individual]


def generate_individual(length: int) -> Individual:
    """
    Generate a random individual (also called Chromosome).
    An individual is a solution to the N-queens problem we want to solve.

    :param length: the number of genes in the chromosome. It represents the size of the chessboard.
    :return: a random individual characterized by a list of `length` genes.
    """

    random.shuffle(individual := list(range(1, length + 1)))
    return individual


def generate_population(pop_size: int, individual_length: int) -> Population:
    """
    Generate a random population.

    :param pop_size: number of individuals in the population.
    :param individual_length: length of each individual, number of genes.
    :return: a random population of `pop_size` individuals.
    """

    return [generate_individual(individual_length) for _ in range(pop_size)]


def fitness_func(individual: Individual) -> int:
    """
    Fitness function to determine the fit of an individual (the higher, the worse).

    :param individual: the individual to evaluate.
    :return: the fitness score of the individual.
    """

    clashes = 0
    for i in range(len(individual) - 1):
        for j in range(i + 1, len(individual)):
            if abs(individual[j] - individual[i]) == j - i:
                clashes += 1
    return clashes


def roulette_selection(population: Population, fitness: FitnessFunc) -> IndividualPair:
    """
    Selection function to select a pair of individuals based on their fitness scores.

    the fitness proportionate selection, also known as roulette wheel selection is a stochastic selection
    method, where the probability for selection of an individual is proportional to its fitness.

    :param population: the population from which to select the pair of individuals.
    :param fitness: the fitness function to score individuals.
    :return: the selected pair of individuals.
    """

    parents = random.choices(
        population=population,
        weights=[fitness(individual) for individual in population],
        k=2,
    )
    return parents[0], parents[1]


def ordered_crossover(parents: IndividualPair) -> IndividualPair:
    """
    Crossover function to combine the genetic information of two parents to generate new offspring.
    Offspring are created by randomly exchanging the genes of the parents individuals.

    The ordered crossover avoids generating invalid solutions by first copying the first part of the
    offspring from one parent and then the remaining unused genes from each second parent to the child.
    This way it guarantees that all the genes are kept without duplicates.

    :param parents: the two parent individuals to be mated.
    :return: the new offspring.
    """

    parent_a, parent_b = parents
    split_index = random.randint(1, len(parent_a) - 1)
    offspring_x = parent_a[:split_index] + list(
        filter(lambda pos: pos not in parent_a[:split_index], parent_b)
    )
    offspring_y = parent_b[:split_index] + list(
        filter(lambda pos: pos not in parent_b[:split_index], parent_a)
    )
    return offspring_x, offspring_y


def swap_mutation(individual: Individual, probability: float) -> Individual:
    """
    Randomly flip two genes of an individual with a given probability.

    :param individual: the individual to be possibly mutated.
    :param probability: the probability that mutation will take place.
    :return: the mutated individual with given `probability`, the input individual otherwise.
    """
    if random.random() <= probability:
        pos1 = random.randint(0, len(individual) - 1)
        pos2 = random.randint(0, len(individual) - 1)
        individual[pos1], individual[pos2] = individual[pos2], individual[pos1]
    return individual


@dataclasses.dataclass
class GeneticAlgorithm:

    fitness: FitnessFunc = fitness_func
    selection: SelectionFunc = roulette_selection
    crossover: CrossoverFunc = ordered_crossover
    mutation: MutationFunc = swap_mutation

    def compute_next_generation(
        self,
        population: list[Individual],
        mutation_prob: float = 0.3,
        n_elites: int = 10,
    ):
        """
        Given a population compute the next generation by applying selection, crossover and mutation to
        all the individuals. The new generation will have the same size of the given population.

        :param population: the starting population.
        :param mutation_prob: the probability at which mutation occurs.
        :param n_elites: number of elitism individuals to keep at each generation.
        :return: the best individual (solution) found.
        """

        next_generation = population[:n_elites]
        for _ in range(int((len(population) - n_elites) / 2)):
            parents = self.selection(population, self.fitness)
            offspring = self.crossover(parents)
            next_generation += map(
                partial(self.mutation, probability=mutation_prob), offspring
            )
        return next_generation

    def run_evolution(
        self,
        pop_size: int,
        individual_length: int,
        fitness_limit: int = 0,
        mutation_prob: float = 0.3,
        n_iter: int = 1000,
        n_elites: int = 10,
    ) -> Individual:
        """
        Initialize a random population and run the Genetic evolution until `fitness_limit` or `n_iter` is reached.

        :param pop_size: the population size, number of individuals.
        :param individual_length: the length of each individual (the N dimension of the NxN chessboard).
        :param fitness_limit: good enough individual's fit to stop the search.
        :param mutation_prob: the probability at which mutation occurs.
        :param n_iter: maximum number of iterations, if reached the best solution found so far is returned.
        :param n_elites: number of elitism individuals to keep at each generation.
        :return: the best individual (solution) found.
        """

        population = generate_population(pop_size, individual_length)

        for i in range(n_iter):
            population = sorted(population, key=self.fitness)
            print(f"Generation {i} - Best fitness {self.fitness(population[0])}")
            if self.fitness(population[0]) <= fitness_limit:
                break
            population = self.compute_next_generation(
                population, mutation_prob, n_elites
            )

        return sorted(population, key=self.fitness)[0]
