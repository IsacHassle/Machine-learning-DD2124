import random , math
from scipy . optimize import minimize
import matplotlib . pyplot as plt
import numpy as np


def linear_kernel(x, y):
    # Linear kernel, dot product of x and y
    return np.dot(x, y)

def polynomial_kernel(x, y, p):
    # Polynomial kernel of degree p
    return (np.dot(x, y) + 1) ** p

def rbf_kernel(x, y, sigma):
    # Radial basis function (RBF) kernel
    # K(x, y) = exp(-||x - y||^2 / (2 * sigma^2))
    # where ||x - y|| is the Euclidean distance between x and y,
    # and sigma controls the width of the Gaussian distribution
    return math.exp(-linalg.norm(x-y)**2 / (2*sigma**2))


def kernel_matrix(X, t, kernel_func):
    n = len(X)
    K = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            K[i, j] = t[i] * t[j] * kernel_func(X[i], X[j])
    return K

def objective(alpha, precomputed_K):
    return -np.sum(alpha) + 0.5 * np.dot(alpha, np.dot(precomputed_K, alpha))


def zerofun(alpha):
    return np.sum(alpha, t)

