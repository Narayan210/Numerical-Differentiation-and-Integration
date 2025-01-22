import numpy as np

def romberg_integration(f, a, b, n):
    """
    Perform Romberg integration to approximate the integral of f(x) from a to b.
    
    Parameters:
    f: callable
        Function to integrate.
    a: float
        Lower limit of integration.
    b: float
        Upper limit of integration.
    n: int
        Number of levels of Romberg integration.
        
    Returns:
    np.ndarray
        Romberg integration table.
    """
    R = np.zeros((n, n))
    
    # Trapezoidal rule for R[0, 0]
    R[0, 0] = (b - a) * (f(a) + f(b)) / 2.0
    
    # Fill the Romberg table
    for i in range(1, n):
        # Step size for the trapezoidal rule at this level
        h = (b - a) / (2 ** i)
        # Trapezoidal approximation
        sum_trap = sum(f(a + (2 * k - 1) * h) for k in range(1, 2 ** (i - 1) + 1))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_trap
        
        # Richardson extrapolation
        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4 ** j - 1)
    
    return R

# Define the function to integrate
def integrand(x):
    if x == 0:
        return 0  # Define value at x=0 to avoid division by zero
    return (np.sin(x) ** 2) / x

# Set parameters
a, b = 0, 1  # Integration bounds
n = 5        # Levels of Romberg integration

# Compute the Romberg integration table
romberg_table = romberg_integration(integrand, a, b, n)

# Print the Romberg table
print("Romberg Integration Table:")
print(romberg_table)

# Most accurate result (last cell of the last row)
result = romberg_table[-1, -1]
print(f"\nApproximate value of the integral: {result}")
