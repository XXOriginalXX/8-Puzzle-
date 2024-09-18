import heapq

def calculate_heuristic(state, goal):
    distance = 0
    goal_positions = {}
    for i in range(3):
        for j in range(3):
            goal_positions[goal[i][j]] = (i, j)
    
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x, target_y = goal_positions[value]
                distance += abs(i - target_x) + abs(j - target_y)
    
    return distance

def is_goal_state(state, goal):
    return state == goal


def generate_moves(state):
    x, y = 0, 0  
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break
    
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for direction in directions:
        new_x, new_y = x + direction[0], y + direction[1]
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]

            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            moves.append(new_state)
    
    return moves

def a_star(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (calculate_heuristic(start, goal), start, []))
    visited = set()

    while priority_queue:
        _, current_state, path = heapq.heappop(priority_queue)
        visited.add(tuple(tuple(row) for row in current_state))

        if is_goal_state(current_state, goal):
            return path + [current_state]

        for move in generate_moves(current_state):
            if tuple(tuple(row) for row in move) not in visited:
                heapq.heappush(priority_queue, (len(path) + 1 + calculate_heuristic(move, goal), move, path + [current_state]))
    
    return None


start = []
for i in range(3):
    start.append(list(map(int, input(f"Enter row {i+1} of the start state (space-separated): ").split())))

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = a_star(start, goal)

if solution:
    print("Solution found!")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution exists.")
