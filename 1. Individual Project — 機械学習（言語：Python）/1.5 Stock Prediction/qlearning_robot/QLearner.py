""" 			  		 			 	 	 		 		 	  		   	  			  	
Template for implementing QLearner  (c) 2015 Tucker Balch 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
Copyright 2018, Georgia Institute of Technology (Georgia Tech) 			  		 			 	 	 		 		 	  		   	  			  	
Atlanta, Georgia 30332 			  		 			 	 	 		 		 	  		   	  			  	
All Rights Reserved 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
Template code for CS 4646/7646 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
Georgia Tech asserts copyright ownership of this template and all derivative 			  		 			 	 	 		 		 	  		   	  			  	
works, including solutions to the projects assigned in this course. Students 			  		 			 	 	 		 		 	  		   	  			  	
and other users of this template code are advised not to share it with others 			  		 			 	 	 		 		 	  		   	  			  	
or to make it available on publicly viewable websites including repositories 			  		 			 	 	 		 		 	  		   	  			  	
such as github and gitlab.  This copyright statement should not be removed 			  		 			 	 	 		 		 	  		   	  			  	
or edited. 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
We do grant permission to share solutions privately with non-students such 			  		 			 	 	 		 		 	  		   	  			  	
as potential employers. However, sharing with other current or future 			  		 			 	 	 		 		 	  		   	  			  	
students of CS 7646 is prohibited and subject to being investigated as a 			  		 			 	 	 		 		 	  		   	  			  	
GT honor code violation. 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
-----do not edit anything above this line--- 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
Student Name: Zhihua Jin                                                                                            
GT User ID: zjin80                                                                                          
GT ID: 903355416        		  		 			 	 	 		 		 	  		   	  			  	
""" 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
import numpy as np 			  		 			 	 	 		 		 	  		   	  			  	
import random as rand

			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
class QLearner(object): 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
    def author(self):
        return 'zjin80' 

    def __init__(self, \
        num_states=100, \
        num_actions = 4, \
        alpha = 0.2, \
        gamma = 0.9, \
        rar = 0.5, \
        radr = 0.99, \
        dyna = 0, \
        verbose = False): 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
        self.verbose = verbose 			  		 			 	 	 		 		 	  		   	  			  	
        self.num_actions = num_actions 			  		 			 	 	 		 		 	  		   	  			  	
        self.s = 0 			  		 			 	 	 		 		 	  		   	  			  	
        self.a = 0

        self.rar = rar
        self.radr = radr
        self.dyna = dyna
        self.alpha = alpha
        self.gamma = gamma

        self.qtable = np.random.uniform(-1.0, 1.0, size=(num_states, num_actions))
        self.track = []

 			  		 			 	 	 		 		 	  		   	  			  	
    def querysetstate(self, s): 			  		 			 	 	 		 		 	  		   	  			  	
        """ 			  		 			 	 	 		 		 	  		   	  			  	
        @summary: Update the state without updating the Q-table 			  		 			 	 	 		 		 	  		   	  			  	
        @param s: The new state 			  		 			 	 	 		 		 	  		   	  			  	
        @returns: The selected action 			  		 			 	 	 		 		 	  		   	  			  	
        """ 			  		 			 	 	 		 		 	  		   	  			  	
        self.s = s 			  		 			 	 	 		 		 	  		   	  			  	
        random_action_decision = rand.random()
        if random_action_decision < self.rar:
            action = rand.randint(0, self.num_actions-1)
        else:
            action = np.argmax(self.qtable[self.s])

        if self.verbose: print "s =", s,"a =",action
        return action 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
    def query(self,s_prime,r): 			  		 			 	 	 		 		 	  		   	  			  	
        """ 			  		 			 	 	 		 		 	  		   	  			  	
        @summary: Update the Q table and return an action 			  		 			 	 	 		 		 	  		   	  			  	
        @param s_prime: The new state 			  		 			 	 	 		 		 	  		   	  			  	
        @param r: The ne state 			  		 			 	 	 		 		 	  		   	  			  	
        @returns: The selected action 			  		 			 	 	 		 		 	  		   	  			  	
        """ 			  		 			 	 	 		 		 	  		   	  			  	


        self.qtable[self.s,self.a] = (1 - self.alpha) * self.qtable[self.s,self.a] + self.alpha*(r + self.gamma*self.qtable[s_prime, np.argmax(self.qtable[s_prime])])
        self.track.append([self.s,self.a,s_prime,r])

        action = np.argmax(self.qtable[s_prime, :])

        if rand.uniform(0.0, 1.0) < self.rar:
            action = rand.randint(0, self.num_actions - 1)
        
        if self.dyna != 0:
            index = np.random.choice(len(self.track), size = self.dyna)
            
            for i in index:
                s_dyna, a_dyna, snext_dyna, R = self.track[i]
                self.qtable[s_dyna,a_dyna] = (1 - self.alpha) * self.qtable[s_dyna,a_dyna] + self.alpha * (R + self.gamma * self.qtable[snext_dyna, np.argmax(self.qtable[snext_dyna])])

        self.rar = self.rar * self.radr
        self.s = s_prime    
        self.a = action

        if self.verbose: print "s =", s_prime,"a =",action,"r =",r
        return action 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
if __name__=="__main__": 			  		 			 	 	 		 		 	  		   	  			  	
    print "Remember Q from Star Trek? Well, this isn't him" 			  		 			 	 	 		 		 	  		   	  			  	
