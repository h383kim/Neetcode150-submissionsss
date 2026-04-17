class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (1 + n) * n / 2
        Sum = 0
        for num in nums:
            Sum += num
        return int(total - Sum)