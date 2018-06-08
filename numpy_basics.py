# import numpy as np 

# # Create a 1D array of uint-8 (0-255) integers
# a = np.array([1,2,3,4,5], dtype='uint8')
# print(a)
# print()

# # Convert a python list to a numpy array (defaults to int64 or float64)
# l = [5,6,7,8,9]
# print(type(l))
# l = np.asarray(l, dtype='uint8')
# print(type(l))
# print(type(l[0]))
# print()

# # Convert numpy array back to a python list
# l = l.tolist()
# print(type(l))
# print(type(l[0]))
# print()

# # Cast 'uint8' to 'float32'
# a_asfloat = a.astype('float32')
# print(type(a[0]))
# print(type(a_asfloat[0]))
# print()

##################### Generating data sets #####################
import numpy as np 

def print_array(arr_name, arr):
	print(arr_name, " = \n")
	for item in arr:
		print(" ", item)
	print()

# Seed the random generator for repeatable results
np.random.seed()# <-- un-seed at any time by running: np.random.seed()

""" Uniform Distributions """
# Generate a numpy array of 'n' uniformly-distributed floats between 0(inclusive) and 10(exclusive)
n=10
uniform_floats = np.random.uniform(0, 100, n)
print_array('uniform_floats', uniform_floats)

# Generate 'n' uniformly-distributed ints between 0(inclusive) and 10(exclusive)
uniform_ints = np.random.randint(0, 10, n, dtype='int8')
print_array('uniform_ints', uniform_ints)

# Generate 'n' normally-distributed floats between 0(inclusive) and 10(exclusive)
n=10
mu = 0.0 # <-- mean-centered distribution about 'loc'
std_dev = 100.0 # <-- min = -100.0,  max = 100.0
normal_floats = np.random.normal(mu, std_dev, n)
print_array('normal_floats', normal_floats)

# NOTE: true values get closer to ideal values as n-->inf
ideal_mu = mu
true_mu = np.mean(normal_floats)
print("ideal_mu = ", ideal_mu)
print("true__mu = ", true_mu)
print()

ideal_std_dev = std_dev
true_std_dev = np.std(normal_floats)
print("ideal_std_dev = ", ideal_std_dev)
print("true__std_dev = ", true_std_dev)
print()

# Generate 'n' uniformly-distributed ints between 0(inclusive) and 10(exclusive)
# uniform_ints = np.random.randint(0, 10, n, dtype='int8')
# print_array('uniform_ints', uniform_ints)
