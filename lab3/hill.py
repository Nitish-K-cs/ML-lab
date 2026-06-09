def objective_function(x):
    return -x**2 + 5


def hill_climbing(start, step_size, max_iterations):
    current = start

    for i in range(max_iterations):
        left = current - step_size
        right = current + step_size

        current_value = objective_function(current)
        left_value = objective_function(left)
        right_value = objective_function(right)

        if left_value > current_value:
            current = left
        elif right_value > current_value:
            current = right
        else:
            break

    return current, objective_function(current)


start = float(input("Enter starting value: "))
step = float(input("Enter step size: "))
iterations = int(input("Enter max iterations: "))

solution, value = hill_climbing(start, step, iterations)

print("Optimal Solution:", solution)
print("Optimal Value:", value)


code = """
Enter starting value: 3
Enter step size: 1
Enter max iterations: 10

Output
Optimal Solution: 0.0
Optimal Value: 5.0

"""
