# leetcode 1

def twoSum_0(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum_A(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


def twoSum_B(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_map and i != nums_map[complement]:
            return [i, nums_map[complement]]


def twoSum_C(nums, target):
    left, right = 0, len(nums) - 1
    while left != right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


# if nums not sorted
def twoSum_C2(nums, target):
    nums = [(num, ind) for ind, num in enumerate(nums)]
    nums.sort(key=lambda x: x[0])

    left, right = 0, len(nums) - 1
    while left != right:
        if nums[left][0] + nums[right][0] < target:
            left += 1
        elif nums[left][0] + nums[right][0] > target:
            right -= 1
        else:
            return [nums[left][1], nums[right][1]]


if __name__ == "__main__":
    print(twoSum_C2([2, 15, 7, 11], 9))