# PyCon22
### Solving the N-queens problem with genetic algorithms
Companion project for the talk: Genetic Algorithm from Scratch in Python @ PyCon Italia 2022.

<div style="text-align:center">
<img src="https://github.com/AnghileriDavide/PyCon22/blob/master/img/chessboard_53172864.png?raw=true" 
alt="8x8 Chessboard with 8 Queens" width="200">
</div>

## How to setup

I use poetry to manage Python packages so after cloning the project, run the following commands to install
poetry and the required dependencies:

```bash
pip install poetry
poetry install
```

then run the following command to execute the genetic algorithm solving the N-queens problem:
```bash
python3 -m queens_ambit.py
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

## Contact

You can reach me at davide.anghileri@prima.it

## License

[![Licence](https://github.com/AnghileriDavide/PyCon22/blob/73cc1c9242059bf5343d8e9509849a80e91cd22b/img/mit-license.png?raw=true)](./LICENSE)
