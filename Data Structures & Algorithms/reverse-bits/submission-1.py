class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = ""
        for i in range(32):
            if n & (1 << i) != 0:
                reverse += "1"
            else:
                reverse += "0"
        
        res = 0
        for i, c in enumerate(reverse[::-1]):
            if c == "1":
                res += (1 << i)

        return res
