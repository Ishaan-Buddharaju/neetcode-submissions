class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = {}
        for char in s:
            if char in tracker.keys():
                tracker[char] += 1
            else:
                tracker[char] = 1
        
        for char in t:
            if char in tracker.keys():
                tracker[char] -= 1
            else: 
                return False

        for k,v in tracker.items():
            if v != 0: 
                return False
        
        return True

