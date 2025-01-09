def gaussian_elimination(A, B):
    n = len(A)

    # Целочисленным не место! Преобразование всех значений в float
    for i in range(n):
        A[i] = [float(a) for a in A[i]]
        B[i] = float(B[i])

    # Преобразование в U матрицу
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]

    # Обратная подстановка
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = B[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x

def jacobi_method(A, B, iterations=25, tolerance=1e-10):
    n = len(A)
    x = [0] * n  # ты просто нулевой вектор

    for iteration in range(iterations):
        x_new = [0] * n
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (B[i] - s) / A[i][i]  # Обнова

        print(f"Iteration {iteration+1}: x = {x_new}")

        if max(abs(x_new[i] - x[i]) for i in range(n)) <= tolerance:
            print(f"Jacobi Method сошелся за {iteration+1} итераций.")
            return x_new

        x = x_new  # Сенкью некст

    return x

def gauss_seidel_method(A, B, iterations=25, tolerance=1e-10):
    n = len(A)
    x = [0] * n  # зум

    for iteration in range(iterations):
        x_new = x[:]
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (B[i] - s1 - s2) / A[i][i]

        print(f"Iteration {iteration+1}: x = {x_new}")

        if max(abs(x_new[i] - x[i]) for i in range(n)) <= tolerance:  # чек
            print(f"Gauss-Seidel Method сошелся за {iteration+1} итераций.")
            return x_new

        x = x_new  # Сенкью некст

    return x

def get_user_input():
    print("\nProvide your matrix row by row, separating numbers with spaces.")
    print("Example input for a 3x3 matrix:\n 6 1 1\n 4 -2 5\n 2 8 7")
    print("\nTo finish input, press Enter after the last row.")
    
    A = []
    while True:
        row = input("Enter row (or press Enter to finish): ")
        if row.strip() == "":
            break
        A.append(list(map(float, row.split())))

    if len(A) == 0:
        print("No valid matrix entered. Stopping existence.")
        exit()

    print("\nEnter the right-hand side values, separating numbers with spaces:")
    B = list(map(float, input().split()))
    if len(B) != len(A):
        print("Инвалид! The number of right-hand side values must match the number of equations.")
        exit()
    
    return A, B

def main():
    print("Choose a method to solve the system of linear equations:")
    print("1 - Gaussian Elimination")
    print("2 - Jacobi Method")
    print("3 - Gauss-Seidel Method")

    choice = input("Enter the method number: ")
    A, B = get_user_input()
    
    if choice == "1":
        result = gaussian_elimination(A, B)
        print("Solution using Gaussian Elimination:", result)
    elif choice == "2":
        result = jacobi_method(A, B)
        print("Solution using Jacobi Method:", result)
    elif choice == "3":
        result = gauss_seidel_method(A, B)
        print("Solution using Gauss-Seidel Method:", result)
    else:
        print("Инвалид - choice!")

if __name__ == "__main__":
    main()
