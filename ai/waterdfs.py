from collections import deque

def water_jug_dfs(start, goal, capacity):
    visited = set()
    stack=deque([(start,[])])
    result = []

    while stack:
        current_state, current_path = stack.pop()  # Pop from the end (DFS)

        if current_state == goal:
            result.append(current_path + [current_state])

        visited.add(current_state)

        # Actions in a specific order for DFS exploration
        # Pour jug 2 to jug 1
        # Fill jug 1
        fill_jug1 = (capacity[0], current_state[1])
        if fill_jug1 not in visited:
            stack.append((fill_jug1, current_path + [current_state]))

        # Fill jug 2
        fill_jug2 = (current_state[0], capacity[1])
        if fill_jug2 not in visited:
            stack.append((fill_jug2, current_path + [current_state]))

        # Pour jug 1 to jug 2
        pour_jug1_to_jug2 = (
            max(0, current_state[0] - (capacity[1] - current_state[1])),
            min(current_state[1] + current_state[0], capacity[1])
        )
        if pour_jug1_to_jug2 not in visited:
            stack.append((pour_jug1_to_jug2, current_path + [current_state]))

        pour_jug2_to_jug1 = (
            min(current_state[0] + current_state[1], capacity[0]),
            max(0, current_state[1] - (capacity[0] - current_state[0]))
        )
        if pour_jug2_to_jug1 not in visited:
            stack.append((pour_jug2_to_jug1, current_path + [current_state]))

        # Empty jug 1
        empty_jug1 = (0, current_state[1])
        if empty_jug1 not in visited:
            stack.append((empty_jug1, current_path + [current_state]))

        # Empty jug 2
        empty_jug2 = (current_state[0], 0)
        if empty_jug2 not in visited:
            stack.append((empty_jug2, current_path + [current_state]))

    return result

# Example usage:
a = int(input("Enter capacity of jug A: "))
b = int(input("Enter capacity of jug B: "))
target = int(input("Enter target amount: "))

start_state = (0, 0)
goal_state = (target, 0)
jug_capacities = (a, b)

solutions = water_jug_dfs(start_state, goal_state, jug_capacities)

if solutions:
    print("All Solution Paths:")
    for path in solutions:
        print(path)
else:
    print("No Solution")
