import numpy as np
from utils import *
from copy import deepcopy

class neural_network:
    '''
    a fully connected neural network
    '''
    def __init__(self, input_dim, ncls):
        # input_dim: dimenstion of the input
        # ncls: number of different target classes
        self.input_dim = input_dim + 1
        self.ncls = ncls
        
        # init with no hidden layers
        self.hidden_layer = 0
        self.weight = {}
        self.activation = {}
        
    def add_layer(self, n_out, activation):
        # add a single layer over the last layer
        if self.hidden_layer == 0:
            n_in = self.input_dim
        else:
            n_in = self.weight['l%d'%self.hidden_layer].shape[1]
        
        self.hidden_layer += 1
        self.weight['l%d'%(self.hidden_layer)] = xavier(n_in, n_out)
        self.activation['l%d'%(self.hidden_layer)] = activation
    
    def add_output_layer(self, activation=softmax):
        # add the final prediction layer
        if self.hidden_layer == 0:
            n_in = self.input_dim
        else:
            n_in = self.weight['l%d'%self.hidden_layer].shape[1]
        n_out = self.ncls
        self.weight['l%d'%(self.hidden_layer+1)] = xavier(n_in, n_out)
        self.activation['l%d'%(self.hidden_layer+1)] = activation
        
    def feed_forward(self, x):
        '''
        return the final prediction, and the output of each hidden layer
        '''
        out = [x]
        for l in range(1, self.hidden_layer+1):
            tmp = np.matmul(out[-1], self.weight['l%d'%l])
            out.append(self.activation['l%d'%l](tmp))
        logits = np.matmul(out[-1], self.weight['l%d'%(self.hidden_layer+1)])
        z = self.activation['l%d'%(self.hidden_layer+1)](logits)
        return z, logits, out
        
    def learn(self, x, y, batch_size=128, max_iter=5000, lr=1e-1, discount=0.999, criterion=cross_entropy, trace=True):
        '''
        x: N x d
        y: N x nclass
        '''
        x = add_bias_dim(x)
        index = np.arange(x.shape[0])
        if trace:
            loss_curve = []
        
        loss_deriv = eval(criterion.__name__ + '_deriv')
            
        for epoch in range(max_iter):
            # sample a batch of dataset
            batch_index = np.random.choice(x.shape[0], batch_size, replace=False)
            x_, y_ = x[batch_index,:], y[batch_index,:]

            # get output and loss
            z, logits, out = self.feed_forward(x_)
            loss = criterion(y_, z)
            
            if trace:
                loss_curve.append(loss)
            
            # update from output layer back to input layer
            delta = loss_deriv(y_, logits) / batch_size
            self.weight['l%d'%(self.hidden_layer+1)] += lr * np.matmul(out[-1].T, delta)
            for l in range(self.hidden_layer, 0, -1):
                activation_deriv = func_deriv(self.activation['l%d'%(self.hidden_layer)])
                delta = np.matmul(delta, self.weight['l%d'%(l+1)].T) * activation_deriv(out[l])
                self.weight['l%d'%(l)] += lr * np.matmul(out[l-1].T, delta)
            
            lr *= discount
                
        z, _, _ = self.feed_forward(x_)
        loss = criterion(y_, z)
        
        if trace:
            loss_curve.append(loss)
            return loss_curve
        else:
            return loss
        
    def learn_by_hill_climbing(self, x, y, sigma = 0.01, annealed_ratio = 0.99, annealed_iters = 10, sigma_cast = 1e-6,
                               max_iter = 500, lr = 1e-1, early_stop_iters = 10, early_stop_threshold = 1e-5,
                               criterion = cross_entropy):
        '''
        randomized hill climbing
        each time the parameters update, the update vector is a random weight (N(0, sigma^2)) plus gradient
        and if the update effects (cross entropy decreases), accept it, otherwise, retry an update.
        after 50 (annealed_iters) failures, anneal the randomized level (sigma) by a factor 0.99
        
        x: N x d
        y: N x nclass
        '''
        total_iter = 0
        early_stop_iter = 0
        x = add_bias_dim(x)
        loss_curve = []
    
        loss_deriv = eval(criterion.__name__ + '_deriv')
    
        # get output and loss    
        z, logits, out = self.feed_forward(x)
        loss = criterion(y, z)

        for epoch in range(max_iter):
            loss_curve.append(loss)
    
            # calculate gradients from output layer back to the first layer
            gradient = {}
            delta = loss_deriv(y, logits) / x.shape[0]
            gradient['l%d'%(self.hidden_layer+1)] = np.matmul(out[-1].T, delta)
            for l in range(self.hidden_layer, 0, -1):
                activation_deriv = func_deriv(self.activation['l%d'%(self.hidden_layer)])
                delta = np.matmul(delta, self.weight['l%d'%(l+1)].T) * activation_deriv(out[l])
                gradient['l%d'%(l)] = np.matmul(out[l-1].T, delta)
                
            # update by randomized graident
            annealed = True
            tmp_weight = deepcopy(self.weight)
            for try_iter in range(annealed_iters):
                total_iter += 1
                randomized_gradient = deepcopy(gradient)
                for k in randomized_gradient:
                    n_in, n_out = randomized_gradient[k].shape
                    randomized_gradient[k] += np.random.randn(n_in, n_out) * sigma
                for l in range(self.hidden_layer+1, 0, -1):
                    self.weight['l%d'%(l)] = tmp_weight['l%d'%(l)] + lr * randomized_gradient['l%d'%(l)]
                z, logits, out = self.feed_forward(x)
                try_loss = criterion(y, z)
                if try_loss < loss:
                    annealed = False
                    loss = try_loss
                    break  
        
            if annealed:
                sigma *= annealed_ratio
                if sigma < sigma_cast:
                    sigma = 0.
                    annealed_iters = 1
                self.weight = deepcopy(tmp_weight)
                
            if sigma == 0: 
                if (loss - loss_curve[-1]) / loss_curve[-1] <= early_stop_threshold:
                    early_stop_iter += 1
                    if early_stop_iter >= early_stop_iters:
                        break
                else:
                    early_stop_iter = 0

        loss_curve.append(loss)
        return loss_curve, total_iter
    
    def learn_by_simulated_annealing(self, x, y, init_temp = 1e-3, annealed_ratio = 0.9, stop_temp = 1e-5,
                                     max_iter = 100, early_stop_iters = 10, criterion = cross_entropy):
        '''
        simulated annealing
        no need to use gradient any more

        x: N x d
        y: N x nclass
        '''
        temp = init_temp
        x = add_bias_dim(x)
        loss_curve = []

        loss_deriv = eval(criterion.__name__ + '_deriv')

        # get output and loss    
        z, _, _ = self.feed_forward(x)
        loss = criterion(y, z)

        total_iter = 0
        while temp >= stop_temp:
            loss_curve.append(loss)
            
            early_stop_iter = 0
            for i in range(max_iter):
                total_iter += 1
                tmp_weight = deepcopy(self.weight)
                
                # generate a new solution
                for l in range(self.hidden_layer+1, 0, -1):
                    n_in, n_out = tmp_weight['l%d'%(l)].shape
                    noise_level = .01 * np.max(abs(tmp_weight['l%d'%(l)]))
                    self.weight['l%d'%(l)] = tmp_weight['l%d'%(l)] + np.random.randn(n_in, n_out) * noise_level
                
                # calculate its loss
                z, _, _ = self.feed_forward(x)
                try_loss = criterion(y, z)
                
                # determine whether to accept the new solution
                if try_loss < loss:
                    loss = try_loss
                else:
                    prob = 1. / (1.+np.exp((loss-try_loss) / temp))
                    if np.random.rand() <= prob:
                        self.weight = tmp_weight
                        early_stop_iter += 1
                    else:
                        loss = try_loss
                        early_stop_iter = 0
                
            temp *= annealed_ratio

        loss_curve.append(loss)
        return loss_curve, total_iter

    def learn_by_genetic_algorithm(self, x, y, group_size = 100, variance_level = .1, variance_discount = 0.9, variance_ratio = 0.1,
                                   max_iter = 100, early_stop_iters = 10, criterion = cross_entropy):
        '''
        genetic algorithm
        no need to use gradient any more

        x: N x d
        y: N x nclass
        '''
        x = add_bias_dim(x)
        loss_curve = []

        loss_deriv = eval(criterion.__name__ + '_deriv')

        # get output and loss    
        z, _, _ = self.feed_forward(x)
        loss = criterion(y, z)

        early_stop_iter = 0
        total_iter = 0
        for i in range(max_iter):
            loss_curve.append(loss)

            total_iter += 1
            # generate a group of solution
            weight_groups = [None for _ in range(group_size)]
            for j in range(group_size):
                weight_groups[j] = deepcopy(self.weight)
                for k in weight_groups[j]:
                    n_in, n_out = weight_groups[j][k].shape
                    noise_level = variance_level * np.max(abs(weight_groups[j][k]))
                    weight_groups[j][k] += np.random.randn(n_in, n_out) * noise_level            
                
            # evaluate the solution, choose the top two of them
            weight_scores = [1. for _ in range(group_size)]
            for j in range(group_size):
                self.weight = weight_groups[j]
                z, _, _ = self.feed_forward(x)
                weight_scores[j] = criterion(y, z)
            
            weight_rank = np.argsort(weight_scores)
            weight1 = weight_groups[weight_rank[0]]
            weight2 = weight_groups[weight_rank[1]]
            
            # update the weight
            for k in self.weight:
                # inherit
                self.weight[k] = .5 * weight1[k] + .5 * weight2[k]
                # mutate (by adding Guassian noise to a part of weights)
                noise_level = variance_level * np.max(abs(self.weight[k]))
                n_in, n_out = self.weight[k].shape
                noise_loc = np.random.rand(n_in, n_out) < 1-variance_ratio
                self.weight[k] += np.random.randn(n_in, n_out) * noise_level * noise_loc
                
            z, _, _ = self.feed_forward(x)
            loss = criterion(y, z)            
            variance_level *= variance_discount
            
            if loss < loss_curve[-1]:
                early_stop_iter = 0
            else:
                early_stop_iter += 1
                if early_stop_iter > early_stop_iters:
                    break

        loss_curve.append(loss)
        return loss_curve, total_iter
    
    def predict_proba(self, x):
        '''
        get the final prediction (it can be probability or regression value)
        '''
        x = np.atleast_2d(x)
        x = add_bias_dim(x)
        z, _, _ = self.feed_forward(x)
        return z
    
    def predict(self, x):
        '''
        if self.ncls is 1, then the network is used to fit a regression problem,
        otherwise, it is used to solve a classification problem.
        '''
        value = self.predict_proba(x)
        if self.ncls == 1:
            return value
        else:
            return np.argmax(value, axis=1)