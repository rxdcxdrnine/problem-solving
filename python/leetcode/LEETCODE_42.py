from typing import List


# Leetcode #42
class Solution:
    def trap_0(self, height: List[int]) -> int:
        lefts: List[int] = [0] * len(height)
        rights: List[int] = [0] * len(height)
        cumsum: int = 0

        left_max: int = 0
        right_max: int = 0

        for ind in range(len(height)):
            if left_max < height[ind]:
                left_max = height[ind]
            lefts[ind] = left_max

        for ind in reversed(range(len(height))):
            if right_max < height[ind]:
                right_max = height[ind]
            rights[ind] = right_max

        for ind in range(len(height)):
            cumsum += min(lefts[ind], rights[ind]) - height[ind]

        return cumsum

    def trap_1(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume
