
import math
import matplotlib.pyplot as plt


def bisection_method(func, a, b, epsilon):
    if func(a) * func(b) >= 0:
        print("Error")
        return None

    iteration = 1
    x_values = []

    while (b - a) / 2 > epsilon:
        x = (a + b) / 2
        x_values.append(x)

        print(f"{iteration}-iteration: x = {x:.6f} a = {a:.6f} b = {b:.6f} f(x) = {func(x):.6f}")

        if func(x) * func(a) < 0:
            b = x
        else:
            a = x

        iteration += 1

    print(f"\nRoot: x = {x:.6f} found in {iteration} iterations.")
    return x, x_values


def false_position_method(func, a, b, epsilon):
    if func(a) * func(b) >= 0:
        print("Error")
        return None

    iteration = 1
    x_values = []

    while True:
        x = (a * func(b) - b * func(a)) / (func(b) - func(a))
        x_values.append(x)

        print(f"{iteration}-iteration: x = {x:.6f} a = {a:.6f} b = {b:.6f} f(x) = {func(x):.6f}")

        if abs(func(x)) < epsilon or abs(b - a) < epsilon:
            break

        if func(x) * func(a) < 0:
            b = x
        else:
            a = x

        iteration += 1

    print(f"\nRoot: x = {x:.6f} found in {iteration} iterations.")
    return x, x_values


def iteration_method(func, g_func, x0, epsilon):
    iteration = 1
    x_values = [x0]

    while True:
        x1 = g_func(x0)
        x_values.append(x1)

        print(f"{iteration}-iteration: x = {x1:.6f} f(x) = {func(x1):.6f}")

        if abs(x1 - x0) < epsilon:
            break

        x0 = x1
        iteration += 1

    print(f"\nRoot: x = {x1:.6f} found in {iteration} iterations.")
    return x1, x_values


def newton_raphson_method(func, d_func, x0, epsilon):
    iteration = 1
    x_values = [x0]

    while True:
        x1 = x0 - func(x0) / d_func(x0)
        x_values.append(x1)

        print(f"{iteration}-iteration: x = {x1:.6f} f(x) = {func(x1):.6f}")

        if abs(x1 - x0) < epsilon:
            break

        x0 = x1
        iteration += 1

    print(f"\nRoot: x = {x1:.6f} found in {iteration} iterations.")
    return x1, x_values


func = lambda x: x * math.exp(x) - 1
g_func = lambda x: 1 / math.exp(x)

d_func = lambda x: math.exp(x) * (x + 1)

a = float(input("Enter number for a: "))
b = float(input("Enter number for b: "))
x0 = float(input("Enter initial guess for x0: "))
epsilon = float(input("Enter a epsilon: "))

print("\nBisection Method:")
bisection_root, bisection_x_values = bisection_method(func, a, b, epsilon)

print("\nMethod of False Position:")
false_position_root, false_position_x_values = false_position_method(func, a, b, epsilon)

print("\nIteration Method:")
iteration_root, iteration_x_values = iteration_method(func, g_func, x0, epsilon)

print("\nNewton-Raphson Method:")
newton_raphson_root, newton_raphson_x_values = newton_raphson_method(func, d_func, x0, epsilon)

plt.figure(figsize=(12, 8))

plt.plot(range(1, len(bisection_x_values) + 1), bisection_x_values, marker='o', label='Bisection Method')

plt.plot(range(1, len(false_position_x_values) + 1), false_position_x_values, marker='s', label='False Position Method')

plt.plot(range(1, len(iteration_x_values) + 1), iteration_x_values, marker='^', label='Iteration Method')

plt.plot(range(1, len(newton_raphson_x_values) + 1), newton_raphson_x_values, marker='x', label='Newton-Raphson Method')

plt.title('Convergence of Root Finding Methods')
plt.xlabel('Iteration')
plt.ylabel('x Value')
plt.grid(True)
plt.legend()
plt.show()