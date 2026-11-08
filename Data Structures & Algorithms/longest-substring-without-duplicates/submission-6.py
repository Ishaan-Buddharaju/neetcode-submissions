class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if (n < 2):
            return n
        currLen = 1
        maxLen = 1
        L = 0
        R = 1
        substr = set(s[L]) # b, w 
        while (R < n):
            if not s[R] in substr:
                substr.add(s[R])
                currLen += 1 # 2
                maxLen = currLen if currLen > maxLen else maxLen
                R += 1
                continue
            
            while (s[R] != s[L]): 
                substr.remove(s[L])
                L += 1
                currLen -= 1
            L += 1
            R += 1
        
        return maxLen
            

            