# PyCon22
Companion project for the talk: Genetic Algorithm from Scratch in Python @ PyCon Italia 2022.

![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)

## How to setup

I use poetry to manage Python packages so after cloning the project, run the following commands to install
poetry and the required dependencies:

```bash
pip install poetry
poetry install
```

then run the following command to execute the genetic algorithm solving the N-queens problem:
```bash
python3 -m n_queens_solver.py
```

Optional arguments:
		
|         Parameter         | Default |           Description            |
|:-------------------------:|:-------:|:--------------------------------:|
|       -p --pop-size       |   100   |         population size          |
|  -n --individual-length   |    8    |     chessboard NxN dimension     |
|    -l --fitness-limit     |    0    | fitness score to stop the search |
|      --mutation-prob      |   0.3   |       mutation probability       |
|         --n-iter          |  1000   |   maximum number of iterations   |
|        --n-elites         |   10    |         number of elites         |
