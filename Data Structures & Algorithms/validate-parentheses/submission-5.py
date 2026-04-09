class Solution:
    def isValid(self, s: str) -> bool:
        result = True
        open_stack = ['(', '[', '{']
        match_dict = {')':'(', ']':'[', '}':'{'}
        input_open = []
        for c in s:
            if c in open_stack:
                input_open.append(c)
            else: # c = ')' or ']' or '}'
                if len(input_open) == 0:
                    result = False
                    break
                if match_dict[c] != input_open.pop():
                    result = False
                    break
        if len(input_open) != 0:
            result = False
        return result
        