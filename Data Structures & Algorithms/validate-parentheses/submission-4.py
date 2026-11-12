class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s: 
            if char not in lookup: 
                stack.append(char)
            elif len(stack) != 0 and stack[-1] == lookup[char]:
                stack.pop()
            else: 
                return False
        
        return True if len(stack) == 0 else False

                
            