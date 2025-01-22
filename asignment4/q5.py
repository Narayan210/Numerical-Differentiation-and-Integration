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

# Define the function to integrate
f = lambda x: x**3 + 2

# Function to compute integration using different methods and segment counts
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

# Integration range
a, b = 2, 4

# Perform integration for different segment counts
for segments in [2, 4, 6]:
    print(f"\nUsing {segments} segments:")
    integrate_using_methods(a, b, segments)
