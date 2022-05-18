import sys
from typing import List


def solution(N: int, costs: List[List[int]]) -> int:
    dp: List[List[int]] = [[0 for y in range(3)] for x in range(N)]

    for ind in range(3):
        dp[0][ind] = costs[0][ind]

    for i in range(1, N):
        for j in range(3):
            min_cost: int = sys.maxsize
            for k in range(3):
                if k == j:
                    continue

                if min_cost > dp[i - 1][k]:
                    min_cost = dp[i - 1][k]

            dp[i][j] = costs[i][j] + min_cost

    return min(dp[-1])


if __name__ == "__main__":
    N: int = int(input())
    costs: List[List[int]] = []

    for _ in range(N):
        costs.append(list(map(int, input().split())))

    print(solution(N, costs))
