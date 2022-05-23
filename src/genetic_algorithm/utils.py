"""
Other utilities or GA functions.
"""
import math
import random
from typing import Optional, TypeAlias

import chess
import chess.svg
from cairosvg import svg2png  # type: ignore

Individual: TypeAlias = list[int]


def display_chessboard(
    individual: Individual, with_conflicts: bool = False, save: bool = False
) -> Optional[str]:
    """
    Display the individual solution using the Chess module.
    It works only for 8x8 chessboards, otherwise uses the aSCII characters to print the board.

    :param individual: the solution to visualize.
    :param with_conflicts: whether to visualize arrows for conflicts or not.
    :param save: whether to save the board as png image.

    :returns the board SVG image.
    """

    if len(individual) != 8:
        view_chessboard(individual)
        return None

    print_stats(individual)

    board = chess.Board(fen=None)
    for i, rank in enumerate(individual):
        board.set_piece_at(
            chess.square(file_index=i, rank_index=rank - 1),
            piece=chess.Piece(chess.QUEEN, color=chess.WHITE),
        )
    arrows = []
    if with_conflicts:
        for i in range(len(individual) - 1):
            for j in range(i + 1, len(individual)):
                if abs(individual[j] - individual[i]) == j - i:
                    piece_from = chess.square(i, individual[i] - 1)
                    piece_to = chess.square(j, individual[j] - 1)
                    arrows.append(
                        chess.svg.Arrow(piece_from, piece_to, color="#bb0000")
                    )

    board_image = chess.svg.board(board, arrows=arrows, size=400)

    if save:
        svg2png(
            bytestring=board_image,
            write_to=f'./img/chessboard_1arrow_{"".join([str(pos) for pos in individual])}.png',
        )
    return board_image


def print_stats(individual: Individual) -> None:
    """
    Print the number of possible solutions using permutation encoding
    and the solution representation.

    :param individual: the solution to visualize.
    """

    print(f"\nNumber of possible solution {math.factorial(len(individual)):,}")
    print(f"Solution: {individual}\n")


def view_chessboard(individual: Individual) -> None:
    """
    Print the individual solution using ASCII character.
    "[ ]" is an empty cell, while "[Q]" a cell with a queen.

    :param individual: the solution to visualize.
    """

    print_stats(individual)

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
