class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Contains permutation if there is a window of len s1 with set(s1 characters)
        if len(s2) < len(s1):
            return False

        L = 0
        R = L + len(s1) - 1
        s1Freq = {}
        for char in s1: 
            if char in s1Freq: 
                s1Freq[char] += 1
            else:
                s1Freq[char] = 1

        s2Freq = {}
        for i in range(len(s1) - 1):
            if s2[i] in s2Freq:
                s2Freq[s2[i]] += 1
            else: 
                s2Freq[s2[i]] = 1
        
        while R < len(s2):
            if s2[R] in s2Freq: 
                s2Freq[s2[R]] += 1
            else: 
                s2Freq[s2[R]] = 1

            if s1Freq == s2Freq: 
                return True
            
            s2Freq[s2[L]] -= 1
            if s2Freq[s2[L]] == 0:
                del s2Freq[s2[L]]
            L += 1
            R += 1
            
        if s2Freq == s1Freq:
            return True

        return False