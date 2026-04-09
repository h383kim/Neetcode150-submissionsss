class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            next_max = max(dp[i - 1], dp[i - 2] + nums[i])
            dp[i] = next_max
        
        return dp[n - 1]