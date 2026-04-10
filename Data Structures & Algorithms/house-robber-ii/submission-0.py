class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        if N == 2:
            return max(nums[0], nums[1])

        n = len(nums) - 1
        dp_with_left = [0] * n
        dp_with_right = [0] * n

        dp_with_left[0] = nums[0]
        dp_with_right[0] = nums[1]
        dp_with_left[1] = max(nums[0], nums[1])
        dp_with_right[1] = max(nums[1], nums[2])

        for i in range(2, n):
            dp_with_left[i] = max(
                dp_with_left[i - 2] + nums[i],
                dp_with_left[i - 1]
            )
            dp_with_right[i] = max(
                dp_with_right[i - 2] + nums[i + 1],
                dp_with_right[i - 1]
            )
        
        return max(dp_with_left[n - 1], dp_with_right[n - 1])