from collections import deque

m = int(input("No of missionaries: "))
c = int(input("No of cannibals: "))

final_paths = []

def is_valid(state):
    m1,c1, n = state

    m2 = m-m1
    c2 = c-c1

    if m1 < 0 or m2 < 0 or c1 < 0 or c2<0:
        return 0
    if (m1 and m1 < c1) or (m2 and m2 < c2):
        return 0

    return 1

def generate_successors(state):
    m, c, n = state
    successors = []

    actions=[(1,0), (2,0), (0,1), (0,2), (1,1)]

    for action in actions:
        moved_ms, moved_cn = action

        if n==1:
            new_state = (m-moved_ms, c-moved_cn, 0)
        else:
            new_state = (m+moved_ms, c+moved_cn, 1)

        if is_valid(new_state):
            successors.append(new_state)

    return successors


def bfs():
    start_state=(m, c, 1)
    goal_state= (0,0,0)

    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state = queue.popleft()
        state, path = current_state

        if state in visited:
            continue

        path.append(state)

        if state == goal_state:
            final_paths.append(path)
            continue

        visited.add(state)
        for successor in generate_successors(state):
            if successor not in visited:
                queue.append((successor, path))

bfs()

if len(final_paths) != 0:
    for p in final_paths:
        print(p)
