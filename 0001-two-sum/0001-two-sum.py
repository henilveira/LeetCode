class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = [(num, idx) for idx, num in enumerate(nums)]
        
        indexed_nums.sort()
        
        left, right = 0, len(nums) - 1

        while left < right:
            soma = indexed_nums[left][0] + indexed_nums[right][0]
            if soma == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif soma < target:
                left += 1
            else:
                right -= 1

        return []