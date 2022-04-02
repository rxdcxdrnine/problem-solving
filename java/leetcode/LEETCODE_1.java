package leetcode;


import java.util.stream.IntStream;

class LEETCODE_1 {
    public int[] twoSum(int[] nums, int target) {
        int[] inds = IntStream.range(0, nums.length)
            .boxed()
            .sorted((a, b) -> Integer.compare(nums[a], nums[b]))
            .mapToInt(Integer::intValue)
            .toArray();
        
        int left = 0, right = nums.length - 1;
        int agg = nums[inds[left]] + nums[inds[right]];
        
        while (agg != target) {
            if (agg > target) {
                right -= 1;
            }
            if (agg < target) {
                left += 1;
            }
            
            agg = nums[inds[left]] + nums[inds[right]];
        }
        
        return new int[] { inds[left], inds[right] };
    }
}
