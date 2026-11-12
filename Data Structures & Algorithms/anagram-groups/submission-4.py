class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        res = []
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            freq = tuple(freq)
            if freq in lookup: 
                res[lookup[freq]].append(word)
            else:
                res.append([word])
                lookup[freq] = len(res) - 1
        
        return res
