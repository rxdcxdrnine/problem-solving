from typing import List


def solution(N: int, K: int, items: List[List[int]]) -> int:
    dp: List[List[int]] = [[0 for y in range(K + 1)] for x in range(N + 1)]

    for i in range(N):
        for j in range(1, K + 1):
            w, v = items[i]

            if w <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[N - 1][K]


if __name__ == "__main__":
    N, K = map(int, input().split())
    items: List[List[int]] = []

    for _ in range(N):
        items.append(list(map(int, input().split())))

    print(solution(N, K, items))
