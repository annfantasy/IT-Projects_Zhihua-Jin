import numpy as np
import matplotlib.pyplot as plt
from random_optim import *
import time

testing_times = 50
length = 40

def fitness(sol):
    '''
    for example, [1, 0, 1, 1] fitness is 1*2 = 2
    [1, 0, 1, 1, 0, 1, 1, 1] fitness is 1*2*3 = 6
    '''
    sol = list(sol)
    sol.append(0)
    sums = []
    start = -1
    for i in range(len(sol)):
        if start == -1 and sol[i] == 1:
            start = i
        elif start != -1 and sol[i] == 0:
            sums.append(sum(sol[start:i]))
            start = -1
            
    return np.prod(sums)

def init_generator():
    sol = np.random.rand(length) < 0.5
    sol = sol.astype(np.int)
    
    return sol

def neighbor_generator(sol):
    idx = int(np.floor(np.random.random() * length))
    sol[idx] = 1 - sol[idx]
    
    return sol

def mutator(sol1, sol2):
    sol = np.zeros(len(sol1))
    zeros_places = np.argwhere(sol1 == 0)
    idx = zeros_places[np.random.randint(len(zeros_places))][0]
    sol[:idx] = sol1[:idx]
    sol[idx:] = sol2[idx:]
    
    return sol

if __name__ == '__main__':
    fit_rhc = np.zeros(testing_times)
    fit_sa = np.zeros(testing_times)
    fit_ga = np.zeros(testing_times)
    fit_mimic = np.zeros(testing_times)
    
    total_iter_rhc = np.zeros(testing_times)
    total_iter_sa = np.zeros(testing_times)
    total_iter_ga = np.zeros(testing_times)
    total_iter_mimic = np.zeros(testing_times)
    
    time_rhc = np.zeros(testing_times)
    time_sa = np.zeros(testing_times)
    time_ga = np.zeros(testing_times)
    time_mimic = np.zeros(testing_times)    
    for i in range(testing_times):
        t1 = time.time()
        _, fit_rhc[i], total_iter_rhc[i] = randomized_hill_climbing(fitness, neighbor_generator, init_generator)
        t2 = time.time()
        time_rhc[i] = (t2-t1) / total_iter_rhc[i]        

        t1 = time.time()
        _, fit_sa[i], total_iter_sa[i] = simulated_annealing(fitness, neighbor_generator, init_generator, init_temp=1., stop_temp=.05, max_iters=30)
        t2 = time.time()
        time_sa[i] = (t2-t1) / total_iter_sa[i] 

        t1 = time.time()
        _, fit_ga[i], total_iter_ga[i] = genetic_algorithm(fitness, neighbor_generator, init_generator, mutator)
        t2 = time.time()
        time_ga[i] = (t2-t1) / total_iter_ga[i]        

        t1 = time.time()
        _, fit_mimic[i], total_iter_mimic[i] = MIMIC(fitness, init_generator)
        t2 = time.time()
        time_mimic[i] = (t2-t1) / total_iter_mimic[i]             

    print('       max   ave   min    std   time/iter')
    print('  rhc  %.3f   %.3f   %.3f   %.3f   %f'%
          (np.max(fit_rhc), np.mean(fit_rhc), np.min(fit_rhc), np.std(fit_rhc), time_rhc[i]))
    print('  sa   %.3f   %.3f   %.3f   %.3f   %f'%
          (np.max(fit_sa), np.mean(fit_sa), np.min(fit_sa), np.std(fit_sa), time_sa[i]))
    print('  ga   %.3f   %.3f   %.3f   %.3f   %f'%
          (np.max(fit_ga), np.mean(fit_ga), np.min(fit_ga), np.std(fit_ga), time_ga[i]))
    print('mimic  %.3f   %.3f   %.3f   %.3f   %f'%
          (np.max(fit_mimic), np.mean(fit_mimic), np.min(fit_mimic), np.std(fit_mimic), time_mimic[i]))  
    plt.hist(fit_rhc, alpha=.3)
    plt.hist(fit_sa, alpha=.3)
    plt.hist(fit_ga, alpha=.3)
    plt.hist(fit_mimic, alpha=.3)
    plt.legend(['randomized hill climbing', 'simulated annealing', 'genetic algorithm', 'MIMIC'])
    plt.show()