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
nn = neural_network(x.shape[1], len(np.unique(y)))
nn.add_layer(50, ReLU)
nn.add_output_layer(activation=softmax)
loss_curve1, _ = nn.learn_by_simulated_annealing(x, y, init_temp=1e-2)
plt.plot(loss_curve1)

nn = neural_network(x.shape[1], len(np.unique(y)))
nn.add_layer(50, ReLU)
nn.add_output_layer(activation=softmax)
loss_curve2, _ = nn.learn_by_simulated_annealing(x, y, init_temp=5e-2)
plt.plot(loss_curve2)

nn = neural_network(x.shape[1], len(np.unique(y)))
nn.add_layer(50, ReLU)
nn.add_output_layer(activation=softmax)
loss_curve3, _ = nn.learn_by_simulated_annealing(x, y, init_temp=1e-3)
_y = np.argmax(y, axis=1)
plt.plot(loss_curve3)

nn = neural_network(x.shape[1], len(np.unique(y)))
nn.add_layer(50, ReLU)
nn.add_output_layer(activation=softmax)
loss_curve4, _ = nn.learn_by_simulated_annealing(x, y, init_temp=5e-3)
_y = np.argmax(y, axis=1)
plt.plot(loss_curve4)

plt.xlabel('iters')
plt.ylabel('cross entropy')
plt.legend(['init_temp = 1e-2', 'init_temp = 5e-2', 'init_temp = 1e-3', 'init_temp = 5e-3'])
plt.show()