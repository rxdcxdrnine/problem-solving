from typing import List, Tuple


def numIslands(grid: List[List[str]]) -> int:
    plane: List[List[int]] = get_plane(grid)

    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]

    stack: List[Tuple[int, int]] = []
    visited: List[List[bool]] = [[False for _ in range(len(grid[0]))]
                                 for _ in range(len(grid))]

    comps: int = 0

    for row in range(len(plane)):
        for col in range(len(plane[0])):

            if not plane[row][col] or visited[row][col]:
                continue

            comps += 1
            stack.append((row, col))
            visited[row][col] = True

            while stack:
                x, y = stack.pop()

                for i in range(len(dxs)):
                    dx: int = dxs[i]
                    dy: int = dys[i]
                    if 0 <= x + dx < len(plane) and 0 <= y + dy < len(plane[0]) \
                            and plane[x + dx][y + dy] and not visited[x + dx][y + dy]:
                        stack.append((x + dx, y + dy))

                        visited[x + dx][y + dy] = True

    return comps


def get_plane(grid: List[List[str]]) -> List[List[int]]:
    plane: List[List[bool]] = []

    for row in range(len(grid)):
        line: List[bool] = []

        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                line.append(True)
            else:
                line.append(False)

        plane.append(line)

    return plane


if __name__ == "__main__":
    grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
    ]
    print(numIslands(grid))
