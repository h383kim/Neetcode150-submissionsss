class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     regex = re.compile('[^a-zA-Z]')
    #     clean_str = re.sub(regex, '', s)
    #     clean_str = clean_str.lower()
    #     print(clean_str)

    #     los = len(clean_str)
    #     stack = []
    #     # First half
    #     for i in range(los // 2):
    #         stack.append(clean_str[i])
    #     half = los // 2
    #     if los % 2 == 0:
    #         idx = los // 2
    #     else:
    #         idx = los // 2 + 1
    #     for i in range(half):
    #         if clean_str[idx + i] == stack.pop():
    #             pass
    #         else:
    #             return False
        
    #     return True
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for i in s:
            if i.isalnum():
                clean.append(i.lower())
        
        l, r = 0, len(clean) - 1
        while l < r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1
        return True