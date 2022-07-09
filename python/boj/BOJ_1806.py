import sys
from typing import List


def solution(nums: List[int]) -> int:
    left, right = 0, 0

    total: int = nums[0]
    min_len: int = sys.maxsize

    if total >= S:
        return 1

    while left <= right < len(nums):
        if total >= S:
            total -= nums[left]
            left += 1
        elif right < len(nums) - 1:
            right += 1
            total += nums[right]
        else:
            break

        if total >= S:
            min_len = min(min_len, right - left + 1)

    if min_len == sys.maxsize:
        return 0
    else:
        return min_len


if __name__ == "__main__":
    N, S = map(int, input().split())
    nums: List[int] = list(map(int, input().split()))

    print(solution(nums))
