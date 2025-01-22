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

def simpsons_one_third_rule(x, y):
    n = len(x) - 1
    if n % 2 != 0:
        raise ValueError("Simpson's 1/3 rule requires an even number of intervals.")

    h = (x[-1] - x[0]) / n
    result = y[0] + y[-1]

    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * y[i]
        else:
            result += 4 * y[i]

    return (h / 3) * result

def simpsons_three_eighth_rule(x, y):
    n = len(x) - 1
    if n % 3 != 0:
        raise ValueError("Simpson's 3/8 rule requires the number of intervals to be a multiple of 3.")

    h = (x[-1] - x[0]) / n
    result = y[0] + y[-1]

    for i in range(1, n):
        if i % 3 == 0:
            result += 2 * y[i]
        else:
            result += 3 * y[i]

    return (3 * h / 8) * result

def trapezoidal_rule(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    result = y[0] + y[-1]

    for i in range(1, n):
        result += 2 * y[i]

    return (h / 2) * result

# Input data for integration
x = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
y = np.array([1.0000, 0.9975, 0.9900, 0.9776, 0.8604])

# Extracting the range of integration from x = 1.8 to x = 3.4
x_range = np.arange(1.8, 3.5, 0.1)
y_range = np.array([1.0000, 0.9975, 0.9900, 0.9776, 0.8604])  # Example; replace with actual values corresponding to x_range

# Perform integration using all three methods
try:
    simpsons_1_3_result = simpsons_one_third_rule(x_range, y_range)
    print("Simpson's 1/3 Rule result:", simpsons_1_3_result)
except ValueError as e:
    print(e)

try:
    simpsons_3_8_result = simpsons_three_eighth_rule(x_range, y_range)
    print("Simpson's 3/8 Rule result:", simpsons_3_8_result)
except ValueError as e:
    print(e)

trapezoidal_result = trapezoidal_rule(x_range, y_range)
print("Trapezoidal Rule result:", trapezoidal_result)
