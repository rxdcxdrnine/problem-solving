import collections
from typing import List, Optional, Tuple, Deque


def solution(grid: List[List[int]]):
    n, m = len(grid), len(grid[0])

    dr: List[int] = [-1, 0, 1, 0]  # [north, east, south, west]
    dc: List[int] = [0, 1, 0, -1]

    dists_0: List[List[Optional[int]]] = [[None for y in range(m)] for x in range(n)]  # not smashed
    dists_1: List[List[Optional[int]]] = [[None for y in range(m)] for x in range(n)]  # smashed

    queue: Deque[Tuple[int, int, int, int]] = collections.deque([(1, 0, 0, 0)])
    while queue:
        dist, smash, r, c = queue.popleft()

        if smash:
            if dists_1[r][c] is not None \
                    and dist >= dists_1[r][c]:
                continue
            dists_1[r][c] = dist
        else:
            if dists_0[r][c] is not None \
                    and dist >= dists_0[r][c]:
                continue
            dists_0[r][c] = dist

        if r == n - 1 and c == m - 1:
            break

        for i in range(4):
            nr: int = r + dr[i]
            nc: int = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == 0:
                    queue.append((dist + 1, smash, nr, nc))
                if grid[nr][nc] == 1 and smash == 0:
                    queue.append((dist + 1, 1, nr, nc))

    cond_0: bool = dists_0[n - 1][m - 1] is None
    cond_1: bool = dists_1[n - 1][m - 1] is None

    if cond_0 and cond_1:
        return -1
    elif not cond_0 and cond_1:
        return dists_0[n - 1][m - 1]
    elif cond_0 and not cond_1:
        return dists_1[n - 1][m - 1]
    else:
        return min(dists_0[n - 1][m - 1], dists_1[n - 1][m - 1])


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr: List[List[int]] = []

    for _ in range(N):
        arr.append(list(map(int, list(input()))))

    print(solution(arr))
