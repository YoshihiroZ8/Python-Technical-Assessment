# This script demonsrtates using numpy for array operations
import numpy as np
import pandas as pd
import os

#--- Part 1: Using Numpy
print("---Using NumPy ---")
# Create a NumPy array
numpy_arr1 = np.array([1, 2, 3, 4, 5])
print(f"1D NumPy Array: {numpy_arr1}")

numpy_arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2D NumPy Array:\n{numpy_arr2}")

array_a = np.array([10, 20, 30])
array_b = np.array([1, 2, 3])

#addition 
sum_array = array_a + array_b
print(f"Array Addition (sum): {sum_array}")

#multiplication
product_array = array_a * array_b
print(f"Array Multiplication (product): {product_array}")

#scalar multiplication
scaled_array = array_a * 2
print(f"Scalar Multiplication ({array_a} * 2): {scaled_array}")

#Using NumPy functions
print(f"Sum of array_a: {np.sum(array_a)}")
print(f"Mean of array_a: {np.mean(array_a)}")
