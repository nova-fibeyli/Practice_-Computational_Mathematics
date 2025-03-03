import math
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify

def bisection_method(func, a, b, epsilon):
    if func(a) * func(b) >= 0:
        print("Error: Function must have opposite signs.")
        return None, []
    iteration = 1
    x_values = []

    while (b - a) > epsilon:
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
        print("Error: Function must have opposite signs.")
        return None, []
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

def input_function_with_derivative():
    x = symbols('x')
    while True:
        equation = input("Enter the function (e.g., x**3 - x - 1): ")
        try:
            func_expr = eval(equation)
            d_func_expr = diff(func_expr, x)
            func = lambdify(x, func_expr, 'math')
            d_func = lambdify(x, d_func_expr, 'math')
            return func, d_func
        except Exception as e:
            print(f"Error: Invalid function. Please try again. ({e})")

while True:
    print("\nChoose a method:")
    print("1. Bisection Method")
    print("2. Method of False Position")
    print("3. Iteration Method")
    print("4. Newton-Raphson Method")
    print("5. Plot all methods")
    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        func, d_func = input_function_with_derivative()
        a = float(input("Enter number for a: "))
        b = float(input("Enter number for b: "))
        epsilon = float(input("Enter epsilon: "))
        x0 = float(input("Enter initial guess for x0: "))

        print("\nBisection Method:")
        bisection_root, bisection_x_values = bisection_method(func, a, b, epsilon)

        print("\nMethod of False Position:")
        false_position_root, false_position_x_values = false_position_method(func, a, b, epsilon)

        print("\nIteration Method:")
        iteration_root, iteration_x_values = iteration_method(func, lambda x: (x + 1) ** (1/3), x0, epsilon)

        print("\nNewton-Raphson Method:")
        newton_raphson_root, newton_raphson_x_values = newton_raphson_method(func, d_func, x0, epsilon)

        plt.figure(figsize=(10, 10))
        plt.plot(range(1, len(bisection_x_values) + 1), bisection_x_values, marker='o', label='Bisection Method')
        plt.plot(range(1, len(false_position_x_values) + 1), false_position_x_values, marker='o', label='False Position Method')
        plt.plot(range(1, len(iteration_x_values) + 1), iteration_x_values, marker='o', label='Iteration Method')
        plt.plot(range(1, len(newton_raphson_x_values) + 1), newton_raphson_x_values, marker='o', label='Newton-Raphson Method')
        plt.title('Root Finding Methods')
        plt.xlabel('Iteration')
        plt.ylabel('x Value')
        plt.grid(True)
        plt.legend()
        plt.show()

    elif choice in {"1", "2", "3", "4"}:
        func, d_func = input_function_with_derivative()

        if choice in {"1", "2"}:
            a = float(input("Enter number for a: "))
            b = float(input("Enter number for b: "))
            epsilon = float(input("Enter epsilon: "))

            if choice == "1":
                print("\nBisection Method:")
                root, x_values = bisection_method(func, a, b, epsilon)
            elif choice == "2":
                print("\nMethod of False Position:")
                root, x_values = false_position_method(func, a, b, epsilon)

        elif choice in {"3", "4"}:
            x0 = float(input("Enter initial guess for x0: "))
            epsilon = float(input("Enter epsilon: "))

            if choice == "3":
                print("\nIteration Method:")
                root, x_values = iteration_method(func, lambda x: (x + 1) ** (1/3), x0, epsilon)
            elif choice == "4":
                print("\nNewton-Raphson Method:")
                root, x_values = newton_raphson_method(func, d_func, x0, epsilon)

        if x_values:
            plt.plot(range(1, len(x_values) + 1), x_values, marker='o', label=f"Method {choice}")
            plt.title('Chosen Method:')
            plt.xlabel('Iteration')
            plt.ylabel('x Value')
            plt.grid(True)
            plt.legend()
            plt.show()

    else:
        print("Invalid. Try again.")
