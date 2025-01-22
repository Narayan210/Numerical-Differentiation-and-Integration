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

# Define the function to integrate
f = lambda x: 1 + x**3

# Integration range
a, b = 0, 1

# Perform Romberg integration
romberg_result = romberg_integration(f, a, b)
print(f"Romberg Integration Result: {romberg_result:.6f}")

# Perform integration for 8 segments using other methods
segments = 8
print(f"\nUsing {segments} segments:")
def integrate_using_methods(a, b, segments):
    x = np.linspace(a, b, segments + 1)
    y = f(x)

    try:
        trap_result = trapezoidal_rule(x, y)
        print(f"Trapezoidal Rule with {segments} segments: {trap_result:.6f}")
    except Exception as e:
        print(e)

    try:
        simp_1_3_result = simpsons_one_third_rule(x, y)
        print(f"Simpson's 1/3 Rule with {segments} segments: {simp_1_3_result:.6f}")
    except Exception as e:
        print(e)

    try:
        simp_3_8_result = simpsons_three_eighth_rule(x, y)
        print(f"Simpson's 3/8 Rule with {segments} segments: {simp_3_8_result:.6f}")
    except Exception as e:
        print(e)

integrate_using_methods(a, b, segments)
