from typing import List, Tuple


def solution(n: int) -> Tuple[int, List[int]]:
    dp: List[List[int]] = [[0, None] for _ in range(1000001)]

    for i in range(2, 1000001):
        tmp: List[List[int]] = [[dp[i - 1][0] + 1, i - 1]]
        if i % 3 == 0:
            tmp.append([dp[i // 3][0] + 1, i // 3])
        if i % 2 == 0:
            tmp.append([dp[i // 2][0] + 1, i // 2])

        dp[i] = min(tmp, key=lambda x: x[0])

    numbers: List[int] = [n]
    count, p = dp[n]

    while p:
        numbers.append(p)
        p = dp[p][1]

    return count, numbers


if __name__ == "__main__":
    N: int = int(input())
    COUNT, NUMBERS = solution(N)

    print(COUNT)
    print(' '.join(map(str, NUMBERS)))
