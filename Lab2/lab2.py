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


# Global kernel matrix
K = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        K[i, j] = targets[i] * targets[j] * linear_kernel(inputs[i], inputs[j])

def objective(alpha):
    return -np.sum(alpha) + 0.5 * np.dot(alpha, np.dot(K, alpha))

# 0 ≤αi ≤C ∀i and ∑alpha_i*t_i = 0 
def zerofun(alpha):
    return np.dot(alpha, targets)


XC = ({'type': 'eq', 'fun': zerofun})
start = np.zeros(N)
C = 1
B = [(0, C) for b in range(N)]


ret = minimize(objective, start, bounds=B, constraints=XC)
alpha = ret['x']

print("success" if ret['success'] else "failed")

for i in range(len(alpha)):
    if abs(alpha[i]) > 1e-5:
        non_zeros=(alpha[i],inputs[i],targets[i])

def b_value(non_zeros):
    b = 0
    for i in range(len(non_zeros)):
        pass

b = b_value(non_zeros)
print(b)