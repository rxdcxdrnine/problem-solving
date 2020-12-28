# leetcode 15

# time limit exceeded
def threeSum_0(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = 0 - nums[i]
        sub_nums = nums[i + 1:]
        left, right = 0, len(sub_nums) - 1

        while sub_nums and left != right:
            if sub_nums[left] + sub_nums[right] < target:
                left += 1
            elif sub_nums[left] + sub_nums[right] > target:
                right -= 1
            else:
                triplet = sorted([nums[i], sub_nums[left], sub_nums[right]])
                if triplet not in result:
                    result.append(triplet)

                sub_nums.pop(right)
                sub_nums.pop(left)
                left, right = 0, len(sub_nums) - 1

    return result


def threeSum_A(nums):
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # jump if duplicated value
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                results.append(nums[i], nums[left], nums[right])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results


if __name__ == "__main__":
    print(threeSum_0([-1,0,1,2,-1,-4]))
