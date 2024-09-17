import random , math
from scipy . optimize import minimize
import matplotlib . pyplot as plt
import numpy as np


classA = np.concatenate((
    np.random.randn(10, 2) * 0.2 + [1.5, 0.5],
    np.random.randn(10, 2) * 0.2 + [-1.5, 0.5]
))

classB = np.random.randn(20, 2) * 0.2 + [0.0, -0.5]
inputs = np.concatenate((classA, classB))
targets = np.concatenate((
    np.ones(classA.shape[0]),
    -np.ones(classB.shape[0])
))

N = inputs.shape[0]  # Number of rows (samples)

permute = list(range(N))
random.shuffle(permute)
inputs = inputs[permute, :]
targets = targets[permute]

def linear_kernel(x, y):
    # Linear kernel, dot product of x and y
    return np.dot(x, y)

def polynomial_kernel(x, y, p):
    # Polynomial kernel of degree p
    return (np.dot(x, y) + 1) ** p

def rbf_kernel(x, y, sigma):
    # Radial basis function (RBF) kernel
    return np.exp(-np.linalg.norm(x-y)**2 / (2*sigma**2))


def kernel_matrix(kernel_func):
    K = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            K[i, j] = targets[i] * targets[j] * kernel_func(inputs[i], inputs[j])
    return K

def objective(alpha, precomputed_K):
    return -np.sum(alpha) + 0.5 * np.dot(alpha, np.dot(precomputed_K, alpha))


def zerofun(alpha):
    return np.sum(alpha, targets)



