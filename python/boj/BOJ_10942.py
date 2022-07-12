import sys
from typing import List, Optional


def solution(nums: List[int], pairs: List[List[int]]) -> List[int]:
    n: int = len(nums)
    dp: List[List[Optional[int]]] = [[None for _ in range(n)] for _ in range(n)]

    def recursion(i: int, j: int) -> int:
        if dp[i][j] is not None:
            return dp[i][j]

        if nums[i] != nums[j]:
            dp[i][j] = 0
        elif j - i > 1:
            dp[i][j] = recursion(i + 1, j - 1)
        else:
            dp[i][j] = 1

        return dp[i][j]

    result: List[int] = []
    for left, right in pairs:
        result.append(recursion(left - 1, right - 1))

    return result


if __name__ == "__main__":
    N: int = int(input())
    nums: List[int] = list(map(int, sys.stdin.readline().split()))

    M: int = int(input())
    pairs: List[List[int]] = []
    for _ in range(M):
        pairs.append(list(map(int, sys.stdin.readline().split())))

    result: List[int] = solution(nums, pairs)
    for num in result:
        sys.stdout.write(str(num) + "\n")
