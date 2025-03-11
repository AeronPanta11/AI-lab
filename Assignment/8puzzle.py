
from heapq import heappush, heappop


initial_state = [
    [3, 1, 2],
    [4, 0, 5],
    [6, 7, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Heuristic 1: Count the number of misplaced tiles


def h1(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j] and state[i][j] != 0:
                count += 1
    return count

# Heuristic 2: Calculate the Manhattan distance


def h2(state, goal):
    distance = 0
    n = len(state)
    goal_positions = {}
    for i in range(n):
        for j in range(n):
            goal_positions[goal[i][j]] = (i, j)

    for i in range(n):
        for j in range(n):
            tile = state[i][j]
            if tile != 0:
                goal_row, goal_col = goal_positions[tile]
                distance += abs(i - goal_row) + abs(j - goal_col)

    return distance

# Move the blank tile


def move_blank(state, direction):
    new_state = [row[:] for row in state]  
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if direction == 'up' and i > 0:
                    new_state[i][j], new_state[i -
                                               1][j] = new_state[i-1][j], new_state[i][j]
                elif direction == 'down' and i < 2:
                    new_state[i][j], new_state[i +
                                               1][j] = new_state[i+1][j], new_state[i][j]
                elif direction == 'left' and j > 0:
                    new_state[i][j], new_state[i][j -
                                                  1] = new_state[i][j-1], new_state[i][j]
                elif direction == 'right' and j < 2:
                    new_state[i][j], new_state[i][j +
                                                  1] = new_state[i][j+1], new_state[i][j]
                else:
                    return None
                return new_state
    return None

# Get all possible moves


def get_nodes(state):
    directions = ['up', 'down', 'left', 'right']
    nodes = []
    for direction in directions:
        node = move_blank(state, direction)
        if node:
            nodes.append((node, direction))  
    return nodes

# A* algorithm to solve the 8-puzzle


def a_star_8_puzzle(initial, goal):
    open_set = []
    heappush(open_set, (0, initial, []))  
    visited = set()
    g_cost = {str(initial): 0}

    while open_set:
        _, current, path = heappop(open_set)  
        if current == goal:
            print("Goal State Reached!")
            for step, (move, state) in enumerate(path, start=1):
                print(f"\nMove {step}: {move}")
                for row in state:
                    print(row)
            print("\nFinal State:")
            for row in current:
                print(row)
            return

        visited.add(str(current))
        for node, move in get_nodes(current):
            if str(node) in visited:
                continue

            new_g = g_cost[str(current)] + 1
            h = h1(node, goal) + h2(node, goal)
            f = new_g + h
            if str(node) not in g_cost or new_g < g_cost[str(node)]:
                g_cost[str(node)] = new_g
                heappush(open_set, (f, node, path + [(move, node)]))

    print("No Solution Found")


# Run the A* algorithm
a_star_8_puzzle(initial_state, goal_state)
