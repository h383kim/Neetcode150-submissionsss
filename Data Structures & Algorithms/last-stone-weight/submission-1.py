import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)
            max1, max2 = -max1, -max2

            if max1 < max2:
                new = -(max2 - max1)
                heapq.heappush(stones, new)
            elif max1 > max2:
                new = -(max1 - max2)
                heapq.heappush(stones, new)
        
        if len(stones) == 0:
            return 0
        return -stones[0]
