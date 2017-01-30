# This file shows how to write a first script with numpy
import numpy as np

A = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
X = np.array([2, 3, 4, 5])
B = A.dot(X)
X2 = X.dot(X)

print "Matrix A:"
print A
print "Vector X:"
print X
print "Vector B = A * X:"
print B
print "Vector X * X:"
print X2
print "Matrix A^T:"
print A.T
