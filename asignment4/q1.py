import numpy as np

def forward_difference_table(x, y):
    n = len(y)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = table[i + 1, j - 1] - table[i, j - 1]

    return table

def backward_difference_table(x, y):
    n = len(y)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(j, n):
            table[i, j] = table[i, j - 1] - table[i - 1, j - 1]

    return table

def newton_forward_interpolation(x, y, value):
    h = x[1] - x[0]
    table = forward_difference_table(x, y)

    u = (value - x[0]) / h
    result = y[0]
    term = 1

    for i in range(1, len(x)):
        term *= (u - (i - 1))
        result += (term * table[0, i]) / np.math.factorial(i)

    return result

def newton_backward_interpolation(x, y, value):
    h = x[1] - x[0]
    table = backward_difference_table(x, y)

    u = (value - x[-1]) / h
    result = y[-1]
    term = 1

    for i in range(1, len(x)):
        term *= (u + (i - 1))
        result += (term * table[-1, i]) / np.math.factorial(i)

    return result

# Input data
x = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
y = np.array([1.0000, 0.9975, 0.9900, 0.9776, 0.8604])

# Value to interpolate
value = 0.25

# Perform interpolation using both methods
forward_result = newton_forward_interpolation(x, y, value)
backward_result = newton_backward_interpolation(x, y, value)

print("Newton's Forward Interpolation result:", forward_result)
print("Newton's Backward Interpolation result:", backward_result)
