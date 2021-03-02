The codes are uploaded in: https://github.gatech.edu/zjin80/CS7641/tree/master/Assignment%202

The link of dataset id:  
Gender Recognition by Voice: https://www.kaggle.com/primaryobjects/voicegender

Instruction:

1. python version 2.7 or 3 is OK.
Required packages: numpy, matplotlib

2. Execute voice_nn.py, it will output four curves (first one is the baseline, neural network with back propogation, the curves describes training loss v.s. running epochs) and the 5-fold CV average accuracy results.

3. I designed three problems for the 4 randomized otimization algorithms:

3.1 problem 1: sum and parity, that is, given a pre-defined length, output a bitstring with highest sum plus a parity bonus when the sum is even.
I expect simulated annealing to work well in the problem.
Execute sum_and_parity.py, it will output sum_and_parity.png and the outputs.

3.2 problem 2: sum_product, that is, the product of the sum of consecutive ones in a bitstring. For example, fitness of [1,0,1,1] is 1*2=2, and fitness of [1,0,1,1,0,1,1,1] is 1*2*3=6.
Because genetic algorithm can inherit good parts from the 'father' and 'mother' solutions, it is suitable for this problem.
Execute sum_product.py, it will output sum_product.png and the results.

3.3 problem 3: recover. First, a vector is randomly generated according to uniform distribution U[-0.05, 0.05]. Then, I want to optimize another vector to obtain highest inner product with it.
Because MIMIC optimize by estimating probability, so this problem is suitable for MIMIC.
Execute recover.py, it will output recover.png and the results.

