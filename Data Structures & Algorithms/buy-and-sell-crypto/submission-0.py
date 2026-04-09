class Solution:
    def findmax(self, lst: List[int]) -> int:
        max = 0
        for i in lst:
            if i > max:
                max = i
        return max
    
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        for idx, buy in enumerate(prices):
            sell = self.findmax(prices[idx:])
            prof = sell - buy
            if prof > maxprof:
                maxprof = prof    
        
        return maxprof