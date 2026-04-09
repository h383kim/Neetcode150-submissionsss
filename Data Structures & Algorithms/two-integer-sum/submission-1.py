class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {nums[0]: 0}
        for i, num in enumerate(nums[1:]):
            diff = target - num
            if diff in idx.keys() and i + 1 != idx[diff]:
                return [idx[diff], i + 1]
            idx[num] = i + 1

        