import random
import time
from dataclasses import dataclass, field

import matplotlib.pyplot as plt
import numpy
import seaborn

SEED = 1234
NUM_OF_BITS = [2, 4, 6, 8, 10, 12]
TRIALS = 30

# set seed
random.seed(SEED)


@dataclass
class Experiment:
    """Class that contains information about a single trial"""

    num_of_bits: int
    attempts: list = field(default_factory=list)
    durations: list = field(default_factory=list)


def create_random_bit_pattern(length: int) -> str:
    """Generate a random sequence of binary bits of size `length`"""
    binary = random.getrandbits(length)
    return f"{binary:0{length}b}"


def run_trial(num_of_bits: int) -> tuple[int, time]:
    """Measure attempts and time to find a random desired pattern of length `num_of_bits`"""
    desired_pattern = create_random_bit_pattern(num_of_bits)
    attempts = 0
    start_time = time.time()
    time_to_end = start_time + 60 * 60
    pattern = ""
    while time.time() < time_to_end and pattern != desired_pattern:
        pattern = create_random_bit_pattern(num_of_bits)
        attempts += 1
    return attempts, time.time() - start_time


def run_experiment() -> dict[int, Experiment]:
    """Run an experiment iterating over the NUM_OF_BITS"""
    trials = {}
    for num_of_bits in NUM_OF_BITS:
        trial = Experiment(num_of_bits)
        for _ in range(TRIALS):
            attempts, duration = run_trial(num_of_bits)
            trial.attempts.append(attempts)
            trial.durations.append(duration)
        trials[num_of_bits] = trial
    return trials


def boxplot_experiment(experiment: dict[int, Experiment]) -> None:
    """Plot number of bits against attempts / duration"""
    ax = seaborn.boxplot(data=[experiment.attempts for experiment in exp.values()])
    ax.set(xlabel="Num of bits", ylabel="Attempts")
    ax.set_xticklabels(experiment.keys())
    plt.show()

    ax = seaborn.boxplot(data=[experiment.durations for experiment in exp.values()])
    ax.set(xlabel="Num of bits", ylabel="Duration")
    ax.set_xticklabels(experiment.keys())
    plt.show()


def hamming_distance(seq_a: str, seq_b: str) -> int:
    return bin(numpy.bitwise_xor(int(seq_a, 2), int(seq_b, 2))).count("1")


def fitness(seq_a: str, seq_b: str) -> int:
    return len(seq_a) - hamming_distance(seq_a, seq_b)


if __name__ == "__main__":
    exp = run_experiment()
    boxplot_experiment(exp)
