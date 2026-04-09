class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            nums_set.add(i)
        if len(nums) == len(nums_set):
            return False
        else:
            return True