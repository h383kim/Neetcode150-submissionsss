class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        los = len(s)
        if los == 0 or los == 1:
            return los
        if los == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2
        
        l, r = 0, 1
        seen = {s[l]: 1}
        longest = 1
        while r < los:
            print(f"{l}, {r}")
            print(seen)
            # if l == r:
            #     r += 1
            #     continue

            if s[r] not in seen:
                seen[s[r]] = 1
                if (r - l + 1) > longest:
                    longest = r - l + 1
                r += 1
                continue
            # Check duplicates
            if seen[s[r]] > 0:
                seen[s[l]] -= 1 # Remove left from dict
                l += 1 # move left pointer
                #seen[s[l]] = True
                #seen[s[r]] = True # Add right to dict again in case left=right
                continue
            
            if (r - l + 1) > longest:
                longest = r - l + 1

            # If no duplicate, extend right pointer
            seen[s[r]] += 1 # Add character to seen dict
            r += 1
        
        return longest