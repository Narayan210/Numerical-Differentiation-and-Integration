import numpy as np

def divided_difference_table(x, y):
    n = len(y)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (x[i + j] - x[i])

    return table

def newton_divided_difference(x, y, value):
    table = divided_difference_table(x, y)
    n = len(x)
    result = y[0]
    term = 1

    for i in range(1, n):
        term *= (value - x[i - 1])
        result += term * table[0, i]

    return result

# Input data
x = np.array([2, 4, 9, 10])
y = np.array([4, 56, 711, 980])

# Value to interpolate
value = 5

# Perform interpolation
result = newton_divided_difference(x, y, value)

print("Newton's Divided Difference result at x=5:", result)
