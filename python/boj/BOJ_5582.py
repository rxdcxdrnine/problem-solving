from typing import List


def solution(x: str, y: str) -> int:

    counts: List[List[int]] = [[0 for _ in range(len(y) + 1)]
                               for _ in range(len(x) + 1)]

    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            if i == 0 or j == 0:
                counts[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                counts[i][j] += counts[i - 1][j - 1] + 1
            else:
                counts[i][j] = 0

    max_len: int = 0
    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            max_len = max(max_len, counts[i][j])

    return max_len


if __name__ == "__main__":
    first: str = input()
    second: str = input()
    print(solution(first, second))
