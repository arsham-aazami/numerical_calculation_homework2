import numpy as np
from scipy.interpolate import lagrange

def find_approximating_polynomial(x, y):
    polynomial = lagrange(x, y)
    return polynomial

def find_polynomial_roots(polynomial):
    roots = np.roots(polynomial)
    return roots

def generate_approximating_table(x, y, roots):
    polynomial = find_approximating_polynomial(x, y)
    roots = find_polynomial_roots(polynomial)
    table = [polynomial(root) for root in roots]
    return table

def calculate_difference(x, y, table):
    difference = abs(y - table[0])
    return difference

# Define the function values
xi_values = [1.0, 1.3, 1.6, 1.9, 2.2]
fi_values = [0.765128, 0.620086, 0.455402, 0.281819, 0.110363]

# Find the approximating polynomial
polynomial = find_approximating_polynomial(xi_values, fi_values)

# Find the roots of the approximating polynomial
roots = find_polynomial_roots(polynomial)

# Generate the approximating table for the original function
table = generate_approximating_table(xi_values, fi_values, roots)

# Calculate the absolute value of the difference between the original function and its approximating table at point 0 (i.e., xi[0])
difference = calculate_difference(xi_values[0], fi_values[0], table)

print("Approximating polynomial:", polynomial)
print("Roots of the approximating polynomial:", roots)
print("Approximating table:", table)
print("Difference at point 0:", difference)
