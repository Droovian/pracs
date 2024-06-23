def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])

def heuristic(ini, goa): # add sum as values in ini not matching with goal as heuristic
    sum=0
    for i in goa:
        if(goa[i] != ini[i]):
            sum +=1
    return sum

def move(state, direction):
    blank_index = state.index(0) # 0  indicates empty position to shift
    copy_state = list(state)

    if direction == 'up' and blank_index > 2:
        copy_state[blank_index], copy_state[blank_index - 3] = copy_state[blank_index - 3], copy_state[blank_index]
    elif direction == 'down' and blank_index < 6:
        copy_state[blank_index], copy_state[blank_index + 3] = copy_state[blank_index + 3], copy_state[blank_index]
    elif direction == 'left' and blank_index % 3 != 0:
        copy_state[blank_index], copy_state[blank_index - 1] = copy_state[blank_index - 1], copy_state[blank_index]
    elif direction == 'right' and blank_index % 3 != 2:
        copy_state[blank_index], copy_state[blank_index + 1] = copy_state[blank_index + 1], copy_state[blank_index]
    else:
        return None

    return tuple(copy_state)

def generate_neighbours(some_state):

    neighbours = []
    directions = ['up', 'down', 'left', 'right' ]
    for direction in directions:
        neighbour = move(some_state, direction)
        if neighbour is not None:
            neighbours.append(neighbour)
    return neighbours

def solve_puzzle(initial_state, goal_state, max_count=1000):
    current_state = initial_state
    current_cost = heuristic(initial_state, goal_state)

    counter = 0
    path = [current_state]
    print("Current heuristic:", current_cost)

    while current_cost > 0 and counter < max_count:
        neighbours = generate_neighbours(current_state)
        best_neighbour = min(neighbours, key = lambda x:heuristic(x, goal_state)) # minimum heuristic neighbour to goal
        best_neighbour_cost = heuristic(best_neighbour, goal_state)

        if best_neighbour_cost < current_cost:
            current_state = best_neighbour
            current_cost = best_neighbour_cost

            print_state(current_state)
            print(current_cost)
            path.append(current_state)
        else:
            print("No solution found")
            break
        counter+=1

initial_state = tuple(map(int, input("Enter initial state : ").split()))
goal_state=(1,2,3,4,5,6,7,8,0)

solve_puzzle(initial_state, goal_state)
