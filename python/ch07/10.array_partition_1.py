from typing import List


def arrayPairSum(nums: List[int]) -> int:
    return sum([num for i, num in enumerate(sorted(nums)) if i % 2 == 0])


if __name__ == "__main__":
    nums = [6, 2, 6, 5, 1, 2]
    print(arrayPairSum(nums))