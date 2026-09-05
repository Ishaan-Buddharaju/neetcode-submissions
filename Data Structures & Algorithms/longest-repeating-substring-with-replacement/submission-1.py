class Solution:
    def characterReplacement(self, s: str, k: int) -> int:  
        '''
        The max window size is mostFreqChar + k
        '''
        L = 0
        R = 0
        freqMap = {}
        maxLength = 0
        maxFreq = 0
        while R < len(s):
            length = R - L + 1
            if s[R] in freqMap:
                freqMap[s[R]] += 1
            else: 
                freqMap[s[R]] = 1
            
            maxFreq = max(maxFreq, freqMap[s[R]])
            if length - maxFreq > k:
                freqMap[s[L]] -= 1
                L += 1
                length = R - L + 1

            maxLength = max(length, maxLength)
            R += 1

        return maxLength




            
                


        


        