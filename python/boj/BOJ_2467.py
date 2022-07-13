import sys
from typing import Tuple, List


def solution(nums: List[int]) -> Tuple[int, int]:
    left, right = 0, len(nums) - 1
    min_total, min_left, min_right = sys.maxsize, 0, len(nums) - 1

    while left < right:
        total: int = nums[left] + nums[right]

        if min_total > abs(total):
            min_total, min_left, min_right = abs(total), left, right

        if total == 0:
            return nums[left], nums[right]
        elif total < 0:
            left += 1
        else:
            right -= 1

    return nums[min_left], nums[min_right]


if __name__ == "__main__":
    N: int = int(input())
    nums: List[int] = list((map(int, input().split())))
    left, right = solution(nums)
    print(left, right)
