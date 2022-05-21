from typing import List


def get_dp(nums: List[int]) -> List[int]:
    dp: List[int] = [0 for _ in range(len(nums))]
    dp[0], dp[len(nums) - 1] = 1, 1

    for i in range(1, len(nums)):
        max_val, max_ind = 0, 0
        for j in range(i):
            if nums[i] > nums[j] and dp[j] > max_val:
                max_val, max_ind = dp[j], j

        if max_val == 0:
            dp[i] = 1
        else:
            dp[i] = dp[max_ind] + 1

    return dp


def solution(nums: List[int]) -> int:
    dp_l: List[int] = get_dp(nums)
    dp_r: List[int] = list(reversed(get_dp(list(reversed(nums)))))

    dp: List[int] = [0 for x in range(len(nums))]
    for i, (l, r) in enumerate(zip(dp_l, dp_r)):
        dp[i] = l + r - 1

    return max(dp)


if __name__ == "__main__":
    N: int = int(input())
    arr: List[int] = list(map(int, input().split()))
    print(solution(arr))
