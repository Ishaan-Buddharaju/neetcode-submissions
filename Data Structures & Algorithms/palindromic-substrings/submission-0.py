class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromeCount = 0
        for i in range(len(s)):
            palindromeCount += 1
            l = i
            r = i + 1

            while (r < len(s) and l >= 0):
                if s[l] == s[r]:
                    palindromeCount += 1
                    l -= 1
                    r += 1
                else: 
                    break
            l = i - 1
            r = i + 1
            while (r < len(s) and l >= 0):
                if s[l] == s[r]:
                    palindromeCount += 1
                    l -= 1
                    r += 1
                else:
                    break

        return palindromeCount
                    
