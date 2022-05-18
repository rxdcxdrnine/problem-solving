from typing import List


def solution(nums: List[int]) -> int:
    dp: List[int] = [0 for _ in nums]
    dp[0] = 1

    for i in range(len(nums)):
        max_len = 0

        for j in range(i):
            if nums[i] > nums[j] and dp[j] > max_len:
                max_len = dp[j]

        dp[i] = max_len + 1

    return max(dp)


if __name__ == "__main__":
    N: int = int(input())
    nums: List[int] = list(map(int, input().split()))
    print(solution(nums))
