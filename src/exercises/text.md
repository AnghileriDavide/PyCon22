Evolutionary Algorithm

Imagine a simplification of the mastermind game where we need to figure out a specific pattern. In our simplification we only have two colors and we can vary the pattern size. The pattern will be a bit sequence of a specific size.  

Exercise 1 

Build the simulation environment. Develop the following functionalities:  

a) Create a function that produces a random bit pattern of a specific size (the bit pattern may be coded as a string 
of 0s and 1s)
  
b) Create a function that will generate random patterns and measure how many attempts and how much time does it take 
to generate the “correct” bit pattern. Make two graphs on the evolution of attempts / time vs the number of bits in 
the pattern (2, 4, 8, 12, 16, . . . ). Each “point” in the graph should be a box-plot based on the results of 30 trials. 
Use a fixed set of seeds to be able to reproduce the experiments. Stop when run-times on your machine surpass one hour 
to gather the results for a given number of bits even if you have not reached 16 bits. Compare the difference in 
attempts and run-times for each pattern size.

c) Create an evaluation function that measures the proximity to a pattern, resulting in a single number that should 
be zero if the pattern is an exact match and growing as the difference between the attempted pattern and the “correct” 
pattern increases.
  
d) Create a function inverse to the previous one that measures the “fitness” of the guessed pattern. This function 
should have a maximum value when the guessed pattern matches exactly the “correct” pattern and decreases as distance 
between patterns increases.  