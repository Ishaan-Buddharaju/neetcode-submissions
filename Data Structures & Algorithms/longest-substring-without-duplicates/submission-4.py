class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        slow = 0
        maxLength = 0

        for fast in range(len(s)):
            if s[fast] in hashset:
                while (s[fast] in hashset):
                    hashset.remove(s[slow])
                    slow += 1

            hashset.add(s[fast])
            length = fast - slow + 1
            if length > maxLength:
                maxLength = length
        
        return maxLength
