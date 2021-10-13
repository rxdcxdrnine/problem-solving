from typing import List


def numIslands(grid: List[List[str]]) -> int:

    num_rows = len(grid)
    num_cols = len(grid[0])
    num_islands = 0

    stack = []
    visited = [[False for col in range(num_cols)] for row in range(num_rows)]
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == "1" and not visited[i][j]:
                stack.append([i, j])
                visited[i][j] = True
                num_islands += 1

            while stack:
                current = stack.pop()

                for move in moves:
                    next = [current[0] + move[0], current[1] + move[1]]
                    if 0 <= next[0] < num_rows and 0 <= next[1] < num_cols \
                            and grid[next[0]][next[1]] == "1" and not visited[next[0]][next[1]]:
                        stack.append(next)
                        visited[next[0]][next[1]] = True

    return num_islands


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(numIslands(grid))
