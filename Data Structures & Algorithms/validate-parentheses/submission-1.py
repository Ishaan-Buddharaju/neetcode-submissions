class Solution:
    def isValid(self, s: str) -> bool:
        # maintain stack of curr characters
        # as we encounter make sure we pop corresponding open off the stack
        stack = []
        paren = {')': '(', '}': '{', ']':'['}

        for char in s: 
            if char in paren: # found the end paren
                if stack and stack[-1] == paren[char]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(char)
        return not stack # if not empty by end we had extras, return false
            