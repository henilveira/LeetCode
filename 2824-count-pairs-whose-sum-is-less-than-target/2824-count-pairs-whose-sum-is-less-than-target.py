class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        pairs = 0
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum < target:
                pairs += right-left
                left += 1
            else:
                right -= 1
        return pairs
            