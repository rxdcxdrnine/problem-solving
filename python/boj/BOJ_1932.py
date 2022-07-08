from typing import List


def solution(nums: List[List[int]]) -> int:
    dp: List[List[int]] = [[0] * len(nums)] * len(nums)

    for r in reversed(range(len(nums))):
        for c in range(r + 1):
            if r == len(nums) - 1:
                dp[r][c] = nums[r][c]
            else:
                dp[r][c] = nums[r][c] + max(dp[r + 1][c], dp[r + 1][c + 1])

    return dp[0][0]


if __name__ == "__main__":
    n: int = int(input())
    nums: List[List[int]] = []

    for _ in range(n):
        nums.append(list(map(int, input().split())))
    print(solution(nums))
