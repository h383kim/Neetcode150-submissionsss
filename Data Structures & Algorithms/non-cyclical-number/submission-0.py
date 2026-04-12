class Solution:
    def isHappy(self, n: int) -> bool:
        n1 = n
        n2 = n
        while True:
            n1 = self.sumSquares(n1)
            n2 = self.sumSquares(self.sumSquares(n2))
            if n1 == 1:
                return True
            if n1 == n2:
                return False
    
    def sumSquares(self, n: int) -> int:
        num = str(n)
        sum = 0
        for i in range(len(num)):
            sum += int(num[i])**2
        return sum