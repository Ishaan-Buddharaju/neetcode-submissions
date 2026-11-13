from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = {}
        for char in t: 
            t_freq[char] = 1 if char not in t_freq else t_freq[char] + 1
        state_freq = defaultdict(int) # track the state of current window

        minLength = float('inf')
        minSubstring = ""
        currSubstring = ""
        L = 0
        R = 0
        satisfied = 0
        valid = False
        while (R < len(s) or valid):
            if valid:
                if len(currSubstring) < minLength:
                    minLength = len(currSubstring)
                    minSubstring = currSubstring
                if s[L] in state_freq:
                    state_freq[s[L]] -= 1
                    if state_freq[s[L]] < t_freq[s[L]]:
                        satisfied -= 1
                        valid = False    
                currSubstring = currSubstring[1:]
                L += 1
            else: 
                if s[R] in t_freq:
                    state_freq[s[R]] += 1
                    if state_freq[s[R]] == t_freq[s[R]]:
                        satisfied += 1
                currSubstring += s[R]
                R += 1
                valid = satisfied == len(t_freq)
        return minSubstring
            


