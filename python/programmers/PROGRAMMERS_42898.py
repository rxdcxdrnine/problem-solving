from typing import List


def solution(m: int, n: int, puddles: List[List[int]]):

    dp: List[List[int]] = [[0 for row in range(n)] for col in range(m)]
    loc: List[List[bool]] = [[False for row in range(n)] for col in range(m)]

    dp[0][0] = 1

    if len(puddles) > 0:
        for row, col in puddles:
            loc[row - 1][col - 1] = True

    for row in range(m):
        for col in range(n):
            if loc[row][col]:
                continue

            if row > 0:
                dp[row][col] += dp[row - 1][col]
            if col > 0:
                dp[row][col] += dp[row][col - 1]

    return dp[m - 1][n - 1] % 1_000_000_007


if __name__ == "__main__":
    print(solution(4, 3, [[2, 2]]))
