import random
import math
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np

# Kernels
# Linear kernel, dot product of x and y
def linear_kernel(x, y):
    return np.dot(x, y)

# Polynomial kernel of degree p
def polynomial_kernel(x, y, p=3):
    return (np.dot(x, y) + 1) ** p

# Radial basis function (RBF) kernel
def rbf_kernel(x, y, sigma=3):
    return np.exp(-np.linalg.norm(x - y) ** 2 / (2 * sigma ** 2))

# SVM objective function, one parameter so that the "minimize" function can find the value for alpha that minimizes the return
# Equation (4) in the lab instructions
def objective(alpha):
    return -np.sum(alpha) + 0.5 * np.dot(alpha, np.dot(P, alpha))

# Constraint function: ∑ alpha_i * t_i = 0 
# Equation (10) in the lab instructions
def zerofun(alpha):
    return np.dot(alpha, targets)

# b value for the decision boundary
# Equation (7) in the lab instructions
# ∑(alpha_i * t_i * K(x_1, x_i)) - t_1
def b_value(non_zeros):
    b = 0
    for i in range(len(non_zeros)):
        b += non_zeros[i][0] * non_zeros[i][2] * kernel(non_zeros[0][1], non_zeros[i][1])
    return b - non_zeros[0][2]

# Indicator function for classification
# Equation (6) in the lab instructions
def indicator(s):
    result = 0
    for i in range(len(non_zeros)):
        result += non_zeros[i][0] * non_zeros[i][2] * kernel(s, non_zeros[i][1])
    return result - b_value(non_zeros)

#global variable for the chosen kernel function to use
kernel = linear_kernel

# Generate data for class A and class B
# classA is a 20x2 matrix with 10 samples centered at [1.5, 0.5] and 10 samples centered at [-1.5, 0.5]
# classB is a 20x2 matrix with 20 samples centered at [0.0, -0.5]
# STD is 0.2 for both classes
classA = np.concatenate((np.random.randn(10, 2) * 0.2 + [1.5, 0.5], 
                            np.random.randn(10, 2) * 0.2 + [-1.5, 0.5]))
classB = np.random.randn(20, 2) * 0.2 + [0.0, -0.5]

inputs = np.concatenate((classA, classB))
targets = np.concatenate((np.ones(classA.shape[0]), -np.ones(classB.shape[0])))
N = inputs.shape[0] # Number of rows (samples)

# Randomly shuffle the data
permute = list(range(N))
random.shuffle(permute)
inputs = inputs[permute, :]
targets = targets[permute]

# Pre computed kernel matrix P_ij = t_i * t_j * K(x_i, x_j), Helper function for objective function
P = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        P[i, j] = targets[i] * targets[j] * kernel(inputs[i], inputs[j])

# Set up parameters for minimize
start = np.zeros(N)
C = 1.5  # Slack variable C for soft margin SVM
B = [(0, C) for b in range(N)]
XC = {'type': 'eq', 'fun': zerofun}

# Call minimize function to solve for alpha
ret = minimize(objective, start, bounds=B, constraints=XC)
alpha = ret['x']

# Extract support vectors (those where alpha > 1e-5)
non_zeros = []
for i in range(len(alpha)):
    if abs(alpha[i]) > 1e-5:
        non_zeros.append((alpha[i], inputs[i], targets[i]))

# Plot the data points
plt.plot([p[0] for p in classA], [p[1] for p in classA], 'b.')
plt.plot([p[0] for p in classB], [p[1] for p in classB], 'r.')
plt.axis('equal')



# Plot the decision boundary and margins
xgrid = np.linspace(-5, 5)
ygrid = np.linspace(-4, 4)
grid = np.array([[indicator(np.array([x, y])) for x in xgrid] for y in ygrid])

plt.contour(xgrid, ygrid, grid, (-1.0, 0.0, 1.0), colors=('red', 'black', 'blue'), linewidths=(1, 3, 1))
plt.savefig('svmplot.pdf')
plt.show()

