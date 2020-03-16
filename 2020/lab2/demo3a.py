#https://machinelearningmastery.com/calculate-principal-component-analysis-scratch-python/
from numpy import genfromtxt
from numpy import mean
from numpy import cov
from numpy.linalg import eig
import numpy as np

# Load the dataset as a numpy array
data = genfromtxt('demo3b.csv', delimiter=',')

# Calculate the mean of each column in the dataset
M = mean(data.T, axis=1)

# Normalize the dataset by subtracting the mean from every column in the dataset
data_normal = data - M

# Calculate the covariance matrix of the normalized dataset
covariance = cov(data_normal.T)
print("The covariance matrix of the normalized data is the following: ")
print(covariance)
print()

# Find the eigenvalues and the eigenvectors of the covariance matrix
values, vectors = eig(covariance)
print("The eigenvalues of the normalized data are the following: ")
print(values)
print()

# Choose the most important eigenvalues and adjust eigenvectors accordingly
new_values = values[0:3]
print("The most important eigenvalues are the following: ")
print(new_values)
print()
new_vectors = vectors[0:3]
print("The most important eigenvectors are the following: ")
print(new_vectors)
print()

# Project the dataset to new eigenvectors to get the reduced dataset
new_data = new_vectors.dot(data_normal.T)

# Save the reduced dataset in a csv file
np.savetxt("foo.csv", new_data.T, delimiter=",")
