class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        for num in nums1:
            if num in nums2 and num not in nums:
                nums.append(num)
        return nums