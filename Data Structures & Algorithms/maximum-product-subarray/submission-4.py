class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(1, 1)] * n
        dp[0] = (nums[0], nums[0])
        for i in range(1, n):
            d = nums[i]
            if d == 0:
                dp[i] = (0, 0)
                continue
            prev = i - 1
            maxVal = max(dp[prev][0]*d, dp[prev][1]*d, d)
            minVal = min(dp[prev][0]*d, dp[prev][1]*d, d)
            dp[i] = (maxVal, minVal)
        
        res = dp[0][0]
        for pair in dp[1:]:
            if pair[0] > res:
                res = pair[0]
        
        return res


