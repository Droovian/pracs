def waterJug_dfs(x, y, target, path=[], visited=set()):
    if (x, y) == target :
        return [path + [(x, y)]]

    if (x, y) in visited:
        return []

    visited.add((x, y))
    path = path + [(x, y)]
    paths = []

    if x < a:
        fill_x = waterJug_dfs(a, y, target, path, visited)
        paths.extend(fill_x)

    if y < b:
        fill_y = waterJug_dfs(x, b, target, path, visited)
        paths.extend(fill_y)

    if x > 0:
        pour_x_to_y = waterJug_dfs(max(0, (x - (b - y))), min(b, x + y), target, path, visited)
        paths.extend(pour_x_to_y)

    if y > 0:
        pour_y_to_x = waterJug_dfs(min(a, x + y), max(0, y - (a - x)), target, path, visited)
        paths.extend(pour_y_to_x)

    if x > 0:
        empty_x = waterJug_dfs(0, y, target, path, visited)
        paths.extend(empty_x)

    if y > 0:
        empty_y = waterJug_dfs(x, 0, target, path, visited)
        paths.extend(empty_y)

    return paths


a = int(input("Enter the capacity of jug A: "))
b = int(input("Enter the capacity of jug B: "))
target = int(input("Enter the target amount: "))

paths = waterJug_dfs(0, 0, (0, target))
if paths:
    print("All Solution Paths:")
    for path in paths:
        print(path)
else:
    print("No Solution")
