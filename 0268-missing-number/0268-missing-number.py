class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tamanho = len(nums)
        correct_sum = (tamanho*(tamanho + 1))/2
        all_sum = sum(nums)
        res = correct_sum - all_sum
        return int(res)