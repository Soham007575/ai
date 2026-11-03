# DFS for Water Jug Problem

capacity1 = 4
capacity2 = 3

start = (0, 0)
goal = (2, 0)


# Generate possible states
def get_neighbors(x, y):

    states = []

    # Fill 4-litre jug
    states.append((4, y))

    # Fill 3-litre jug
    states.append((x, 3))

    # Empty 4-litre jug
    states.append((0, y))

    # Empty 3-litre jug
    states.append((x, 0))

    # Pour 4-litre jug into 3-litre jug
    pour = min(x, 3 - y)
    states.append((x - pour, y + pour))

    # Pour 3-litre jug into 4-litre jug
    pour = min(y, 4 - x)
    states.append((x + pour, y - pour))

    return states


# DFS algorithm
def dfs(start, goal):

    stack = [(start, [start])]

    visited = set()

    while stack:

        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        # Check goal
        if state == goal:
            return path

        x, y = state

        # Generate successor states
        for neighbor in get_neighbors(x, y):

            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


# Run DFS
path = dfs(start, goal)

if path:

    print("Solution Found!")

    for state in path:
        print(state)

    print("Total Steps:", len(path) - 1)

else:
    print("No solution found")B