import numpy as np

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

def romberg_integration(f, a, b, tol=1e-6):
    R = [[0]]
    n = 1
    h = b - a
    R[0][0] = h * (f(a) + f(b)) / 2

    while True:
        h /= 2
        n *= 2
        trapezoid_sum = sum(f(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1))
        R.append([0] * (len(R[-1]) + 1))
        R[-1][0] = R[-2][0] / 2 + h * trapezoid_sum

        for k in range(1, len(R[-1])):
            R[-1][k] = R[-1][k - 1] + (R[-1][k - 1] - R[-2][k - 1]) / (4**k - 1)

        if abs(R[-1][-1] - R[-2][-2]) < tol:
            return R[-1][-1]

def double_integral_trapezoidal(f, x_range, y_range, nx, ny):
    x = np.linspace(x_range[0], x_range[1], nx + 1)
    y = np.linspace(y_range[0], y_range[1], ny + 1)
    hx = (x_range[1] - x_range[0]) / nx
    hy = (y_range[1] - y_range[0]) / ny

    integral = 0
    for i in range(nx + 1):
        for j in range(ny + 1):
            weight = 1
            if i == 0 or i == nx:
                weight /= 2
            if j == 0 or j == ny:
                weight /= 2
            integral += weight * f(x[i], y[j])

    return integral * hx * hy

def double_integral_simpsons_one_third(f, x_range, y_range, nx, ny):
    if nx % 2 != 0 or ny % 2 != 0:
        raise ValueError("Simpson's 1/3 rule requires an even number of intervals in both directions.")

    x = np.linspace(x_range[0], x_range[1], nx + 1)
    y = np.linspace(y_range[0], y_range[1], ny + 1)
    hx = (x_range[1] - x_range[0]) / nx
    hy = (y_range[1] - y_range[0]) / ny

    integral = 0
    for i in range(nx + 1):
        for j in range(ny + 1):
            wx = 1
            wy = 1
            if i == 0 or i == nx:
                wx = 1
            elif i % 2 == 0:
                wx = 2
            else:
                wx = 4

            if j == 0 or j == ny:
                wy = 1
            elif j % 2 == 0:
                wy = 2
            else:
                wy = 4

            integral += wx * wy * f(x[i], y[j])

    return integral * hx * hy / 9

# Define the function to integrate
f = lambda x, y: x * y**2

# Integration ranges
x_range = (0, 1)
y_range = (0, 1)

# Number of segments
nx, ny = 4, 4

# Perform double integration
trapezoidal_result = double_integral_trapezoidal(f, x_range, y_range, nx, ny)
simpsons_result = double_integral_simpsons_one_third(f, x_range, y_range, nx, ny)

print(f"Double Integral using Trapezoidal Rule: {trapezoidal_result:.6f}")
print(f"Double Integral using Simpson's 1/3 Rule: {simpsons_result:.6f}")
