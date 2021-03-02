import numpy as np
import matplotlib.pyplot as plt

from utils import *
from nn import *
import time
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score

lines = open('voice.csv').readlines()[1:]
x, label = [], []
for line in lines:
    line = line.strip().split(',')
    x.append([float(n) for n in line[:-1]])
    label.append(line[-1])
    
y, _ = OneHotEncoding(label)
x = np.array(x)
x_min = np.min(x, axis=0)
x_max = np.max(x, axis=0)
for i in range(x.shape[1]):
    x[:,i] = (x[:,i] - x_min[i]) / (x_max[i] - x_min[i])

# loss curve fitting the whole dataset
#nn = neural_network(x.shape[1], len(np.unique(y)))
#nn.add_layer(50, ReLU)
#nn.add_output_layer(activation=softmax)
#loss_curve = nn.learn(x, y)
#_y = np.argmax(y, axis=1)
#pred = nn.predict(x)
#plt.plot(loss_curve)
#plt.xlabel('iters')
#plt.ylabel('cross entropy')
#plt.title('training acc = %.3f, f1 = %.3f'%(accuracy_score(_y, pred), f1_score(_y, pred)))
#plt.show()

#nn = neural_network(x.shape[1], len(np.unique(y)))
#nn.add_layer(50, ReLU)
#nn.add_output_layer(activation=softmax)
#loss_curve, _ = nn.learn_by_hill_climbing(x, y)
#_y = np.argmax(y, axis=1)
#pred = nn.predict(x)
#plt.plot(loss_curve)
#plt.xlabel('iters')
#plt.ylabel('cross entropy')
#plt.title('training acc = %.3f, f1 = %.3f'%(accuracy_score(_y, pred), f1_score(_y, pred)))
#plt.show()

#nn = neural_network(x.shape[1], len(np.unique(y)))
#nn.add_layer(50, ReLU)
#nn.add_output_layer(activation=softmax)
#loss_curve, _ = nn.learn_by_simulated_annealing(x, y)
#_y = np.argmax(y, axis=1)
#pred = nn.predict(x)
#plt.plot(loss_curve)
#plt.xlabel('iters')
#plt.ylabel('cross entropy')
#plt.title('training acc = %.3f, f1 = %.3f'%(accuracy_score(_y, pred), f1_score(_y, pred)))
#plt.show()

#nn = neural_network(x.shape[1], len(np.unique(y)))
#nn.add_layer(50, ReLU)
#nn.add_output_layer(activation=softmax)
#loss_curve, _ = nn.learn_by_genetic_algorithm(x, y)
#_y = np.argmax(y, axis=1)
#pred = nn.predict(x)
#plt.plot(loss_curve)
#plt.xlabel('iters')
#plt.ylabel('cross entropy')
#plt.title('training acc = %.3f, f1 = %.3f'%(accuracy_score(_y, pred), f1_score(_y, pred)))
#plt.show()

# 5-fold CV
idx = np.random.permutation(x.shape[0])
x = x[idx,:]
y = y[idx,:]
acc_hc, acc_sa, acc_ga = [], [], []
t_hc, t_sa, t_ga = [], [], []
f1_hc, f1_sa, f1_ga = [], [], []
auc_hc, auc_sa, auc_ga = [], [], []
for train_idx, test_idx in KFold(n_splits=5).split(x, y):
    x_train, x_test = x[train_idx, :], x[test_idx, :]
    y_train, y_test = y[train_idx, :], y[test_idx, :]
    _y_test = np.argmax(y_test, axis=1)
    
    nn = neural_network(x.shape[1], len(np.unique(y)))
    nn.add_layer(50, ReLU)
    nn.add_output_layer(activation=softmax)    
    t1 = time.time()
    _, total_iters = nn.learn_by_hill_climbing(x_train, y_train)
    t2 = time.time()
    z = nn.predict(x_test)
    p = nn.predict_proba(x_test)
    
    acc_hc.append(accuracy_score(_y_test, z))
    f1_hc.append(f1_score(_y_test, z))
    auc_hc.append(roc_auc_score(_y_test, p[:,1]))
    t_hc.append((t2-t1) / total_iters)
    
    nn = neural_network(x.shape[1], len(np.unique(y)))
    nn.add_layer(50, ReLU)
    nn.add_output_layer(activation=softmax)    
    t1 = time.time()
    _, total_iters = nn.learn_by_simulated_annealing(x_train, y_train)
    t2 = time.time()
    z = nn.predict(x_test)
    p = nn.predict_proba(x_test)
    
    acc_sa.append(accuracy_score(_y_test, z))
    f1_sa.append(f1_score(_y_test, z))
    auc_sa.append(roc_auc_score(_y_test, p[:,1]))
    t_sa.append((t2-t1) / total_iters)
    
    
    nn = neural_network(x.shape[1], len(np.unique(y)))
    nn.add_layer(50, ReLU)
    nn.add_output_layer(activation=softmax)    
    t1 = time.time()    
    _, total_iters = nn.learn_by_genetic_algorithm(x_train, y_train)
    z = nn.predict(x_test)
    t2 = time.time()
    z = nn.predict(x_test)
    p = nn.predict_proba(x_test)
    
    acc_ga.append(accuracy_score(_y_test, z))
    f1_ga.append(f1_score(_y_test, z))
    auc_ga.append(roc_auc_score(_y_test, p[:,1]))
    t_ga.append((t2-t1) / total_iters)
    
    
print('learning by randomized hill climbing, 5-fold CV average, test acc = %.4f, f1 = %.4f, auc = %.4f, time/iter = %.3f'
      %(np.mean(acc_hc), np.mean(f1_hc), np.mean(auc_hc), np.mean(t_hc)))
print('learning by simulated annealing     , 5-fold CV average, test acc = %.4f, f1 = %.4f, auc = %.4f, time/iter = %.3f'
      %(np.mean(acc_sa), np.mean(f1_sa), np.mean(auc_sa), np.mean(t_sa)))
print('learning by genetic algorithm       , 5-fold CV average, test acc = %.4f, f1 = %.4f, auc = %.4f, time/iter = %.3f'
      %(np.mean(acc_ga), np.mean(f1_ga), np.mean(auc_ga), np.mean(t_ga)))