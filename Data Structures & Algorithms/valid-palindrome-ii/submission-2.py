class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        Ideas: 
        - Start two ptrs at beginning and end
        - When conflict, remove both seperately and try both permutations
        '''
        def isPalindrome(s: str) -> bool:
            left = 0
            right = len(s) - 1
            print(s)
            while left < right: 
                if s[left] != s[right]: 
                    return False
                left += 1
                right -= 1
            
            return True

        left = 0
        right = len(s) - 1
        
        while left < right: 
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            
            return isPalindrome(s[left:right]) or isPalindrome(s[left + 1: right + 1])

        return True

    
