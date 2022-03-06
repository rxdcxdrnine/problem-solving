from typing import List

# Leetcode #1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inds: List[int] = sorted([ind for ind in range(len(nums))], key=lambda x: nums[x])
        
        left, right = 0, len(nums) - 1
        agg: int = nums[inds[left]] + nums[inds[right]]
    
        while agg != target:
            agg: int = nums[inds[left]] + nums[inds[right]]
            
            if agg > target:
                right -= 1
            if agg < target:
                left += 1
                
        return inds[left], inds[right]


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
