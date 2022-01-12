from typing import List


# time limit exceeded
def trap_0(height: List[int]) -> int:
    result = 0

    for ind in range(len(height)):
        left, right = ind, ind
        left_max, right_max = height[ind], height[ind]

        while left >= 0:
            left_max = max(left_max, height[left])
            left -= 1
        while right < len(height):
            right_max = max(right_max, height[right])
            right += 1

        result += min(left_max, right_max) - height[ind]

    return result


def trap_1(height: List[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap_1(height))
