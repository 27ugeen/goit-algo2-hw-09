import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    solution = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    best_value = func(solution)

    for _ in range(iterations):
        candidate = [solution[i] + random.uniform(-0.1, 0.1) for i in range(dim)]
        candidate = [max(bounds[i][0], min(bounds[i][1], candidate[i])) for i in range(dim)]

        candidate_value = func(candidate)
        if candidate_value < best_value:
            solution, best_value = candidate, candidate_value

        if abs(candidate_value - best_value) < epsilon:
            break

    return solution, best_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    best_solution = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    best_value = func(best_solution)

    for _ in range(iterations):
        candidate = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            best_solution, best_value = candidate, candidate_value

        if abs(candidate_value - best_value) < epsilon:
            break

    return best_solution, best_value


# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    dim = len(bounds)
    solution = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    best_value = func(solution)

    for i in range(iterations):
        candidate = [solution[j] + random.uniform(-0.5, 0.5) for j in range(dim)]
        candidate = [max(bounds[j][0], min(bounds[j][1], candidate[j])) for j in range(dim)]

        candidate_value = func(candidate)
        delta = candidate_value - best_value

        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temp):
            solution, best_value = candidate, candidate_value

        temp *= cooling_rate
        if temp < epsilon:
            break

    return solution, best_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)