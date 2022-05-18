import copy
import itertools
from collections import deque
from typing import List, Tuple, Deque


def solution(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dr = [-1, 0, 1, 0]  # [north, west, south, east]
    dc = [0, -1, 0, 1]

    zeros: List[Tuple[int, int]] = []
    twos: List[Tuple[int, int]] = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                zeros.append((i, j))
            if grid[i][j] == 2:
                twos.append((i, j))

    max_count: int = 0
    for p1, p2, p3 in itertools.combinations(zeros, 3):
        arr: List[List[int]] = copy.deepcopy(grid)
        arr[p1[0]][p1[1]] = 1
        arr[p2[0]][p2[1]] = 1
        arr[p3[0]][p3[1]] = 1

        queue: Deque[Tuple[int, int]] = deque()
        for point in twos:
            queue.append(point)

        while queue:
            r, c = queue.popleft()

            for i in range(4):
                nr: int = r + dr[i]
                nc: int = c + dc[i]

                if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                    arr[nr][nc] = 2
                    queue.append((nr, nc))

        count: int = 0
        for r in range(n):
            for c in range(m):
                if arr[r][c] == 0:
                    count += 1

        max_count = max(max_count, count)

    return max_count


if __name__ == "__main__":
    N, M = map(int, input().split())
    grid: List[List[int]] = []

    for _ in range(N):
        grid.append(list(map(int, input().split())))

    print(solution(grid))
