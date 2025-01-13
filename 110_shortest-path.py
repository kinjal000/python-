from collections import deque

def shortest_path_in_grid(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (1, 0)]  # Move right or down
    queue = deque([(0, 0, 0,0)])  # (row, col, distance)

    while queue:
        x, y, dist = queue.popleft()

        if x == rows - 1 and y == cols - 1:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                grid[nx][ny] = 1  # Mark as visited
                queue.append((nx, ny, dist + 1))

    return -1  # No path found

grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print("Shortest path length:", shortest_path_in_grid(grid))




























# Explanation: BFS explores the grid level by level. The algorithm tracks the distance
# from the start (top-left) to the end (bottom-right). If a path exists, 
# it returns the shortest distance; otherwise, it returns -1.