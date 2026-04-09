class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
    # def search(self, nums: List[int], target: int) -> int:
    #     index = 0

    #     while len(nums) > 0:
    #         loa = len(nums)
    #         if loa == 1:
    #             if nums[0] == target:
    #                 return index
    #             else:
    #                 return -1
            
    #         mid = loa // 2
    #         mid_num = nums[mid]
    #         if mid_num == target:
    #             return index + mid
    #         elif mid_num > target:
    #             nums = nums[:mid]
    #         else:
    #             index += mid
    #             nums = nums[mid:]
