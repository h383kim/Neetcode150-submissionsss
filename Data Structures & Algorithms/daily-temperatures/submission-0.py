from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIdx, stackTemp = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append([idx, temp])
        
        return res
            
