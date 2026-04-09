from itertools import combinations

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        candidates = []
        for num in nums:
            numMax = target // num
            candidates.extend([num] * numMax)

        maxLen = target // min(nums)
        allCombinations = []
        for n in range(1, maxLen + 1):
            nCombinations = list(combinations(candidates, n))
            for comb in nCombinations:
                if sum(comb) == target:
                    allCombinations.append(sorted(comb))

        result = set()
        for comb in allCombinations:
            result.add(tuple(comb))
        
        return [list(item) for item in result]
            