import itertools
import sys
from typing import List, Tuple


def solution(m: int, arr: List[List[int]]) -> int:
    houses: List[Tuple[int, int]] = []
    chicks: List[Tuple[int, int]] = []
    row, col = len(arr), len(arr[0])

    for r in range(row):
        for c in range(col):
            if arr[r][c] == 1:
                houses.append((r, c))
            if arr[r][c] == 2:
                chicks.append((r, c))

    dist: int = sys.maxsize
    for comb in itertools.combinations(chicks, m):
        dist = min(dist, sum_distance(houses, comb))

    return dist


def sum_distance(houses: List[Tuple[int, int]],
                 chicks: List[Tuple[int, int]]) -> int:
    total: int = 0
    for house in houses:
        dist: int = sys.maxsize

        for chick in chicks:
            dist = min(dist, get_distance(house, chick))
        total += dist

    return total


def get_distance(house: Tuple[int, int],
                 chick: Tuple[int, int]) -> int:
    (r1, c1), (r2, c2) = house, chick
    return abs(r1 - r2) + abs(c1 - c2)


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr: List[List[int]] = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    print(solution(M, arr))
