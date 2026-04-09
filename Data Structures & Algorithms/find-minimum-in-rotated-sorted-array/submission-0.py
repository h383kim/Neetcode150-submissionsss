class Solution:
    def findMin(self, nums: List[int]) -> int:
        l_idx, r_idx = 0, len(nums) - 1
        l, r = nums[l_idx], nums[r_idx]
        
        while l > r:
            m_idx = l_idx + ((r_idx - l_idx) // 2)
            m = nums[m_idx]
            if (r_idx - l_idx) <= 3:
                result = l
                for i in range(l_idx, r_idx + 1):
                    if nums[i] < l:
                        return nums[i]
            # l < m > r
            if (l < m) and (m > r):
                l_idx = m_idx + 1
                l = nums[l_idx]
            # l > m < r
            elif (l > m) and (m < r):
                l_idx = m_idx - 1
                l = nums[l_idx]
        return l