import numpy as np

def xavier(n_in, n_out):
    '''
    xavier initialization method
    refer to Eq. (16) in [http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf]
    '''
    return np.random.uniform(-np.sqrt(6./(n_in+n_out)), np.sqrt(6./(n_in+n_out)), size=[n_in, n_out])

def func_deriv(func):
    '''
    get the function derivation according to func.__name__
    '''
    return eval(func.__name__ + '_deriv')

def idt(x):
    '''
    identity transformation
    '''
    return x

def idt_deriv(out):
    '''
    the derivation of identity transformation
    '''
    return 1.

def ReLU(x):
    '''
    recitified linear unit
    refer to Sec 3.1 in [http://proceedings.mlr.press/v15/glorot11a/glorot11a.pdf]
    '''
    return x*(x>0)

def ReLU_deriv(out):
    '''
    the derivation of ReLU
    '''
    return out > 0

def tanh(x):
    return np.tanh(x)

def tanh_deriv(out):
    '''
    the derivation of tanh()
    '''
    return 1. - out ** 2

def sigmoid(x):
    return 1. / (1. + np.exp(-x))

def sigmoid_deriv(out):
    '''
    the derivation of sigmoid()
    '''
    return out * (1. - out)

def mean_square_error(t, z):
    # mean square error as loss function
    # t: target, N x d, in which
    #      the first dimension N is the number of samples,
    #      the second dimension if the number of outputs
    # z: prediction, N x d
    return 0.5 * np.mean(np.linalg.norm(t-z, axis=1))

def mean_square_error_deriv(t, z):
    # the deriviatives of mean square error function
    return t - z

def cross_entropy(t, z):
    # cross entropy as loss function
    #   use cross entropy in multi-class classification task,
    #   i.e., each item of t is either 0 or 1
    # t: target, N x d
    # z: prediction, N x d
    return -np.mean(np.sum(t * np.log(z), axis=1))

def softmax(x):
    x = np.atleast_2d(x)
    x = np.exp(x)
    for i in range(x.shape[0]):
        x[i,:] /= x[i,:].sum()
    return x

def cross_entropy_deriv(t, z):
    # the deriviatives of cross entropy function
    return t - z

def add_bias_dim(x):
    # add a bias dimension to the input
    x = np.atleast_2d(x)
    x = np.concatenate((x, np.ones([x.shape[0], 1])), axis=1)
    return x
    
def OneHotEncoding(label):
    # label is a list of length N, can be numbers or strings
    # return a binary representation of label, as well as the reverse index
    # e.g.
    # >>> label = [0, 1, 3, 4]
    # >>> y, rind = OneHotEncoding(label)
    # >>> y
    # [[1, 0, 0, 0],
    #  [0, 1, 0, 0],
    #  [0, 0, 1, 0],
    #  [0, 0, 0, 1]]
    # >>> rind
    # {0:0, 1:1, 2:3, 3:4}
    #
    # >>> label = ['c1', 'c2', 'c3']
    # >>> y, rind = OneHotEncoding(label)
    # >>> y
    # [[1, 0, 0],
    #  [0, 1, 0],
    #  [0, 0, 1]]
    # >>> rind
    # {0:'c1', 1:'c2', 2:'c3'}
    label_dict = {_label:i for i, _label in enumerate(np.unique(label))}
    y = np.zeros((len(label), len(label_dict)))
    for i, _label in enumerate(label):
        y[i][label_dict[_label]] = 1
    reverse_index = {v:k for k, v in label_dict.items()}
    return y, reverse_index