from genetic_algorithm.algorithm import (
    GeneticAlgorithm,
    fitness_func,
    roulette_selection,
    ordered_crossover,
    swap_mutation,
)
from genetic_algorithm.utils import view_chessboard
import argparse

# Instantiate the GA to solve the N-Queens problem
genetic_algorithm = GeneticAlgorithm(
    fitness=fitness_func,
    selection=roulette_selection,
    crossover=ordered_crossover,
    mutation=swap_mutation,
)


if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional arguments
    parser.add_argument(
        "-p", "--pop-size", help="Population size", type=int, default=100
    )
    parser.add_argument(
        "-n", "--individual-length", help="Chessboard dimension", type=int, default=15
    )
    parser.add_argument(
        "-l",
        "--fitness-limit",
        help="Fitness score to stop the search",
        type=int,
        default=0,
    )
    parser.add_argument(
        "--mutation-prob", help="Mutation probability", type=float, default=0.3
    )
    parser.add_argument(
        "--n-iter", help="Maximum number of iterations", type=int, default=1000
    )
    parser.add_argument("--n-elites", help="Number of elites", type=int, default=10)

    # Read arguments from command line
    args = parser.parse_args()

    # Run the evolution
    best_solution = genetic_algorithm.run_evolution(
        pop_size=args.pop_size,
        individual_length=args.individual_length,
        fitness_limit=args.fitness_limit,
        mutation_prob=args.mutation_prob,
        n_iter=args.n_iter,
        n_elites=args.n_elites,
    )

    # View the best solution found
    view_chessboard(best_solution)
