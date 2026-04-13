class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carryOver = False
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            
            # Loop continues
            digits[i] = 0
            
            # We have carryOver to the new most significant digit
            if i == 0 and digits[i] == 0:
                carryOver = True
        
        if carryOver:
            return [1] + digits
        else:
            return digits
