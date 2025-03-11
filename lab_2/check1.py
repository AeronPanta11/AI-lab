from itertools import product
import copy

# Get the index of an element in the matrix
def getindex(matrix, element):
    for i, j in product(range(3), range(3)):
        if matrix[i][j] == element:
            return i, j

# Input the puzzle matrix
def inputbox():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            element = int(input(f"Please enter the [{i}][{j}] element: "))
            row.append(element)
        matrix.append(row)
    return matrix

# Get legal moves for the empty tile (0)
def legalMoves(matrix):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 0:
                x, y = i, j
                index = (x, y)
                break
    possible_moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    allowed_moves = [(a, b) for a, b in possible_moves if 0 <= a < 3 and 0 <= b < 3]
    return allowed_moves, index

# Calculate the next possible states
def nextState(next_moves, currentState, emptyIndex):
    possibleMatrix = []
    for move in next_moves:
        temp = copy.deepcopy(currentState)
        temp[emptyIndex[0]][emptyIndex[1]] = temp[move[0]][move[1]]
        temp[move[0]][move[1]] = 0
        possibleMatrix.append(temp)
    return possibleMatrix

# Determine the best move using A* heuristic
def bestMoves(gn, next_moves, goal_state, visited_states):
    hn = float('inf')
    best_state = None

    for move in next_moves:
        h = 0  # Manhattan distance heuristic
        for i, j in product(range(3), range(3)):
            element = move[i][j]
            if element != 0:
                igoal, jgoal = getindex(goal_state, element)
                h += abs(igoal - i) + abs(jgoal - j)

        fn = gn + h
        if fn < hn and tuple(map(tuple, move)) not in visited_states:
            best_state = move
            hn = fn

    if best_state is None:
        print("No valid moves found! Exiting...")
        exit(1)

    gn += 1
    return gn, best_state

# A* algorithm implementation
def Astar(start, goal):
    visited_states = set()  # Use a set for efficient state storage
    gn = 0
    currentState = start

    while currentState != goal:
        visited_states.add(tuple(map(tuple, currentState)))
        print("Current State:")
        for row in currentState:
            print(row)
        print("***********")

        next_moves, emptyIndex = legalMoves(currentState)
        possibleNextStates = nextState(next_moves, currentState, emptyIndex)
        gn, currentState = bestMoves(gn, possibleNextStates, goal, visited_states)

    print("Goal found!")
    print("Final State:")
    for row in currentState:
        print(row)
    print("Cost:", gn)

# Main function
if __name__ == "__main__":
    print("Please enter the start state:")
    start = inputbox()
    print("Please enter the goal state:")
    goal = inputbox()
    Astar(start, goal)
