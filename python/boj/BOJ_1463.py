# N: int = int(input())
# dp = [0 for _ in range(N + 1)]
# dp[1] = 0
#
#
# def solution(n: int) -> int:
#
#     if n == 1 or dp[n]:
#         return dp[n]
#
#     if n % 3 == 0:
#         dp[n] = solution(n // 3) + 1
#         return dp[n]
#
#     if n % 2 == 0:
#         dp[n] = min(solution(n // 2), solution(n - 1)) + 1
#         return dp[n]
#
#     dp[n] = solution(n - 1) + 1
#     return dp[n]
#
#
# print(solution(N))

import sys
from typing import List


def solution(n: int) -> int:
    dp: List[int] = [sys.maxsize for _ in range(N + 1)]
    dp[1] = 0

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1

        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1

    return dp[n]


if __name__ == "__main__":
    N: int = int(input())
    print(solution(N))
