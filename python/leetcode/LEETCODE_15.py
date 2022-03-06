from typing import List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results: List[List[int]] = []
        nums.sort()

        for ind in range(len(nums) - 2):

            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue

            left, right = ind + 1, len(nums) - 1

            while left < right:
                agg: int = nums[ind] + nums[left] + nums[right]

                if agg < 0:
                    left += 1
                elif agg > 0:
                    right -= 1
                else:
                    results.append([nums[ind], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

