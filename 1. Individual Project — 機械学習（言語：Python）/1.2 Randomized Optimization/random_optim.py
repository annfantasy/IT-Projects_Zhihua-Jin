import numpy as np

def randomized_hill_climbing(fitness, neighbor_generator, init_generator, 
                             max_iters = 20, early_stop_iters = 20):
    '''
    iters:
    
    fitness: a function handler to evaluate solutions
    neighbor_generator: a function handler to generate solution based on the present one
    init_generator: a function handler to generate initial solution
    '''
    best_sol = None
    best_fit = 0
    total_iter = 0
    for i in range(max_iters):
        sol = init_generator()
        best_fit_uptonow = fitness(sol)
        best_sol_uptonow = sol
        
        early_stop_iter = 0
        while True:
            total_iter += 1
            sol = neighbor_generator(sol)
            sol_fit = fitness(sol)
            
            if sol_fit > best_fit_uptonow:
                best_fit_uptonow = sol_fit
                best_sol_uptonow = np.copy(sol)
                early_stop_iter = 0
            else:
                early_stop_iter += 1
                if early_stop_iter > early_stop_iters:
                    break
                            
        if best_fit_uptonow > best_fit:
            best_sol = best_sol_uptonow
            best_fit = best_fit_uptonow
            
    return best_sol, best_fit, total_iter

def simulated_annealing(fitness, neighbor_generator, init_generator,
                        init_temp = 10., stop_temp = 0.1, annealed_ratio = 0.95, 
                        max_iters = 100, early_stop_iters = 20):
    sol = init_generator()
    fit = fitness(sol)
    best_sol = None
    best_fit = 0
    total_iter = 0
    
    temp = init_temp
    while temp >= stop_temp:
        early_stop_iter = 0
        for i in range(max_iters):
            total_iter += 1
            # generate a new solution
            old_sol = np.copy(sol)
            old_fit = fit
            sol = neighbor_generator(sol)
            fit = fitness(sol)

            # determine whether to accept the worse solution
            if fit < old_fit:
                prob = np.exp((fit - old_fit) / temp)
                if np.random.rand() > prob: # reject
                    sol = np.copy(old_sol)
                    fit = old_fit
                    early_stop_iter += 1
                    if early_stop_iter > early_stop_iters:
                        break
                else:
                    early_stop_iter = 0
            else:
                if fit > best_fit:
                    best_fit = fit
                    best_sol = np.copy(sol)
                    
        temp *= annealed_ratio
    
    return best_sol, best_fit, total_iter

def genetic_algorithm(fitness, neighbor_generator, init_generator, mutator,
                      max_iter = 500, early_stop_iters = 10, group_ratio = 1.):
    '''
    genetic algorithm

    '''
    sol = init_generator()
    fit = fitness(sol)
    best_sol = None
    best_fit = 0
    total_iter = 0

    early_stop_iter = 0
    for i in range(max_iter):
        # generate a group of solution
        total_iter += 1
        group_size = int(group_ratio*len(sol))
        flip_index = np.random.permutation(len(sol))[:group_size]
        sol_groups = np.zeros((group_size, len(sol)))
        for i in range(group_size):
            sol_groups[i,] = sol
            sol_groups[i,flip_index[i]] = 1 - sol_groups[i,flip_index[i]]
        fit_groups = [fitness(s) for s in sol_groups]
        
        # choose two best solutions
        rank = np.argsort(fit_groups)[::-1]
        sol1 = sol_groups[rank[0]]
        sol2 = sol_groups[rank[1]]
        
        # generate a new solution
        sol = mutator(sol1, sol2)
        fit = fitness(sol)
        
        if fit > best_fit:
            best_fit = fit
            best_sol = sol
            early_stop_iter = 0
        else:
            early_stop_iter += 1
            if early_stop_iter > early_stop_iters:
                break
            
    return best_sol, best_fit, total_iter

def MIMIC(fitness, init_generator, start_up_iters = 500, max_iters = 5000):
    sol = init_generator()
    length = len(sol)
    bit_fit = np.zeros((length, 2))
    total_iter = 0
    
    for i in range(start_up_iters):
        sol = init_generator()
        fit = fitness(sol)
        
        for i in range(length):
            bit_fit[i,sol[i]] += fit        
    
    bit_prob = np.zeros(length)
    for it in range(max_iters):
        total_iter += 1
        for i in range(length):
            if bit_fit[i,0] >= bit_fit[i,1]:
                tmp = np.exp(bit_fit[i,1] - bit_fit[i,0])
                bit_prob[i] = tmp / (1. + tmp)
            else:
                tmp = np.exp(bit_fit[i,0] - bit_fit[i,1])
                bit_prob[i] = 1. / (1. + tmp)
            
        sol = np.random.rand(length) < bit_prob
        sol = sol.astype(np.int)
        fit = fitness(sol)
        
        for i in range(length):
            bit_fit[i,sol[i]] += fit
    
    sol = np.round(bit_prob)
    fit = fitness(sol)
    return sol, fit, total_iter
        
    
    