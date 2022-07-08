import collections
from typing import List, Tuple, Deque


def solution(M: int, N: int, plane: List[List[int]]):
    queue: Deque[Tuple[int, int, int]] = collections.deque()

    for row in range(N):
        for col in range(M):
            if plane[row][col] == 1:
                queue.append((row, col, 0))

    dr: List[int] = [1, -1, 0, 0]
    dc: List[int] = [0, 0, 1, -1]

    last_day: int = 0
    while queue:
        row, col, day = queue.popleft()
        for ind in range(4):
            r: int = row + dr[ind]
            c: int = col + dc[ind]
            if 0 <= r < N and 0 <= c < M and plane[r][c] == 0:
                plane[r][c] = 1
                queue.append((r, c, day + 1))

        last_day = day

    for row in range(N):
        for col in range(M):
            if plane[row][col] == 0:
                return -1

    return last_day


if __name__ == "__main__":
    M, N = map(int, input().split())
    plane: List[List[int]] = []

    for _ in range(N):
        plane.append(list(map(int, input().split())))

    print(solution(M, N, plane))
