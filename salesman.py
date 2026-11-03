import random

# Distance matrix
dist = [
    [0, 10, 15, 20, 18, 12],
    [10, 0, 35, 25, 17, 28],
    [15, 35, 0, 30, 28, 20],
    [20, 25, 30, 0, 22, 16],
    [18, 17, 28, 22, 0, 14],
    [12, 28, 20, 16, 14, 0]
]

cities = ['A', 'B', 'C', 'D', 'E', 'F']

k = 4
iterations = 20

# Calculate total tour cost
def cost(tour):
    total = 0

    for i in range(len(tour)):
        total += dist[tour[i]][tour[(i + 1) % len(tour)]]

    return total


# Generate neighbours using swap operation
def neighbours(tour):
    result = []

    for i in range(1, len(tour)):
        for j in range(i + 1, len(tour)):
            new_tour = tour[:]

            new_tour[i], new_tour[j] = (
                new_tour[j], new_tour[i]
            )

            result.append(new_tour)

    return result


# Generate initial random tours
beam = []

while len(beam) < k:
    tour = [0] + random.sample(
        [1, 2, 3, 4, 5], 5
    )

    if tour not in beam:
        beam.append(tour)


# Global best solution
best_tour = min(beam, key=cost)
best_cost = cost(best_tour)

print("Beam Width:", k)

# Local Beam Search
for iteration in range(1, iterations + 1):

    successors = []

    # Generate neighbours of every tour
    for tour in beam:
        successors.extend(neighbours(tour))

    # Remove duplicate tours
    unique = []

    for tour in successors:
        if tour not in unique:
            unique.append(tour)

    # Sort tours according to cost
    unique.sort(key=cost)

    # Select best k tours
    beam = unique[:k]

    # Update global best
    current_best = min(beam, key=cost)

    if cost(current_best) < best_cost:
        best_tour = current_best
        best_cost = cost(best_tour)

    print(
        "Iteration:", iteration,
        "Current Best:", cost(current_best),
        "Global Best:", best_cost
    )

# Display final result
print("\nFinal Best Tour:")

for city in best_tour:
    print(cities[city], end=" -> ")

print(cities[best_tour[0]])

print("Total Distance:", best_cost)