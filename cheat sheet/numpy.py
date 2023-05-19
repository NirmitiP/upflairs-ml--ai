# ------------ numpy----------------
import numpy as np

# Creating a 1-dimensional array
a = np.array([1, 2, 3, 4, 5])

# Creating a 2-dimensional array
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Creating an array of zeros
c = np.zeros((3, 4))

# Creating an array of ones
d = np.ones((2, 3))

# Creating an identity matrix
e = np.eye(4)


# Accessing elements
a[0] # 1
b[1, 2] # 6

# Slicing arrays
a[1:4] # array([2, 3, 4])
b[:, 1] # array([2, 5, 8])


# Element-wise operations
a + 5 # array([6, 7, 8, 9, 10])
b * 2 # array([[ 2,  4,  6], [ 8, 10, 12], [14, 16, 18]])
c ** 2 # array([[0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 0.]])

# Dot product
f = np.array([1, 2, 3])
g = np.array([4, 5, 6])
h = np.dot(f, g) # 32


# Mean
np.mean(a) # 3.0
np.mean(b, axis=0) # array([4., 5., 6.])

# Standard deviation
np.std(a) # 1.41421356
np.std(b, axis=1) # array([0.81649658, 0.81649658, 0.81649658])

# Min and max
np.min(a) # 1
np.max(b) # 9
