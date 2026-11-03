from collections import deque

# Initial and goal states
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Generate possible moves
def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    moves = [-3, 3, -1, 1]

    for move in moves:

        new_pos = zero + move

        if 0 <= new_pos < 9:

            # Check left and right boundary
            if move == -1 and zero % 3 == 0:
                continue

            if move == 1 and zero % 3 == 2:
                continue

            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# BFS algorithm
def bfs(start, goal):

    queue = deque([start])

    visited = {start}

    parent = {start: None}

    while queue:

        current = queue.popleft()

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for neighbor in get_neighbors(current):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    return None


# Solve the puzzle
path = bfs(start, goal)

if path:

    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for state in path:

        for i in range(0, 9, 3):
            print(state[i:i+3])

        print()

else:
    print("No solution found")