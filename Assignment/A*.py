import heapq
import numpy as np

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost  # g
        self.heuristic = heuristic  # h
        self.total_cost = cost + heuristic  # f = g + h
    
    def __lt__(self, other):
        return self.total_cost < other.total_cost

def manhattan_distance(state, goal):
    distance = 0
    for num in range(1, 9):
        x1, y1 = np.where(state == num)
        x2, y2 = np.where(goal == num)
        distance += abs(x1[0] - x2[0]) + abs(y1[0] - y2[0])
    return distance

def get_neighbors(state):
    neighbors = []
    x, y = np.where(state == 0)  # Find empty space (0)
    x, y = x[0], y[0]
    moves = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}
    
    for move, (dx, dy) in moves.items():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = state.copy()
            new_state[x, y], new_state[new_x, new_y] = new_state[new_x, new_y], new_state[x, y]
            neighbors.append((new_state, move))
    
    return neighbors

def reconstruct_path(node):
    path = []
    states = []
    while node:
        path.append(node.move)
        states.append(node.state)
        node = node.parent
    return path[::-1], states[::-1]

def a_star(initial_state, goal_state):
    goal_state = np.array(goal_state)
    initial_state = np.array(initial_state)
    open_list = []
    heapq.heappush(open_list, PuzzleNode(initial_state, heuristic=manhattan_distance(initial_state, goal_state)))
    closed_set = set()
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if np.array_equal(current_node.state, goal_state):
            return reconstruct_path(current_node)
        
        closed_set.add(tuple(map(tuple, current_node.state)))
        
        for neighbor, move in get_neighbors(current_node.state):
            if tuple(map(tuple, neighbor)) in closed_set:
                continue
            
            new_cost = current_node.cost + 1
            heuristic = manhattan_distance(neighbor, goal_state)
            heapq.heappush(open_list, PuzzleNode(neighbor, current_node, move, new_cost, heuristic))
    
    return None, None  # No solution found

# Example usage
initial = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]  # Example initial state
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state
solution, states = a_star(initial, goal)

if solution:
    for i, (move, state) in enumerate(zip(solution, states)):
        print(f"Step {i+1}: Move {move}")
        print(state, "\n")
else:
    print("No solution found.")
